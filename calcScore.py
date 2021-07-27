# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcScore.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from scoreTeam import Ui_MainWindow as ScoreWindow
import sqlite3
conn = sqlite3.connect("match.db")
cursorObj = conn.cursor()

class Ui_MainWindow(object):
    def __init__(self):
	self.score_window = QtWidgets.QMainWindow()
	self.score_obj = ScoreWindow()
	self.score_obj.setupUi(self.score_window)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 415)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scoreButton = QtWidgets.QPushButton(self.centralwidget)
        self.scoreButton.setGeometry(QtCore.QRect(190, 350, 131, 27))
        self.scoreButton.setObjectName("scoreButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 100, 431, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 120, 68, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 120, 68, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 30, 371, 17))
        self.label_3.setObjectName("label_3")
        self.teamBox = QtWidgets.QComboBox(self.centralwidget)
        self.teamBox.setGeometry(QtCore.QRect(100, 60, 85, 27))
        self.teamBox.setObjectName("teamBox")
        self.matchBox = QtWidgets.QComboBox(self.centralwidget)
        self.matchBox.setGeometry(QtCore.QRect(310, 60, 85, 27))
        self.matchBox.setObjectName("matchBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 150, 401, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PlayerList = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.PlayerList.setObjectName("PlayerList")
        self.horizontalLayout.addWidget(self.PlayerList)
        self.PointList = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.PointList.setObjectName("PointList")
        self.horizontalLayout.addWidget(self.PointList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
	self.teamBox.activated.connect(self.displayMatch)	
	self.matchBox.activated.connect(self.displayPlayer)
	self.scoreButton.clicked.connect(self.scoreWindow)

	cursorObj.execute("SELECT team_name FROM Team")
        team_data = cursorObj.fetchall()
        for row in set(team_data):
	    self.teamBox.addItem(row[0])    

    def displayMatch(self):
	team = self.teamBox.currentText()
	cursorObj.execute("SELECT match FROM Team where team_name = '" + str(team) + "'")
	matchData = cursorObj.fetchall()
	self.matchBox.clear()
	for ele in set(matchData):
	    self.matchBox.addItem(str(ele[0]))
	    print(ele)

    def displayPlayer(self):
	team = self.teamBox.currentText()
	match = self.matchBox.currentText()
	cursorObj.execute("SELECT player, point from Team where match = '" + str(match) + "' and team_name = '" + str(team) + "'")
	playerData = cursorObj.fetchall()
	self.PlayerList.clear()
	self.PointList.clear()
	for ele in playerData:
	    print(ele)
	    self.PlayerList.addItem(ele[0])
	    self.PointList.addItem(str(ele[1]))

    def scoreWindow(self):
	sum = 0
	for index in range(self.PointList.count()):
	    ele = self.PointList.item(index)
	    sum = sum + int(ele.text())
	print(sum)
	self.score_obj.scoreBox.setText(str(sum))
	self.score_window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scoreButton.setText(_translate("MainWindow", "Calculate Score"))
        self.label.setText(_translate("MainWindow", "Players"))
        self.label_2.setText(_translate("MainWindow", "Points"))
        self.label_3.setText(_translate("MainWindow", "Evaluate the Performance of your Fantasy Team :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

