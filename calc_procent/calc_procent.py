from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 538)
        MainWindow.setStyleSheet("background-color: white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 891, 541))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.164179 rgba(144, 0, 255, 193), stop:0.542289 rgba(29, 85, 215, 206), stop:0.840796 rgba(68, 184, 255, 207))")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.first_group = QtWidgets.QFrame(self.frame)
        self.first_group.setGeometry(QtCore.QRect(330, 0, 441, 121))
        self.first_group.setStyleSheet("background-color: transparent")
        self.first_group.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.first_group.setFrameShadow(QtWidgets.QFrame.Raised)
        self.first_group.setObjectName("first_group")
        self.first_one = QtWidgets.QLineEdit(self.first_group)
        self.first_one.setGeometry(QtCore.QRect(10, 50, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.first_one.setFont(font)
        self.first_one.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.first_one.setText("")
        self.first_one.setAlignment(QtCore.Qt.AlignCenter)
        self.first_one.setObjectName("first_one")
        self.zap = QtWidgets.QLabel(self.first_group)
        self.zap.setGeometry(QtCore.QRect(130, 70, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(22)
        self.zap.setFont(font)
        self.zap.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.zap.setObjectName("zap")
        self.first_two = QtWidgets.QLineEdit(self.first_group)
        self.first_two.setGeometry(QtCore.QRect(150, 50, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.first_two.setFont(font)
        self.first_two.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.first_two.setText("")
        self.first_two.setAlignment(QtCore.Qt.AlignCenter)
        self.first_two.setObjectName("first_two")
        self.rav = QtWidgets.QLabel(self.first_group)
        self.rav.setGeometry(QtCore.QRect(280, 60, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(22)
        self.rav.setFont(font)
        self.rav.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.rav.setObjectName("rav")
        self.first_3 = QtWidgets.QLineEdit(self.first_group)
        self.first_3.setGeometry(QtCore.QRect(320, 50, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.first_3.setFont(font)
        self.first_3.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.first_3.setText("")
        self.first_3.setAlignment(QtCore.Qt.AlignCenter)
        self.first_3.setObjectName("first_3")
        self.first_procent = QtWidgets.QLabel(self.first_group)
        self.first_procent.setGeometry(QtCore.QRect(360, 10, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        self.first_procent.setFont(font)
        self.first_procent.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.first_procent.setObjectName("first_procent")
        self.first_num_2 = QtWidgets.QLabel(self.first_group)
        self.first_num_2.setGeometry(QtCore.QRect(180, 10, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        self.first_num_2.setFont(font)
        self.first_num_2.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.first_num_2.setObjectName("first_num_2")
        self.first_num_1 = QtWidgets.QLabel(self.first_group)
        self.first_num_1.setGeometry(QtCore.QRect(40, 10, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        self.first_num_1.setFont(font)
        self.first_num_1.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.first_num_1.setObjectName("first_num_1")
        self.labels_frame = QtWidgets.QFrame(self.frame)
        self.labels_frame.setGeometry(QtCore.QRect(0, 0, 331, 551))
        self.labels_frame.setStyleSheet("background-color: transparent")
        self.labels_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labels_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labels_frame.setObjectName("labels_frame")
        self.l_1 = QtWidgets.QLabel(self.labels_frame)
        self.l_1.setGeometry(QtCore.QRect(0, -20, 339, 151))
        font = QtGui.QFont()
        font.setFamily("Gagalin")
        font.setPointSize(20)
        self.l_1.setFont(font)
        self.l_1.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.l_1.setObjectName("l_1")
        self.l_6 = QtWidgets.QLabel(self.labels_frame)
        self.l_6.setGeometry(QtCore.QRect(10, 80, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(12)
        self.l_6.setFont(font)
        self.l_6.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.l_6.setObjectName("l_6")
        self.l_2 = QtWidgets.QLabel(self.labels_frame)
        self.l_2.setGeometry(QtCore.QRect(0, 161, 339, 71))
        font = QtGui.QFont()
        font.setFamily("Gagalin")
        font.setPointSize(20)
        self.l_2.setFont(font)
        self.l_2.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.l_2.setObjectName("l_2")
        self.l_5 = QtWidgets.QLabel(self.labels_frame)
        self.l_5.setGeometry(QtCore.QRect(46, 210, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(12)
        self.l_5.setFont(font)
        self.l_5.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.l_5.setObjectName("l_5")
        self.l_3 = QtWidgets.QLabel(self.labels_frame)
        self.l_3.setGeometry(QtCore.QRect(0, 282, 339, 81))
        font = QtGui.QFont()
        font.setFamily("Gagalin")
        font.setPointSize(20)
        self.l_3.setFont(font)
        self.l_3.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.l_3.setObjectName("l_3")
        self.l_7 = QtWidgets.QLabel(self.labels_frame)
        self.l_7.setGeometry(QtCore.QRect(60, 460, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(12)
        self.l_7.setFont(font)
        self.l_7.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.l_7.setObjectName("l_7")
        self.l_4 = QtWidgets.QLabel(self.labels_frame)
        self.l_4.setGeometry(QtCore.QRect(0, 390, 331, 101))
        font = QtGui.QFont()
        font.setFamily("Gagalin")
        font.setPointSize(20)
        self.l_4.setFont(font)
        self.l_4.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.l_4.setObjectName("l_4")
        self.l_8 = QtWidgets.QLabel(self.labels_frame)
        self.l_8.setGeometry(QtCore.QRect(50, 340, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(12)
        self.l_8.setFont(font)
        self.l_8.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.l_8.setObjectName("l_8")
        self.second_group = QtWidgets.QFrame(self.frame)
        self.second_group.setGeometry(QtCore.QRect(330, 130, 441, 121))
        self.second_group.setStyleSheet("background-color: transparent")
        self.second_group.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.second_group.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_group.setObjectName("second_group")
        self.second_3 = QtWidgets.QLineEdit(self.second_group)
        self.second_3.setGeometry(QtCore.QRect(320, 50, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.second_3.setFont(font)
        self.second_3.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.second_3.setText("")
        self.second_3.setAlignment(QtCore.Qt.AlignCenter)
        self.second_3.setObjectName("second_3")
        self.second_one = QtWidgets.QLineEdit(self.second_group)
        self.second_one.setGeometry(QtCore.QRect(10, 50, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.second_one.setFont(font)
        self.second_one.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.second_one.setText("")
        self.second_one.setAlignment(QtCore.Qt.AlignCenter)
        self.second_one.setObjectName("second_one")
        self.second_2 = QtWidgets.QLineEdit(self.second_group)
        self.second_2.setGeometry(QtCore.QRect(150, 50, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.second_2.setFont(font)
        self.second_2.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.second_2.setText("")
        self.second_2.setAlignment(QtCore.Qt.AlignCenter)
        self.second_2.setObjectName("second_2")
        self.rav_2 = QtWidgets.QLabel(self.second_group)
        self.rav_2.setGeometry(QtCore.QRect(280, 60, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(22)
        self.rav_2.setFont(font)
        self.rav_2.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.rav_2.setObjectName("rav_2")
        self.first_procent_2 = QtWidgets.QLabel(self.second_group)
        self.first_procent_2.setGeometry(QtCore.QRect(350, 10, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        self.first_procent_2.setFont(font)
        self.first_procent_2.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.first_procent_2.setObjectName("first_procent_2")
        self.zap_2 = QtWidgets.QLabel(self.second_group)
        self.zap_2.setGeometry(QtCore.QRect(130, 70, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(22)
        self.zap_2.setFont(font)
        self.zap_2.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.zap_2.setObjectName("zap_2")
        self.first_num_3 = QtWidgets.QLabel(self.second_group)
        self.first_num_3.setGeometry(QtCore.QRect(50, 10, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        self.first_num_3.setFont(font)
        self.first_num_3.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.first_num_3.setObjectName("first_num_3")
        self.first_num_4 = QtWidgets.QLabel(self.second_group)
        self.first_num_4.setGeometry(QtCore.QRect(180, 10, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        self.first_num_4.setFont(font)
        self.first_num_4.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.first_num_4.setObjectName("first_num_4")
        self.threed_group = QtWidgets.QFrame(self.frame)
        self.threed_group.setGeometry(QtCore.QRect(330, 250, 441, 121))
        self.threed_group.setStyleSheet("background-color: transparent")
        self.threed_group.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.threed_group.setFrameShadow(QtWidgets.QFrame.Raised)
        self.threed_group.setObjectName("threed_group")
        self.threed_3 = QtWidgets.QLineEdit(self.threed_group)
        self.threed_3.setGeometry(QtCore.QRect(320, 50, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.threed_3.setFont(font)
        self.threed_3.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.threed_3.setText("")
        self.threed_3.setAlignment(QtCore.Qt.AlignCenter)
        self.threed_3.setObjectName("threed_3")
        self.threed_one = QtWidgets.QLineEdit(self.threed_group)
        self.threed_one.setGeometry(QtCore.QRect(10, 50, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.threed_one.setFont(font)
        self.threed_one.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.threed_one.setText("")
        self.threed_one.setAlignment(QtCore.Qt.AlignCenter)
        self.threed_one.setObjectName("threed_one")
        self.threed_2 = QtWidgets.QLineEdit(self.threed_group)
        self.threed_2.setGeometry(QtCore.QRect(160, 50, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.threed_2.setFont(font)
        self.threed_2.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.threed_2.setText("")
        self.threed_2.setAlignment(QtCore.Qt.AlignCenter)
        self.threed_2.setObjectName("threed_2")
        self.rav_3 = QtWidgets.QLabel(self.threed_group)
        self.rav_3.setGeometry(QtCore.QRect(280, 60, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(22)
        self.rav_3.setFont(font)
        self.rav_3.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.rav_3.setObjectName("rav_3")
        self.first_procent_3 = QtWidgets.QLabel(self.threed_group)
        self.first_procent_3.setGeometry(QtCore.QRect(350, 10, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        self.first_procent_3.setFont(font)
        self.first_procent_3.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.first_procent_3.setObjectName("first_procent_3")
        self.plus = QtWidgets.QLabel(self.threed_group)
        self.plus.setGeometry(QtCore.QRect(130, 60, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(22)
        self.plus.setFont(font)
        self.plus.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.plus.setObjectName("plus")
        self.first_num_5 = QtWidgets.QLabel(self.threed_group)
        self.first_num_5.setGeometry(QtCore.QRect(40, 10, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        self.first_num_5.setFont(font)
        self.first_num_5.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.first_num_5.setObjectName("first_num_5")
        self.first_num_6 = QtWidgets.QLabel(self.threed_group)
        self.first_num_6.setGeometry(QtCore.QRect(200, 10, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        self.first_num_6.setFont(font)
        self.first_num_6.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.first_num_6.setObjectName("first_num_6")
        self.forth_group = QtWidgets.QFrame(self.frame)
        self.forth_group.setGeometry(QtCore.QRect(330, 380, 441, 121))
        self.forth_group.setStyleSheet("background-color: transparent")
        self.forth_group.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.forth_group.setFrameShadow(QtWidgets.QFrame.Raised)
        self.forth_group.setObjectName("forth_group")
        self.fourth_3 = QtWidgets.QLineEdit(self.forth_group)
        self.fourth_3.setGeometry(QtCore.QRect(320, 50, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fourth_3.setFont(font)
        self.fourth_3.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.fourth_3.setText("")
        self.fourth_3.setAlignment(QtCore.Qt.AlignCenter)
        self.fourth_3.setObjectName("fourth_3")
        self.fourth_one = QtWidgets.QLineEdit(self.forth_group)
        self.fourth_one.setGeometry(QtCore.QRect(10, 50, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fourth_one.setFont(font)
        self.fourth_one.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.fourth_one.setText("")
        self.fourth_one.setAlignment(QtCore.Qt.AlignCenter)
        self.fourth_one.setObjectName("fourth_one")
        self.fourth_2 = QtWidgets.QLineEdit(self.forth_group)
        self.fourth_2.setGeometry(QtCore.QRect(160, 50, 113, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fourth_2.setFont(font)
        self.fourth_2.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.fourth_2.setText("")
        self.fourth_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fourth_2.setObjectName("fourth_2")
        self.rav_5 = QtWidgets.QLabel(self.forth_group)
        self.rav_5.setGeometry(QtCore.QRect(280, 60, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(22)
        self.rav_5.setFont(font)
        self.rav_5.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.rav_5.setObjectName("rav_5")
        self.first_procent_5 = QtWidgets.QLabel(self.forth_group)
        self.first_procent_5.setGeometry(QtCore.QRect(350, 10, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        self.first_procent_5.setFont(font)
        self.first_procent_5.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.first_procent_5.setObjectName("first_procent_5")
        self.minus = QtWidgets.QLabel(self.forth_group)
        self.minus.setGeometry(QtCore.QRect(130, 60, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(22)
        self.minus.setFont(font)
        self.minus.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.minus.setObjectName("minus")
        self.first_num_9 = QtWidgets.QLabel(self.forth_group)
        self.first_num_9.setGeometry(QtCore.QRect(40, 10, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        self.first_num_9.setFont(font)
        self.first_num_9.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.first_num_9.setObjectName("first_num_9")
        self.first_num_10 = QtWidgets.QLabel(self.forth_group)
        self.first_num_10.setGeometry(QtCore.QRect(200, 10, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        self.first_num_10.setFont(font)
        self.first_num_10.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"")
        self.first_num_10.setObjectName("first_num_10")
        self.b_1 = QtWidgets.QPushButton(self.frame)
        self.b_1.setGeometry(QtCore.QRect(790, 40, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(36)
        self.b_1.setFont(font)
        self.b_1.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 170, 255);\n"
"    border: 3px solid rgb(0, 255, 255);\n"
"    border-radius: 15px;\n"
"    color: rgb(0, 255, 255)\n"
"}\n"
"QPushButton::hover {\n"
"    color: rgb(255, 170, 255);\n"
"    border-color: rgb(255, 170, 255);\n"
"}\n"
"QPushButton::pressed {\n"
"    color: rgb(171, 62, 255);\n"
"    border-color: rgb(171, 62, 255);\n"
"}\n"
"")
        self.b_1.setObjectName("b_1")
        self.b_2 = QtWidgets.QPushButton(self.frame)
        self.b_2.setGeometry(QtCore.QRect(790, 170, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(36)
        self.b_2.setFont(font)
        self.b_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 170, 255);\n"
"    border: 3px solid rgb(0, 255, 255);\n"
"    border-radius: 15px;\n"
"    color: rgb(0, 255, 255)\n"
"}\n"
"QPushButton::hover {\n"
"    color: rgb(255, 170, 255);\n"
"    border-color: rgb(255, 170, 255);\n"
"}\n"
"QPushButton::pressed {\n"
"    color: rgb(171, 62, 255);\n"
"    border-color: rgb(171, 62, 255);\n"
"}\n"
"")
        self.b_2.setObjectName("b_2")
        self.b_3 = QtWidgets.QPushButton(self.frame)
        self.b_3.setGeometry(QtCore.QRect(790, 290, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(36)
        self.b_3.setFont(font)
        self.b_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 170, 255);\n"
"    border: 3px solid rgb(0, 255, 255);\n"
"    border-radius: 15px;\n"
"    color: rgb(0, 255, 255)\n"
"}\n"
"QPushButton::hover {\n"
"    color: rgb(255, 170, 255);\n"
"    border-color: rgb(255, 170, 255);\n"
"}\n"
"QPushButton::pressed {\n"
"    color: rgb(171, 62, 255);\n"
"    border-color: rgb(171, 62, 255);\n"
"}\n"
"")
        self.b_3.setObjectName("b_3")
        self.b_4 = QtWidgets.QPushButton(self.frame)
        self.b_4.setGeometry(QtCore.QRect(790, 420, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(36)
        self.b_4.setFont(font)
        self.b_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 170, 255);\n"
"    border: 3px solid rgb(0, 255, 255);\n"
"    border-radius: 15px;\n"
"    color: rgb(0, 255, 255)\n"
"}\n"
"QPushButton::hover {\n"
"    color: rgb(255, 170, 255);\n"
"    border-color: rgb(255, 170, 255);\n"
"}\n"
"QPushButton::pressed {\n"
"    color: rgb(171, 62, 255);\n"
"    border-color: rgb(171, 62, 255);\n"
"}\n"
"")
        self.b_4.setObjectName("b_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.design()
        self.main_function()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.zap.setText(_translate("MainWindow", ","))
        self.rav.setText(_translate("MainWindow", "="))
        self.first_procent.setText(_translate("MainWindow", "%"))
        self.first_num_2.setText(_translate("MainWindow", "num"))
        self.first_num_1.setText(_translate("MainWindow", "num"))
        self.l_1.setText(_translate("MainWindow", "Проценты от чисел"))
        self.l_6.setText(_translate("MainWindow", "Число 20 от числа 75 = 26.66%"))
        self.l_2.setText(_translate("MainWindow", "Число от процентов"))
        self.l_5.setText(_translate("MainWindow", "5% от числа 4000 = 200"))
        self.l_3.setText(_translate("MainWindow", "прибавить проценты"))
        self.l_7.setText(_translate("MainWindow", "1000 - 20% = 800"))
        self.l_4.setText(_translate("MainWindow", "вычесть проценты"))
        self.l_8.setText(_translate("MainWindow", "1000 + 20% = 1200"))
        self.rav_2.setText(_translate("MainWindow", "="))
        self.first_procent_2.setText(_translate("MainWindow", "num"))
        self.zap_2.setText(_translate("MainWindow", ","))
        self.first_num_3.setText(_translate("MainWindow", "%"))
        self.first_num_4.setText(_translate("MainWindow", "num"))
        self.rav_3.setText(_translate("MainWindow", "="))
        self.first_procent_3.setText(_translate("MainWindow", "num"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.first_num_5.setText(_translate("MainWindow", "num"))
        self.first_num_6.setText(_translate("MainWindow", "%"))
        self.rav_5.setText(_translate("MainWindow", "="))
        self.first_procent_5.setText(_translate("MainWindow", "num"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.first_num_9.setText(_translate("MainWindow", "num"))
        self.first_num_10.setText(_translate("MainWindow", "%"))
        self.b_1.setText(_translate("MainWindow", "P"))
        self.b_2.setText(_translate("MainWindow", "P"))
        self.b_3.setText(_translate("MainWindow", "P"))
        self.b_4.setText(_translate("MainWindow", "P"))

    def main_function(self):
        self.b_1.clicked.connect(self.first_function)
        self.b_2.clicked.connect(self.second_function)
        self.b_3.clicked.connect(self.third_function)
        self.b_4.clicked.connect(self.fourth_function)

    def is_float(self, n1, n2):
        try: 
            float(n1), float(n2)
            return True
        except:
            return False

           

    def first_function(self):
        n1 = self.first_one.text()
        n2 = self.first_two.text()

        if self.is_float(n1, n2) == False:
            fall = QMessageBox()
            
            fall.setWindowTitle('Error')
            fall.setText('Введено неккоректное значение')
            fall.setStandardButtons(QMessageBox.Ok)
            fall.setWindowIcon(QIcon('error.ico'))

            fall.exec_()
        else:
            n1, n2 = float(n1), float(n2)

            total = n2 / 100
            total = n1 / total
            total = str(total)
            self.first_3.setText('')
            self.first_3.setText(total[0:total.index('.') + 3])

    def second_function(self):
        n1 = self.second_one.text()
        n2 = self.second_2.text()

        if self.is_float(n1, n2) == False:
            fall = QMessageBox()
            
            fall.setWindowTitle('Error')
            fall.setText('Введено неккоректное значение')
            fall.setStandardButtons(QMessageBox.Ok)
            fall.setWindowIcon(QIcon('error.ico'))

            fall.exec_()
        else:
            n1, n2 = float(n1), float(n2)

            total = n2 / 100 
            total *= n1
            total = str(total)
            self.second_3.setText('')
            self.second_3.setText(total[0:total.index('.') + 3])

    def third_function(self):
        n1 = self.threed_one.text()
        n2 = self.threed_2.text()

        if self.is_float(n1, n2) == False:
            fall = QMessageBox()
            
            fall.setWindowTitle('Error')
            fall.setText('Введено неккоректное значение')
            fall.setStandardButtons(QMessageBox.Ok)
            fall.setWindowIcon(QIcon('error.ico'))

            fall.exec_()
        else:
            n1, n2 = float(n1), float(n2)

            total = n1 / 100
            total = n1 + n2 * total
            total = str(total)
            self.threed_3.setText('')
            self.threed_3.setText(total[0:total.index('.') + 3])

    def fourth_function(self):
        n1 = self.fourth_one.text()
        n2 = self.fourth_2.text()

        if self.is_float(n1, n2) == False:
            fall = QMessageBox()
            
            fall.setWindowTitle('Error')
            fall.setText('Введено неккоректное значение')
            fall.setStandardButtons(QMessageBox.Ok)
            fall.setWindowIcon(QIcon('error.ico'))

            fall.exec_()
        else:
            n1, n2 = float(n1), float(n2)

            total = n1 / 100
            total = n1 - n2 * total
            total = str(total)
            self.fourth_3.setText('')
            self.fourth_3.setText(total[0:total.index('.') + 3])

    def design(self):
        MainWindow.setWindowTitle('Calculator precent')
        MainWindow.setFixedSize(891, 538)
        MainWindow.setWindowIcon(QIcon('precent.ico'))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())