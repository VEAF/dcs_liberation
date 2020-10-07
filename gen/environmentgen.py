import logging
import random
from datetime import timedelta

from dcs.mission import Mission
from dcs.weather import Weather, Wind

from .conflictgen import Conflict

WEATHER_CLOUD_BASE = 2000, 3000
WEATHER_CLOUD_DENSITY = 1, 8
WEATHER_CLOUD_THICKNESS = 100, 400
WEATHER_CLOUD_BASE_MIN = 1600

WEATHER_FOG_CHANCE = 20
WEATHER_FOG_VISIBILITY = 2500, 5000
WEATHER_FOG_THICKNESS = 100, 500

RANDOM_TIME = {
    "night": 7,
    "dusk": 40,
    "dawn": 40,
    "day": 100,
}

RANDOM_WEATHER = {
    1: 0,  # thunderstorm
    2: 20,  # rain
    3: 80,  # clouds
    4: 100,  # clear
}


class EnvironmentSettings:
    weather_dict = None
    start_time = None


class EnviromentGenerator:
    def __init__(self, mission: Mission, conflict: Conflict, game):
        self.mission = mission
        self.conflict = conflict
        self.game = game

    def _gen_time(self):

        start_time = self.game.current_day

        daytime = self.game.current_turn_daytime
        logging.info("Mission time will be {}".format(daytime))
        if self.game.settings.night_disabled:
            logging.info("Skip Night mission due to user settings")
            if daytime == "dawn":
                time_range = (8, 9)
            elif daytime == "day":
                time_range = (10, 12)
            elif daytime == "dusk":
                time_range = (12, 14)
            elif daytime == "night":
                time_range = (14, 17)
            else:
                time_range = (10, 12)
        else:
            time_range = self.game.theater.daytime_map[daytime]

        start_time += timedelta(hours=random.randint(*time_range))

        logging.info("time - {}, slot - {}, night skipped - {}".format(
            str(start_time),
            str(time_range),
            self.game.settings.night_disabled))

        self.mission.start_time = start_time

    def _generate_wind(self, wind_speed, wind_direction=None):
        # wind
        if not wind_direction:
            wind_direction = random.randint(0, 360)

        self.mission.weather.wind_at_ground = Wind(wind_direction, wind_speed)
        self.mission.weather.wind_at_2000 = Wind(wind_direction, wind_speed * 2)
        self.mission.weather.wind_at_8000 = Wind(wind_direction, wind_speed * 3)

    def _generate_base_weather(self):
        # clouds
        self.mission.weather.clouds_base = random.randint(*WEATHER_CLOUD_BASE)
        self.mission.weather.clouds_density = random.randint(*WEATHER_CLOUD_DENSITY)
        self.mission.weather.clouds_thickness = random.randint(*WEATHER_CLOUD_THICKNESS)

        # wind
        self._generate_wind(random.randint(0, 4))

        # fog
        if random.randint(0, 100) < WEATHER_FOG_CHANCE:
            self.mission.weather.fog_visibility = random.randint(*WEATHER_FOG_VISIBILITY)
            self.mission.weather.fog_thickness = random.randint(*WEATHER_FOG_THICKNESS)

    def _gen_random_weather(self):
        weather_type = None
        for k, v in RANDOM_WEATHER.items():
            if random.randint(0, 100) <= v:
                weather_type = k
                break

        logging.info("generated weather {}".format(weather_type))
        if weather_type == 1:
            # thunderstorm
            self._generate_base_weather()
            self._generate_wind(random.randint(0, 8))

            self.mission.weather.clouds_density = random.randint(9, 10)
            self.mission.weather.clouds_iprecptns = Weather.Preceptions.Thunderstorm
        elif weather_type == 2:
            # rain
            self._generate_base_weather()
            self.mission.weather.clouds_density = random.randint(5, 8)
            self.mission.weather.clouds_iprecptns = Weather.Preceptions.Rain

            self._generate_wind(random.randint(0, 6))
        elif weather_type == 3:
            # clouds
            self._generate_base_weather()
        elif weather_type == 4:
            # clear
            pass

        if self.mission.weather.clouds_density > 0:
            # sometimes clouds are randomized way too low and need to be fixed
            self.mission.weather.clouds_base = max(self.mission.weather.clouds_base, WEATHER_CLOUD_BASE_MIN)

        if self.mission.weather.wind_at_ground.speed == 0:
            # frontline smokes look silly w/o any wind
            self._generate_wind(1)

    def generate(self) -> EnvironmentSettings:
        self._gen_time()
        self._gen_random_weather()

        settings = EnvironmentSettings()
        settings.start_time = self.mission.start_time
        settings.weather_dict = self.mission.weather.dict()
        return settings

    def load(self, settings: EnvironmentSettings):
        self.mission.start_time = settings.start_time
        self.mission.weather.load_from_dict(settings.weather_dict)

