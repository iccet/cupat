# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'static/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 494)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("static/ui/../static/icons/index.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.rootWidget = QtWidgets.QWidget(MainWindow)
        self.rootWidget.setObjectName("rootWidget")
        self.mainWindowWidgetGridLayout = QtWidgets.QGridLayout(self.rootWidget)
        self.mainWindowWidgetGridLayout.setObjectName("mainWindowWidgetGridLayout")
        MainWindow.setCentralWidget(self.rootWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cupat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
