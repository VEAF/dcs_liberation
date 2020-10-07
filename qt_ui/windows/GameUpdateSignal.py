from __future__ import annotations

from typing import Optional

from PySide2.QtCore import QObject, Signal

from game import Game
from game.event import Event, Debriefing


class DebriefingSignal:

    def __init__(self, game, gameEvent, debriefing):
        self.game = game
        self.gameEvent = gameEvent
        self.debriefing = debriefing


class GameUpdateSignal(QObject):

    instance = None
    gameupdated = Signal(Game)
    budgetupdated = Signal(Game)
    debriefingReceived = Signal(DebriefingSignal)

    flight_paths_changed = Signal()

    def __init__(self):
        super(GameUpdateSignal, self).__init__()
        GameUpdateSignal.instance = self

    def redraw_flight_paths(self) -> None:
        # noinspection PyUnresolvedReferences
        self.flight_paths_changed.emit()

    def updateGame(self, game: Optional[Game]):
        # noinspection PyUnresolvedReferences
        self.gameupdated.emit(game)

    def updateBudget(self, game: Game):
        # noinspection PyUnresolvedReferences
        self.budgetupdated.emit(game)

    def sendDebriefing(self, game: Game, gameEvent: Event, debriefing: Debriefing):
        sig = DebriefingSignal(game, gameEvent, debriefing)
        # noinspection PyUnresolvedReferences
        self.gameupdated.emit(game)
        # noinspection PyUnresolvedReferences
        self.debriefingReceived.emit(sig)

    @staticmethod
    def get_instance() -> GameUpdateSignal:
        return GameUpdateSignal.instance
