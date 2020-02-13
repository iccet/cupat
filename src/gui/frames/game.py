from PyQt5.QtWidgets import QFrame
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QTimer, QBasicTimer
from ui_gameframe import Ui_GameFrame
from projects.tron import Tron

FPS = 60
RANDOM_EVENT_INTERVAL = REI = 5000


class GameFrame(QFrame):
    game = None
    _root = None

    def __init__(self, parent, root):
        super().__init__(parent)
        self._root = root
        self.game = Tron(self._root)
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
        del self.game
        del self.timer

    def timerEvent(self, event):
        self.game.update()
        self.update()

    def mouseReleaseEvent(self, QMouseEvent):
        self.game._player.move_vector = (QMouseEvent.x(), QMouseEvent.y())

    def mouseMoveEvent(self, QMouseEvent):
        self.game._player.move_vector = (QMouseEvent.x(), QMouseEvent.y())

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.game.render(qp)
        qp.end()

    def ready(self):
        """ readyPushBtn click event """
        self.game._player.ready = True

    def update(self):
        self.ui.forceLcdNumber.display(abs(self.game._random_force.force))
        self.ui.speedLcdNumber.display(abs(self.game._player.speed.force))
