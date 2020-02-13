from ..ui_generated.ui_stackedwidget import Ui_StackedWidget
from PyQt5.QtWidgets import QStackedWidget


class StackedWidget(QStackedWidget):

    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent)
        self.ui = Ui_StackedWidget()
        self.ui.setupUi(self)

    def setCurrentIndex(self, index):
        QStackedWidget.setCurrentIndex(self, index)
