from PyQt5.QtWidgets import QMainWindow, QColorDialog
from PyQt5.QtCore import QBasicTimer, Qt, QCoreApplication, pyqtSlot, \
    QPropertyAnimation, QRect
from ui_mainwindow import Ui_MainWindow
from ..widgets.stacked import StackedWidget
from .dialog import Dialog
from frames.game import GameFrame

FPS = 60

BLUE = "#2980b9"
RED = "#ce4250"
ORANGE = "#f59e16"
GREEN = "#268C52"
MAGENTA = "#bd93f9"
PURPLE = "#f676c0"

DARK_BLUE = "#07086f"
REGULAR_BLUE = "#0005e3"
TURQ_BLUE = "#28dfff"
LIGHT_BLUE = "#2494ea"

GRAY = "#31363b"
BLACK = "#23262a"
WHITE = "#eff0f1"

MAIN_COLORS = [GREEN, RED, BLUE, ORANGE, MAGENTA, PURPLE]
BASIC_SHAPES = ("cursor", "arrow", "rocket", "triangle")


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
        self.gameFrameInit()

    def gameFrameInit(self):
        self.stackedWidget.ui.gameFrame = GameFrame(self.stackedWidget.ui.gamePage, self)
        self.stackedWidget.ui.gamePageaGridLayout.addWidget(self.stackedWidget.ui.gameFrame, 0, 1, 1, 1)

    def buttonsMapping(self):
        self.stackedWidget.ui.connectPushBtn.clicked.connect(self.connect)
        self.stackedWidget.ui.settingsPushBtn.clicked.connect(self.settings)
        self.stackedWidget.ui.trainingPushBtn.clicked.connect(self.training)
        self.stackedWidget.ui.exitPushBtn.clicked.connect(self.exit)
        self.stackedWidget.ui.choosePlayerColorPushBtn.clicked.connect(self.choose_color)
        self.stackedWidget.ui.choosePlayerTrackColorPushBtn.clicked.connect(self.choose_color)

    def loadContent(self):
        self.stackedWidget.ui.playerColorComboBox.addItems(MAIN_COLORS)
        self.stackedWidget.ui.playerTrackColorComboBox.addItems(MAIN_COLORS)
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
        self.stackedWidget.setCurrentIndex(1)

    def settings(self):
        """ settingsPushBtn click event """
        self.stackedWidget.setCurrentIndex(2)

    def exit(self):
        """ exitPushBtn click event """
        self.animation(self.stackedWidget.ui.exitPushBtn)
        self.dialog = Dialog("Exit", "Are you sure about exit?", QCoreApplication.quit)

    @pyqtSlot()
    def choose_color(self):
        return QColorDialog.getColor()

    def receive_player_position(self):
        _x = self.frameGeometry().width()
        _y = self.frameGeometry().height()
        return [_x / 2, _y / 2]

    def receive_player_shape(self):
        return self.stackedWidget.ui.playerShapeComboBox.currentText()

    def receive_player_name(self):
        return self.stackedWidget.ui.playerNameLineEdit.text()

    def receive_player_track_color(self):
        return self.stackedWidget.ui.playerTrackColorComboBox.currentText()

    def receive_player_color(self):
        return self.stackedWidget.ui.playerColorComboBox.currentText()

    def timerEvent(self, event):
        self.update()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Escape:
            if not self.stackedWidget.currentIndex():
                self.exit()
            self.stackedWidget.setCurrentIndex(0)
