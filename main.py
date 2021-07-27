# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from createTeam import Ui_MainWindow as CreateTeam
from openTeam import Ui_MainWindow as OpenTeam
from calcScore import Ui_MainWindow as CalcScore
from PyQt5.QtWidgets import QMessageBox
import sqlite3
conn = sqlite3.connect("match.db")
cursorObj = conn.cursor()


class Ui_MainWindow(object):
    def __init__(self):
	self.max_BAT = 4
	self.max_BWL = 3
	self.max_WK = 1
	self.max_AR = 3
	self.create_window = QtWidgets.QMainWindow()
	self.create_obj = CreateTeam()
	self.create_obj.setupUi(self.create_window)
	self.open_window = QtWidgets.QMainWindow()
	self.open_obj = OpenTeam()
	self.open_obj.setupUi(self.open_window)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 611, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bowler_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.bowler_label.setObjectName("bowler_label")
        self.horizontalLayout.addWidget(self.bowler_label)
        self.bowler_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.bowler_text.setObjectName("bowler_text")
        self.horizontalLayout.addWidget(self.bowler_text)
        self.batsmen_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.batsmen_label.setObjectName("batsmen_label")
        self.horizontalLayout.addWidget(self.batsmen_label)
        self.batsmen_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.batsmen_text.setObjectName("batsmen_text")
        self.horizontalLayout.addWidget(self.batsmen_text)
        self.rounders_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.rounders_label.setObjectName("rounders_label")
        self.horizontalLayout.addWidget(self.rounders_label)
        self.rounders_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.rounders_text.setObjectName("rounders_text")
        self.horizontalLayout.addWidget(self.rounders_text)
        self.wicket_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.wicket_label.setObjectName("wicket_label")
        self.horizontalLayout.addWidget(self.wicket_label)
        self.wicket_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.wicket_text.setObjectName("wicket_text")
        self.horizontalLayout.addWidget(self.wicket_text)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 111, 31))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(470, 170, 121, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.points_used = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.points_used.setObjectName("points_used")
        self.horizontalLayout_2.addWidget(self.points_used)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 170, 151, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.points_available = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.points_available.setObjectName("points_available")
        self.horizontalLayout_3.addWidget(self.points_available)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(60, 120, 491, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bowler_radio = QtWidgets.QRadioButton(self.horizontalLayoutWidget_6)
        self.bowler_radio.setEnabled(False)
        self.bowler_radio.setObjectName("bowler_radio")
        self.horizontalLayout_6.addWidget(self.bowler_radio)
        self.batsmen_radio = QtWidgets.QRadioButton(self.horizontalLayoutWidget_6)
        self.batsmen_radio.setEnabled(False)
        self.batsmen_radio.setObjectName("batsmen_radio")
        self.horizontalLayout_6.addWidget(self.batsmen_radio)
        self.rounders_radio = QtWidgets.QRadioButton(self.horizontalLayoutWidget_6)
        self.rounders_radio.setEnabled(False)
        self.rounders_radio.setObjectName("rounders_radio")
        self.horizontalLayout_6.addWidget(self.rounders_radio)
        self.wicket_radio = QtWidgets.QRadioButton(self.horizontalLayoutWidget_6)
        self.wicket_radio.setEnabled(False)
        self.wicket_radio.setObjectName("wicket_radio")
        self.horizontalLayout_6.addWidget(self.wicket_radio)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(200, 170, 241, 39))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.team_name_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.team_name_label.setObjectName("team_name_label")
        self.horizontalLayout_4.addWidget(self.team_name_label)
        self.team_name_box = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.team_name_box.setObjectName("team_name_box")
        self.horizontalLayout_4.addWidget(self.team_name_box)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 230, 581, 341))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.player_list = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.player_list.setObjectName("player_list")
        self.horizontalLayout_5.addWidget(self.player_list)
        self.final_list = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.final_list.setObjectName("final_list")
        self.horizontalLayout_5.addWidget(self.final_list)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.MANAGETeams = QtWidgets.QToolBar(MainWindow)
        self.MANAGETeams.setMouseTracking(True)
        self.MANAGETeams.setAcceptDrops(True)
        self.MANAGETeams.setAutoFillBackground(True)
        self.MANAGETeams.setObjectName("MANAGETeams")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.MANAGETeams)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 25))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.action_NEW = QtWidgets.QAction(MainWindow)
        self.action_NEW.setObjectName("action_NEW")
        self.action_SAVE = QtWidgets.QAction(MainWindow)
        self.action_SAVE.setObjectName("action_SAVE")
        self.action_OPEN = QtWidgets.QAction(MainWindow)
        self.action_OPEN.setObjectName("action_OPEN")
        self.action_EVALUATE = QtWidgets.QAction(MainWindow)
        self.action_EVALUATE.setObjectName("action_EVALUATE")
        self.NEW = QtWidgets.QAction(MainWindow)
        self.NEW.setObjectName("NEW")
        self.SAVE = QtWidgets.QAction(MainWindow)
        self.SAVE.setObjectName("SAVE")
        self.OPEN = QtWidgets.QAction(MainWindow)
        self.OPEN.setObjectName("OPEN")
        self.EVALUATE = QtWidgets.QAction(MainWindow)
        self.EVALUATE.setObjectName("EVALUATE")
        self.MANAGETeams.addSeparator()
        self.menuManage_Teams.addAction(self.NEW)
        self.menuManage_Teams.addAction(self.SAVE)
        self.menuManage_Teams.addAction(self.OPEN)
        self.menuManage_Teams.addAction(self.EVALUATE)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
	self.NEW.triggered.connect(self.create_team)
	self.SAVE.triggered.connect(self.save_team)
	self.OPEN.triggered.connect(self.open_team)
	self.EVALUATE.triggered.connect(self.calc_score)
	self.create_obj.pushButton.clicked.connect(self.show_team)
	self.open_obj.pushButton.clicked.connect(self.display_team)
	self.batsmen_radio.clicked.connect(self.show_player)
	self.bowler_radio.clicked.connect(self.show_player)
	self.rounders_radio.clicked.connect(self.show_player)
	self.wicket_radio.clicked.connect(self.show_player)
	self.player_list.doubleClicked.connect(self.add_player)
	self.final_list.doubleClicked.connect(self.remove_player)


    def create_team(self):
	self.max_BAT = 4
	self.max_BWL = 3
	self.max_WK = 1
	self.max_AR = 3
	self.create_obj.lineEdit.clear()
	self.create_window.show()


    def open_team(self):
	self.open_obj.lineEdit.clear()
	self.open_window.show()


    def save_team(self):
	team_name = self.team_name_box.text()
	print(team_name)
	cursorObj.execute("SELECT match FROM Team where team_name = '" + str(team_name) + "'")
	match_data = cursorObj.fetchall()
	if len(match_data) is not 0:
	    last_match = match_data[-1][0]
	    temp = int(last_match[-1])
	    temp = temp + 1
	    matches = 'Match' + str(temp)
	else:
	    matches = 'Match1'
	print(match_data)
	final_data = []
	for ele in range(self.final_list.count()):
	    final_data.append(self.final_list.item(ele).text())
	for elem in final_data:
	    cursorObj.execute("SELECT Points from Player where Player = '" + str(elem) +"'")
	    point = cursorObj.fetchall()
	    print(point)
	    cursorObj.execute("INSERT INTO Team VALUES (?, ?, ?, ?)",(team_name, elem, point[0][0], matches))
	    conn.commit()	


    def show_team(self):
        self.bowler_radio.setEnabled(True)
        self.batsmen_radio.setEnabled(True)
        self.rounders_radio.setEnabled(True)
        self.wicket_radio.setEnabled(True)
	self.player_list.clear()
	self.final_list.clear()	
	self.team_name_box.setText(self.create_obj.create())
	cursorObj.execute('SELECT sum(Points) from Player')
	score = cursorObj.fetchall()	
	print(score[0][0])
	self.points_available.setText(str(score[0][0]))
	cursorObj.execute('SELECT count(player) FROM Player where Type = "BAT"')
	bat_cnt = cursorObj.fetchall()
	self.batsmen_text.setText(str(bat_cnt[0][0]))
	cursorObj.execute('SELECT count(player) FROM Player where Type = "BWL"')
	bwl_cnt = cursorObj.fetchall()
	self.bowler_text.setText(str(bwl_cnt[0][0]))
	cursorObj.execute('SELECT count(player) FROM Player where Type = "AR"')
	ar_cnt = cursorObj.fetchall()
	self.rounders_text.setText(str(ar_cnt[0][0]))
	cursorObj.execute('SELECT count(player) FROM Player where Type = "WK"')
	wk_cnt = cursorObj.fetchall()
	self.wicket_text.setText(str(wk_cnt[0][0]))
	self.points_used.setText('00')
	

    def show_player(self):
	self.player_list.clear()
	final_data = []
	for ele in range(self.final_list.count()):
	    final_data.append(self.final_list.item(ele).text())
	if self.batsmen_radio.isChecked():
            cursorObj.execute('SELECT player from Player where Type = "BAT"')
	    playerList = cursorObj.fetchall()
	    for ele in playerList:
	        if ele[0] in list(final_data):
	    	    continue
		self.player_list.addItem(ele[0])
	elif self.bowler_radio.isChecked():
            cursorObj.execute('SELECT player from Player where Type = "BWL"')
	    playerList = cursorObj.fetchall()
	    for ele in playerList:
	        if ele[0] in list(final_data):
	    	    continue
	        self.player_list.addItem(ele[0])
	elif self.rounders_radio.isChecked():
            cursorObj.execute('SELECT player from Player where Type = "AR"')
	    playerList = cursorObj.fetchall()
	    for ele in playerList:
	        if ele[0] in list(final_data):
	    	    continue
	        self.player_list.addItem(ele[0])
	elif self.wicket_radio.isChecked():
            cursorObj.execute('SELECT player from Player where Type = "WK"')
	    playerList = cursorObj.fetchall()
	    for ele in playerList:
	        if ele[0] in list(final_data):
	    	    continue
	        self.player_list.addItem(ele[0])
	

    def add_player(self):
	player_name = self.player_list.takeItem(self.player_list.currentRow())
	cursorObj.execute("SELECT Points from Player where Player ='" + player_name.text() + "'")
	point = cursorObj.fetchall()
	point_text = int(self.points_used.text())
	point_avail = int(self.points_available.text())	
	flag = 1
	if self.batsmen_radio.isChecked():
	    if self.max_BAT is not 0:        
		self.max_BAT = self.max_BAT - 1    
		bat_cnt = self.batsmen_text.text()
		bat_cnt = int(bat_cnt) - 1
		self.batsmen_text.setText(str(bat_cnt))
	    else:
		flag = 0
		self.player_list.addItem(player_name)
  		msg = QMessageBox()
	        msg.setIcon(QMessageBox.Warning)
	        msg.setText("You cannot select more than 4 Batsmen")
        	msg.exec_()
	elif self.bowler_radio.isChecked():
	    if self.max_BWL is not 0:
		self.max_BWL = self.max_BWL - 1            
		bwl_cnt = self.bowler_text.text()
		bwl_cnt = int(bwl_cnt) - 1
		self.bowler_text.setText(str(bwl_cnt))
	    else:
		flag = 0
		self.player_list.addItem(player_name)
  		msg = QMessageBox()
	        msg.setIcon(QMessageBox.Warning)
	        msg.setText("You cannot select more than 4 Bowlers")
        	msg.exec_()
	elif self.rounders_radio.isChecked():
	    if self.max_AR is not 0:
		self.max_AR = self.max_AR - 1            
		rnd_cnt = self.rounders_text.text()
		rnd_cnt = int(rnd_cnt) - 1
		self.rounders_text.setText(str(rnd_cnt))
	    else:
		flag = 0
		self.player_list.addItem(player_name)
  		msg = QMessageBox()
	        msg.setIcon(QMessageBox.Warning)
	        msg.setText("You cannot select more than 3 All-Rounders")
        	msg.exec_()
	elif self.wicket_radio.isChecked():
	    if self.max_WK is not 0:
		self.max_WK = self.max_WK - 1            
		wk_cnt = self.wicket_text.text()
		wk_cnt = int(wk_cnt) - 1
		self.wicket_text.setText(str(wk_cnt))
	    else:
		flag = 0
		self.player_list.addItem(player_name)
  		msg = QMessageBox()
	        msg.setIcon(QMessageBox.Warning)
	        msg.setText("You cannot select more than 1 Wicket-Keeper")
        	msg.exec_()

	if flag:
	    self.final_list.addItem(player_name)
	    point_text = point_text + point[0][0]
	    self.points_used.setText(str(point_text))
	    point_avail = point_avail - point[0][0]
	    self.points_available.setText(str(point_avail))	    


    def remove_player(self):
	player_name = self.final_list.takeItem(self.final_list.currentRow())
	cursorObj.execute("SELECT Points from Player where Player = '" + player_name.text() + "'")
	point = cursorObj.fetchall()
	point_text = int(self.points_used.text())
	point_avail = int(self.points_available.text())	
	point_text = point_text - point[0][0]
	self.points_used.setText(str(point_text))
        point_avail = point_avail + point[0][0]
        self.points_available.setText(str(point_avail))
	
    def display_team(self):
        self.bowler_radio.setEnabled(False)
        self.batsmen_radio.setEnabled(False)
        self.rounders_radio.setEnabled(False)
        self.wicket_radio.setEnabled(False)
	team_name = self.open_obj.lineEdit.text()
	self.team_name_box.setText(team_name)
	cursorObj.execute("SELECT player, point from Team where team_name = '" +str(team_name) + "'")
	data = set(cursorObj.fetchall())
	self.player_list.clear()
	self.final_list.clear()	
	sum = 0
	for ele in data:
	    self.player_list.addItem(str(ele[0]))
	    self.final_list.addItem(str(ele[1]))
	    sum = sum + ele[1]
	self.points_used.setText(str(sum))
	self.points_available.setText('00')

	cursorObj.execute("SELECT player from Team where team_name = '" +str(team_name) + "'")
	player_data = set(cursorObj.fetchall())    
        cursorObj.execute('SELECT player from Player where Type = "BAT"')
	bat_list = cursorObj.fetchall()
	cursorObj.execute('SELECT player from Player where Type = "BWL"')
	bwl_list = cursorObj.fetchall()
	cursorObj.execute('SELECT player from Player where Type = "AR"')
	ar_list = cursorObj.fetchall()
	cursorObj.execute('SELECT player from Player where Type = "WK"')
	wk_list = cursorObj.fetchall()
	bat = 0
	bwl = 0
	wk = 0
	ar = 0
	for ele in player_data:
	    if ele in bat_list:
		bat = bat + 1
	    elif ele in bwl_list:
		bwl = bwl + 1
	    elif ele in ar_list:
		ar = ar + 1
	    elif ele in wk_list:
		wk = wk + 1
	self.batsmen_text.setText(str(bat))
	self.bowler_text.setText(str(bwl))
	self.rounders_text.setText(str(ar))
	self.wicket_text.setText(str(wk))
	

    def calc_score(self):
	self.calc_window = QtWidgets.QMainWindow()
	self.calc_obj = CalcScore()
	self.calc_obj.setupUi(self.calc_window)
	self.calc_window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bowler_label.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.bowler_text.setText(_translate("MainWindow", "##"))
        self.batsmen_label.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.batsmen_text.setText(_translate("MainWindow", "##"))
        self.rounders_label.setText(_translate("MainWindow", "Allrounders(AR)"))
        self.rounders_text.setText(_translate("MainWindow", "##"))
        self.wicket_label.setText(_translate("MainWindow", "Wicket-keeper(WK)"))
        self.wicket_text.setText(_translate("MainWindow", "##"))
        self.label.setText(_translate("MainWindow", "Your Selections :"))
        self.label_11.setText(_translate("MainWindow", "Points used"))
        self.points_used.setText(_translate("MainWindow", "##"))
        self.label_10.setText(_translate("MainWindow", "Points available"))
        self.points_available.setText(_translate("MainWindow", "##"))
        self.bowler_radio.setText(_translate("MainWindow", "BOW"))
        self.batsmen_radio.setText(_translate("MainWindow", "BAT"))
        self.rounders_radio.setText(_translate("MainWindow", "AR"))
        self.wicket_radio.setText(_translate("MainWindow", "WK"))
        self.team_name_label.setText(_translate("MainWindow", "Team Name :"))
        self.team_name_box.setText(_translate("MainWindow", "##"))
        self.MANAGETeams.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.action_NEW.setText(_translate("MainWindow", "NEW Team"))
        self.action_SAVE.setText(_translate("MainWindow", "SAVE Team"))
        self.action_OPEN.setText(_translate("MainWindow", "OPEN Team"))
        self.action_EVALUATE.setText(_translate("MainWindow", "EVALUATE Team"))
        self.NEW.setText(_translate("MainWindow", "NEW Team"))
        self.SAVE.setText(_translate("MainWindow", "SAVE Team"))
        self.OPEN.setText(_translate("MainWindow", "OPEN Team"))
        self.EVALUATE.setText(_translate("MainWindow", "EVALUATE Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

