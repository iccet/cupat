# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'static/ui/stackedwidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(918, 459)
        self.menuPage = QtWidgets.QWidget()
        self.menuPage.setObjectName("menuPage")
        self.gridLayout = QtWidgets.QGridLayout(self.menuPage)
        self.gridLayout.setObjectName("gridLayout")
        self.menuPageVerticalLayout = QtWidgets.QVBoxLayout()
        self.menuPageVerticalLayout.setObjectName("menuPageVerticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menuPageVerticalLayout.addItem(spacerItem)
        self.connectPushBtn = QtWidgets.QPushButton(self.menuPage)
        self.connectPushBtn.setMinimumSize(QtCore.QSize(100, 40))
        self.connectPushBtn.setStyleSheet("")
        self.connectPushBtn.setObjectName("connectPushBtn")
        self.menuPageVerticalLayout.addWidget(self.connectPushBtn)
        self.trainingPushBtn = QtWidgets.QPushButton(self.menuPage)
        self.trainingPushBtn.setMinimumSize(QtCore.QSize(100, 40))
        self.trainingPushBtn.setObjectName("trainingPushBtn")
        self.menuPageVerticalLayout.addWidget(self.trainingPushBtn)
        self.settingsPushBtn = QtWidgets.QPushButton(self.menuPage)
        self.settingsPushBtn.setMinimumSize(QtCore.QSize(100, 40))
        self.settingsPushBtn.setObjectName("settingsPushBtn")
        self.menuPageVerticalLayout.addWidget(self.settingsPushBtn)
        self.exitPushBtn = QtWidgets.QPushButton(self.menuPage)
        self.exitPushBtn.setMinimumSize(QtCore.QSize(100, 40))
        self.exitPushBtn.setObjectName("exitPushBtn")
        self.menuPageVerticalLayout.addWidget(self.exitPushBtn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menuPageVerticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.menuPageVerticalLayout, 0, 1, 2, 2)
        spacerItem2 = QtWidgets.QSpacerItem(424, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(424, 441, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        StackedWidget.addWidget(self.menuPage)
        self.gamePage = QtWidgets.QWidget()
        self.gamePage.setObjectName("gamePage")
        self.gamePageaGridLayout = QtWidgets.QGridLayout(self.gamePage)
        self.gamePageaGridLayout.setObjectName("gamePageaGridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.gamePage)
        self.groupBox.setObjectName("groupBox")
        self.gamePageaGridLayout.addWidget(self.groupBox, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gamePage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gamePageaGridLayout.addWidget(self.groupBox_2, 0, 0, 2, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.gamePage)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gamePageaGridLayout.addWidget(self.groupBox_3, 0, 2, 2, 1)
        self.gameFrame = QtWidgets.QFrame(self.gamePage)
        self.gameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gameFrame.setObjectName("gameFrame")
        self.gamePageaGridLayout.addWidget(self.gameFrame, 0, 1, 1, 1)
        StackedWidget.addWidget(self.gamePage)
        self.settingsPage = QtWidgets.QWidget()
        self.settingsPage.setObjectName("settingsPage")
        self.settingsPageVerticalLayout = QtWidgets.QVBoxLayout(self.settingsPage)
        self.settingsPageVerticalLayout.setObjectName("settingsPageVerticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.settingsPage)
        self.tabWidget.setObjectName("tabWidget")
        self.gameTab = QtWidgets.QWidget()
        self.gameTab.setObjectName("gameTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gameTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.choosePlayerColorPushBtn = QtWidgets.QPushButton(self.gameTab)
        self.choosePlayerColorPushBtn.setObjectName("choosePlayerColorPushBtn")
        self.gridLayout_2.addWidget(self.choosePlayerColorPushBtn, 4, 3, 1, 1)
        self.playerShapeComboBox = QtWidgets.QComboBox(self.gameTab)
        self.playerShapeComboBox.setCurrentText("")
        self.playerShapeComboBox.setFrame(True)
        self.playerShapeComboBox.setObjectName("playerShapeComboBox")
        self.gridLayout_2.addWidget(self.playerShapeComboBox, 6, 2, 1, 1)
        self.playerColorLabel = QtWidgets.QLabel(self.gameTab)
        self.playerColorLabel.setObjectName("playerColorLabel")
        self.gridLayout_2.addWidget(self.playerColorLabel, 4, 0, 1, 1)
        self.playerShapeLabel = QtWidgets.QLabel(self.gameTab)
        self.playerShapeLabel.setObjectName("playerShapeLabel")
        self.gridLayout_2.addWidget(self.playerShapeLabel, 6, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.gameTab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 8, 0, 1, 1)
        self.restoreGameSettingsPushBtn = QtWidgets.QPushButton(self.gameTab)
        self.restoreGameSettingsPushBtn.setObjectName("restoreGameSettingsPushBtn")
        self.gridLayout_2.addWidget(self.restoreGameSettingsPushBtn, 13, 1, 1, 1)
        self.playerNameLabel = QtWidgets.QLabel(self.gameTab)
        self.playerNameLabel.setObjectName("playerNameLabel")
        self.gridLayout_2.addWidget(self.playerNameLabel, 2, 0, 1, 1)
        self.HUDSubMenuLabel = QtWidgets.QLabel(self.gameTab)
        self.HUDSubMenuLabel.setObjectName("HUDSubMenuLabel")
        self.gridLayout_2.addWidget(self.HUDSubMenuLabel, 7, 0, 1, 1)
        self.acceptGameSettingsPushBtn = QtWidgets.QPushButton(self.gameTab)
        self.acceptGameSettingsPushBtn.setObjectName("acceptGameSettingsPushBtn")
        self.gridLayout_2.addWidget(self.acceptGameSettingsPushBtn, 13, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 13, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 13, 2, 1, 1)
        self.hudSizeColorLabel = QtWidgets.QLabel(self.gameTab)
        self.hudSizeColorLabel.setObjectName("hudSizeColorLabel")
        self.gridLayout_2.addWidget(self.hudSizeColorLabel, 10, 0, 1, 1)
        self.PlayerSubMenuLabel = QtWidgets.QLabel(self.gameTab)
        self.PlayerSubMenuLabel.setObjectName("PlayerSubMenuLabel")
        self.gridLayout_2.addWidget(self.PlayerSubMenuLabel, 0, 0, 1, 1)
        self.playerColorComboBox = QtWidgets.QComboBox(self.gameTab)
        self.playerColorComboBox.setCurrentText("")
        self.playerColorComboBox.setFrame(True)
        self.playerColorComboBox.setObjectName("playerColorComboBox")
        self.gridLayout_2.addWidget(self.playerColorComboBox, 4, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.gameTab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.HUDSizeHorizontalSlider = QtWidgets.QSlider(self.gameTab)
        self.HUDSizeHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.HUDSizeHorizontalSlider.setObjectName("HUDSizeHorizontalSlider")
        self.gridLayout_2.addWidget(self.HUDSizeHorizontalSlider, 10, 2, 1, 1)
        self.showHUDCheckBox = QtWidgets.QCheckBox(self.gameTab)
        self.showHUDCheckBox.setObjectName("showHUDCheckBox")
        self.gridLayout_2.addWidget(self.showHUDCheckBox, 9, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 11, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 13, 3, 1, 1)
        self.enableHUDLabel = QtWidgets.QLabel(self.gameTab)
        self.enableHUDLabel.setObjectName("enableHUDLabel")
        self.gridLayout_2.addWidget(self.enableHUDLabel, 9, 0, 1, 1)
        self.playerNameLineEdit = QtWidgets.QLineEdit(self.gameTab)
        self.playerNameLineEdit.setObjectName("playerNameLineEdit")
        self.gridLayout_2.addWidget(self.playerNameLineEdit, 2, 2, 1, 1)
        self.playerTrackColorLabel = QtWidgets.QLabel(self.gameTab)
        self.playerTrackColorLabel.setObjectName("playerTrackColorLabel")
        self.gridLayout_2.addWidget(self.playerTrackColorLabel, 5, 0, 1, 1)
        self.playerTrackColorComboBox = QtWidgets.QComboBox(self.gameTab)
        self.playerTrackColorComboBox.setCurrentText("")
        self.playerTrackColorComboBox.setFrame(True)
        self.playerTrackColorComboBox.setObjectName("playerTrackColorComboBox")
        self.gridLayout_2.addWidget(self.playerTrackColorComboBox, 5, 2, 1, 1)
        self.choosePlayerTrackColorPushBtn = QtWidgets.QPushButton(self.gameTab)
        self.choosePlayerTrackColorPushBtn.setObjectName("choosePlayerTrackColorPushBtn")
        self.gridLayout_2.addWidget(self.choosePlayerTrackColorPushBtn, 5, 3, 1, 1)
        self.tabWidget.addTab(self.gameTab, "")
        self.networkTab = QtWidgets.QWidget()
        self.networkTab.setObjectName("networkTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.networkTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 8, 4, 1, 1)
        self.hostSubMenuLabel = QtWidgets.QLabel(self.networkTab)
        self.hostSubMenuLabel.setObjectName("hostSubMenuLabel")
        self.gridLayout_4.addWidget(self.hostSubMenuLabel, 0, 0, 1, 1)
        self.adressLEdit = QtWidgets.QLineEdit(self.networkTab)
        self.adressLEdit.setObjectName("adressLEdit")
        self.gridLayout_4.addWidget(self.adressLEdit, 2, 2, 1, 1)
        self.restoreNetworkSettingsPushBtn = QtWidgets.QPushButton(self.networkTab)
        self.restoreNetworkSettingsPushBtn.setObjectName("restoreNetworkSettingsPushBtn")
        self.gridLayout_4.addWidget(self.restoreNetworkSettingsPushBtn, 8, 1, 1, 1)
        self.clientSubMenuLabel = QtWidgets.QLabel(self.networkTab)
        self.clientSubMenuLabel.setObjectName("clientSubMenuLabel")
        self.gridLayout_4.addWidget(self.clientSubMenuLabel, 5, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 251, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem9, 7, 2, 1, 1)
        self.privateHostCheckBox = QtWidgets.QCheckBox(self.networkTab)
        self.privateHostCheckBox.setObjectName("privateHostCheckBox")
        self.gridLayout_4.addWidget(self.privateHostCheckBox, 3, 2, 1, 1)
        self.adressLabel = QtWidgets.QLabel(self.networkTab)
        self.adressLabel.setObjectName("adressLabel")
        self.gridLayout_4.addWidget(self.adressLabel, 2, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 8, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem11, 8, 3, 1, 1)
        self.acceptNetworkSettingsPushBtn = QtWidgets.QPushButton(self.networkTab)
        self.acceptNetworkSettingsPushBtn.setObjectName("acceptNetworkSettingsPushBtn")
        self.gridLayout_4.addWidget(self.acceptNetworkSettingsPushBtn, 8, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.networkTab)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_4.addWidget(self.line_4, 6, 0, 1, 1)
        self.privateHostLabel = QtWidgets.QLabel(self.networkTab)
        self.privateHostLabel.setObjectName("privateHostLabel")
        self.gridLayout_4.addWidget(self.privateHostLabel, 3, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.networkTab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.networkTab, "")
        self.profileTab = QtWidgets.QWidget()
        self.profileTab.setObjectName("profileTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.profileTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem12 = QtWidgets.QSpacerItem(20, 349, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem12, 2, 1, 1, 1)
        self.statisticSubMenuLabel = QtWidgets.QLabel(self.profileTab)
        self.statisticSubMenuLabel.setObjectName("statisticSubMenuLabel")
        self.gridLayout_5.addWidget(self.statisticSubMenuLabel, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(726, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem13, 3, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.profileTab)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_5.addWidget(self.line_5, 1, 0, 1, 1)
        self.tabWidget.addTab(self.profileTab, "")
        self.settingsPageVerticalLayout.addWidget(self.tabWidget)
        StackedWidget.addWidget(self.settingsPage)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.connectPushBtn.setText(_translate("StackedWidget", "Connect"))
        self.trainingPushBtn.setText(_translate("StackedWidget", "Training"))
        self.settingsPushBtn.setText(_translate("StackedWidget", "Settings"))
        self.exitPushBtn.setText(_translate("StackedWidget", "Exit"))
        self.groupBox.setTitle(_translate("StackedWidget", "GroupBox"))
        self.groupBox_2.setTitle(_translate("StackedWidget", "GroupBox"))
        self.groupBox_3.setTitle(_translate("StackedWidget", "GroupBox"))
        self.choosePlayerColorPushBtn.setText(_translate("StackedWidget", "Choose color"))
        self.playerColorLabel.setText(_translate("StackedWidget", "Color"))
        self.playerShapeLabel.setText(_translate("StackedWidget", "Shape"))
        self.restoreGameSettingsPushBtn.setText(_translate("StackedWidget", "Restore"))
        self.playerNameLabel.setText(_translate("StackedWidget", "Name"))
        self.HUDSubMenuLabel.setText(_translate("StackedWidget", "HUD:"))
        self.acceptGameSettingsPushBtn.setText(_translate("StackedWidget", "Accept"))
        self.hudSizeColorLabel.setText(_translate("StackedWidget", "Size"))
        self.PlayerSubMenuLabel.setText(_translate("StackedWidget", "Player:"))
        self.showHUDCheckBox.setText(_translate("StackedWidget", "on/off"))
        self.enableHUDLabel.setText(_translate("StackedWidget", "Enable"))
        self.playerNameLineEdit.setText(_translate("StackedWidget", "Player"))
        self.playerTrackColorLabel.setText(_translate("StackedWidget", "Track color"))
        self.choosePlayerTrackColorPushBtn.setText(_translate("StackedWidget", "Choose color"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gameTab), _translate("StackedWidget", "Game"))
        self.hostSubMenuLabel.setText(_translate("StackedWidget", "Host:"))
        self.adressLEdit.setText(_translate("StackedWidget", "127.0.1.1:5000"))
        self.restoreNetworkSettingsPushBtn.setText(_translate("StackedWidget", "Restore"))
        self.clientSubMenuLabel.setText(_translate("StackedWidget", "Client:"))
        self.privateHostCheckBox.setText(_translate("StackedWidget", "on/off"))
        self.adressLabel.setText(_translate("StackedWidget", "Adress"))
        self.acceptNetworkSettingsPushBtn.setText(_translate("StackedWidget", "Accept"))
        self.privateHostLabel.setText(_translate("StackedWidget", "Private"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.networkTab), _translate("StackedWidget", "Network"))
        self.statisticSubMenuLabel.setText(_translate("StackedWidget", "Statistic:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profileTab), _translate("StackedWidget", "Profile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StackedWidget = QtWidgets.QStackedWidget()
    ui = Ui_StackedWidget()
    ui.setupUi(StackedWidget)
    StackedWidget.show()
    sys.exit(app.exec_())
