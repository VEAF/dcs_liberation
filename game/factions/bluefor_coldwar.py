from dcs.helicopters import (
    SA342L,
    SA342M,
    UH_1H,
)
from dcs.planes import (
    AJS37,
    A_10A,
    C_130,
    E_3A,
    F_14B,
    F_4E,
    F_5E_3,
    KC130,
    KC_135,
)
from dcs.ships import (
    Armed_speedboat,
    CVN_74_John_C__Stennis,
    LHA_1_Tarawa,
)
from dcs.vehicles import (
    AirDefence,
    Armor,
    Infantry,
    Unarmed,
)

BLUEFOR_COLDWAR = {
    "country": "Combined Joint Task Forces Blue",
    "side": "blue",
    "units": [

        F_14B,
        F_4E,
        F_5E_3,
        A_10A,
        AJS37,

        KC_135,
        KC130,
        C_130,
        E_3A,

        UH_1H,
        SA342M,
        SA342L,

        Armor.MBT_M60A3_Patton,
        Armor.APC_M113,

        Unarmed.Transport_M818,
        Infantry.Infantry_M4,
        Infantry.Soldier_M249,

        AirDefence.SAM_Hawk_PCP,
        AirDefence.SAM_Chaparral_M48,

        CVN_74_John_C__Stennis,
        LHA_1_Tarawa,
        Armed_speedboat,
    ], "shorad": [
        AirDefence.AAA_Vulcan_M163,
    ], "aircraft_carrier": [
        CVN_74_John_C__Stennis,
    ], "helicopter_carrier": [
        LHA_1_Tarawa,
    ], "carrier_names": [
        "CVN-71 Theodore Roosevelt",
        "CVN-72 Abraham Lincoln",
        "CVN-73 George Washington",
        "CVN-74 John C. Stennis",
    ], "lhanames": [
        "LHA-1 Tarawa",
        "LHA-2 Saipan",
        "LHA-3 Belleau Wood",
        "LHA-4 Nassau",
        "LHA-5 Peleliu"
    ], "boat": [
    ], "has_jtac": True
}
