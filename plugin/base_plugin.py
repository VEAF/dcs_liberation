from game.game import Game
from qt_ui.windows.settings import QSettingsWindow
from PySide2.QtCore import QSize, Qt, QItemSelectionModel, QPoint
from PySide2.QtWidgets import QLabel, QDialog, QGridLayout, QListView, QStackedLayout, QComboBox, QWidget, \
    QAbstractItemView, QPushButton, QGroupBox, QCheckBox, QVBoxLayout, QSpinBox

class BasePlugin():
    nameInUI:str = "Base plugin"
    nameInSettings:str = "plugin.base"

    def __init__(self):
        self.uiWidget: QCheckBox = None

    def setupUI(self, settingsWindow: QSettingsWindow, row:int):
        if not self.nameInSettings in settingsWindow.game.settings.plugins:
            settingsWindow.game.settings.plugins[self.nameInSettings] = False

        self.uiWidget = QCheckBox()
        self.uiWidget.setChecked(settingsWindow.game.settings.plugins[self.nameInSettings])
        self.uiWidget.toggled.connect(lambda: self.applySetting(settingsWindow))

        settingsWindow.pluginsGroupLayout.addWidget(QLabel(self.nameInUI), row, 0)
        settingsWindow.pluginsGroupLayout.addWidget(self.uiWidget, row, 1, Qt.AlignRight)

    def applySetting(self, settingsWindow: QSettingsWindow):
        settingsWindow.game.settings.plugins[self.nameInSettings] = self.uiWidget.isChecked()

    def injectScripts(self):
        pass

    def injectConfiguration(self):
        pass

