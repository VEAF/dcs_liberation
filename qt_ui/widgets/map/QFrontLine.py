"""Common base for objects drawn on the game map."""
from typing import Optional

from PySide2.QtCore import Qt
from PySide2.QtGui import QPen
from PySide2.QtWidgets import (
    QAction,
    QGraphicsLineItem,
    QGraphicsSceneContextMenuEvent,
    QGraphicsSceneHoverEvent,
    QGraphicsSceneMouseEvent,
    QMenu,
)

import qt_ui.uiconstants as const
from qt_ui.dialogs import Dialog
from qt_ui.windows.mission.QPackageDialog import QNewPackageDialog
from theater.missiontarget import MissionTarget


class QFrontLine(QGraphicsLineItem):
    """Base class for objects drawn on the game map.

    Game map objects have an on_click behavior that triggers on left click, and
    change the mouse cursor on hover.
    """

    def __init__(self, x1: float, y1: float, x2: float, y2: float,
                 mission_target: MissionTarget) -> None:
        super().__init__(x1, y1, x2, y2)
        self.mission_target = mission_target
        self.new_package_dialog: Optional[QNewPackageDialog] = None
        self.setAcceptHoverEvents(True)

        pen = QPen(brush=const.COLORS["bright_red"])
        pen.setColor(const.COLORS["orange"])
        pen.setWidth(8)
        self.setPen(pen)

    def hoverEnterEvent(self, event: QGraphicsSceneHoverEvent):
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        if event.button() == Qt.LeftButton:
            self.on_click()

    def contextMenuEvent(self, event: QGraphicsSceneContextMenuEvent) -> None:
        menu = QMenu("Menu")

        object_details_action = QAction(self.object_dialog_text)
        object_details_action.triggered.connect(self.on_click)
        menu.addAction(object_details_action)

        new_package_action = QAction(f"New package")
        new_package_action.triggered.connect(self.open_new_package_dialog)
        menu.addAction(new_package_action)

        menu.exec_(event.screenPos())

    @property
    def object_dialog_text(self) -> str:
        """Text to for the object's dialog in the context menu.

        Right clicking a map object will open a context menu and the first item
        will open the details dialog for this object. This menu action has the
        same behavior as the on_click event.

        Return:
            The text that should be displayed for the menu item.
        """
        return "Details"

    def on_click(self) -> None:
        """The action to take when this map object is left-clicked.

        Typically this should open a details view of the object.
        """
        raise NotImplementedError

    def open_new_package_dialog(self) -> None:
        """Opens the dialog for planning a new mission package."""
        Dialog.open_new_package_dialog(self.mission_target)
