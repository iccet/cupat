from PyQt5.QtWidgets import QFrame
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QTimer, QBasicTimer

from gui.ui_generated.ui_gameframe import Ui_GameFrame
from src.core.obj.render import RenderObject, FPS

RANDOM_EVENT_INTERVAL = REI = 5000


class GameFrame(QFrame):
    game = None
    painter = QPainter()

    def __init__(self, parent):
        super().__init__(parent)
        RenderObject.painter = self.painter

        self.ui = Ui_GameFrame()
        self.ui.setupUi(self)
        self.ui.readyPushBtn.clicked.connect(self.ready)

        self.timer = QBasicTimer()
        self.timer.start(1000 / FPS, self)

        self.rnd_timer = QTimer()
        self.rnd_timer.timeout.connect(self.game.random_event)
        self.rnd_timer.start(REI)

    def __del__(self):
        del self.ui
        del self.timer
        del GameFrame.game
        del GameFrame.painter

    def timerEvent(self, event):
        self.game.update()
        self.update()

    def mouseReleaseEvent(self, QMouseEvent):
        self.game.player.move_target = (QMouseEvent.x(), QMouseEvent.y())

    def mouseMoveEvent(self, QMouseEvent):
        self.game.player.move_target = (QMouseEvent.x(), QMouseEvent.y())

    def paintEvent(self, event):
        self.painter.begin(self)
        self.game.render()
        self.painter.end()

    def ready(self):
        """ readyPushBtn click event """
        self.game.player.ready = True

    def update(self):
        self.ui.forceLcdNumber.display(abs(self.game._random_force.value))
        self.ui.speedLcdNumber.display(abs(self.game.player.speed.value))
