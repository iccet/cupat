from PyQt5.QtWidgets import QMainWindow, QColorDialog
from PyQt5.QtCore import QBasicTimer, Qt, QCoreApplication, pyqtSlot, QPropertyAnimation, QRect
from ui_mainwindow import Ui_MainWindow
from ..widgets.stacked import StackedWidget
from .dialog import Dialog
from frames.game import GameFrame
from src.templates.player import Player, BASIC_SHAPES
from src.base_game import BaseGame
from samples.tron import Tron
from samples.colors import Colors
from src.core.obj.render import FPS


class MainWindow(QMainWindow):
    dialog = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stackedWidget = StackedWidget(self)
        self.ui.mainWindowWidgetGridLayout.addWidget(self.stackedWidget)

        self.timer = QBasicTimer()
        self.timer.start(1000 / FPS, self)

        self.buttonsMapping()
        self.loadContent()
        self.loadStyleSheets()

    def timerEvent(self, event):
        self.update()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Escape:
            if not self.stackedWidget.currentIndex():
                self.exit()
            self.stackedWidget.setCurrentIndex(0)

    def gameFrameInit(self):
        self.stackedWidget.ui.gameFrame = GameFrame(self.stackedWidget.ui.gamePage)
        self.stackedWidget.ui.gamePageaGridLayout.addWidget(self.stackedWidget.ui.gameFrame, 0, 1, 1, 1)

    def buttonsMapping(self):
        self.stackedWidget.ui.connectPushBtn.clicked.connect(self.connect)
        self.stackedWidget.ui.settingsPushBtn.clicked.connect(self.settings)
        self.stackedWidget.ui.trainingPushBtn.clicked.connect(self.training)
        self.stackedWidget.ui.exitPushBtn.clicked.connect(self.exit)
        self.stackedWidget.ui.choosePlayerColorPushBtn.clicked.connect(self.chooseColor)
        self.stackedWidget.ui.choosePlayerTrackColorPushBtn.clicked.connect(self.chooseColor)

    def loadContent(self):
        self.stackedWidget.ui.playerColorComboBox.addItems(Colors())
        self.stackedWidget.ui.playerTrackColorComboBox.addItems(Colors())
        self.stackedWidget.ui.playerShapeComboBox.addItems(BASIC_SHAPES)

    def loadStyleSheets(self):
        style = "static/qss/mainstyle.qss"
        with open(style, "r") as f:
            self.setStyleSheet(f.read())

    def animation(self, widget):
        self._animation = QPropertyAnimation(widget, b'geometry')
        self._animation.setDuration(100)
        _x = widget.x()
        _y = widget.y()
        _w = widget.width()
        _h = widget.height()
        self._animation.setStartValue(QRect(_x, _y, _w, _h))
        self._animation.setKeyValueAt(0.5, QRect(_x - 10, _y - 10, _w + 20, _h + 20))
        self._animation.setEndValue(QRect(_x, _y, _w, _h))
        self._animation.start()

    def connect(self):
        """ connectPushBtn click event """
        self.animation(self.stackedWidget.ui.connectPushBtn)

    def training(self):
        """ trainingPushBtn click event """
        self.buildGame()
        self.gameFrameInit()
        self.animation(self.stackedWidget.ui.trainingPushBtn)
        self.stackedWidget.setCurrentIndex(1)

    def settings(self):
        """ settingsPushBtn click event """
        self.animation(self.stackedWidget.ui.settingsPushBtn)
        self.stackedWidget.setCurrentIndex(2)

    def exit(self):
        """ exitPushBtn click event """
        self.animation(self.stackedWidget.ui.exitPushBtn)
        self.dialog = Dialog("Exit", "Are you sure about exit?", QCoreApplication.quit)

    @pyqtSlot()
    def chooseColor(self):
        return QColorDialog.getColor()

    def buildGame(self):
        BaseGame.player = self.buildPlayer()
        GameFrame.game = Tron()  # TODO remove default from here, swap by abstract game

    def buildPlayer(self) -> Player:
        _x = self.frameGeometry().width()
        _y = self.frameGeometry().height()
        player_position = [_x / 2, _y / 2]

        player_shape = self.stackedWidget.ui.playerShapeComboBox.currentText()
        track_color = self.stackedWidget.ui.playerTrackColorComboBox.currentText()
        player_color = self.stackedWidget.ui.playerColorComboBox.currentText()
        player_name = self.stackedWidget.ui.playerNameLineEdit.text()

        return Player(position=player_position,
                      shape=BASIC_SHAPES[player_shape],
                      color=player_color,
                      track_color=track_color,
                      name=player_name)
