from PyQt5.QtWidgets import QDialog
from ui_dialogwindow import Ui_Dialog
from PyQt5.QtCore import QCoreApplication


class Dialog(QDialog):
    def __init__(self, title, text, action):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle(title)
        self.ui.label.setText(QCoreApplication.translate(title, text))

        self.ui.buttonBox.button(self.ui.buttonBox.Ok).clicked.connect(action)
        self.ui.buttonBox.button(self.ui.buttonBox.Cancel).clicked.connect(self.close)
        self.show()

