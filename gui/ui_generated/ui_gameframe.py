# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Code\Python\cupat\static\ui\gameframe.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameFrame(object):
    def setupUi(self, GameFrame):
        GameFrame.setObjectName("GameFrame")
        GameFrame.resize(683, 385)
        self.verticalLayout = QtWidgets.QVBoxLayout(GameFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 5, 1, 1)
        self.forceVectorLabel = QtWidgets.QLabel(GameFrame)
        self.forceVectorLabel.setObjectName("forceVectorLabel")
        self.gridLayout.addWidget(self.forceVectorLabel, 0, 0, 1, 1)
        self.readyPushBtn = QtWidgets.QPushButton(GameFrame)
        self.readyPushBtn.setObjectName("readyPushBtn")
        self.gridLayout.addWidget(self.readyPushBtn, 2, 2, 1, 1)
        self.speedLabel = QtWidgets.QLabel(GameFrame)
        self.speedLabel.setObjectName("speedLabel")
        self.gridLayout.addWidget(self.speedLabel, 2, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        self.speedLcdNumber = QtWidgets.QLCDNumber(GameFrame)
        self.speedLcdNumber.setMinimumSize(QtCore.QSize(0, 0))
        self.speedLcdNumber.setBaseSize(QtCore.QSize(0, 0))
        self.speedLcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.speedLcdNumber.setDigitCount(4)
        self.speedLcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.speedLcdNumber.setObjectName("speedLcdNumber")
        self.gridLayout.addWidget(self.speedLcdNumber, 2, 6, 1, 1)
        self.forceLcdNumber = QtWidgets.QLCDNumber(GameFrame)
        self.forceLcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.forceLcdNumber.setDigitCount(4)
        self.forceLcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.forceLcdNumber.setObjectName("forceLcdNumber")
        self.gridLayout.addWidget(self.forceLcdNumber, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(GameFrame)
        QtCore.QMetaObject.connectSlotsByName(GameFrame)

    def retranslateUi(self, GameFrame):
        _translate = QtCore.QCoreApplication.translate
        GameFrame.setWindowTitle(_translate("GameFrame", "GameFrame"))
        self.forceVectorLabel.setText(_translate("GameFrame", "Force"))
        self.readyPushBtn.setText(_translate("GameFrame", "Ready"))
        self.speedLabel.setText(_translate("GameFrame", "Speed"))
