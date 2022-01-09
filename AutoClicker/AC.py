
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow():



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 436, 503))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x2:1, y1:0.568, x4:3, y2:0.539773, stop:0.4 #43e97b, stop:0.99 #38f9d7)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.start_button = QtWidgets.QPushButton(self.frame)
        self.start_button.setGeometry(QtCore.QRect(130, 320, 121, 101))
        font = QtGui.QFont()
        font.setFamily("Amputa Bangiz")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("QPushButton {\n"
"    color: rgb(2, 134, 13);\n"
"    background-color: #d4fc79;\n"
"    border: 5px solid #96e6a1;\n"
"    border-radius: 50px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(255, 170, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 175, 0);\n"
"    color: red;\n"
"    border-color: rgb(0, 61, 0)\n"
"}")
        self.start_button.setObjectName("start_button")
        self.bykematin = QtWidgets.QLabel(self.frame)
        self.bykematin.setGeometry(QtCore.QRect(130, 415, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Minster No 4")
        font.setPointSize(26)
        self.bykematin.setFont(font)
        self.bykematin.setStyleSheet("background-color: transparent;\n"
"color: grey")
        self.bykematin.setObjectName("bykematin")
        self.labelstart = QtWidgets.QLabel(self.frame)
        self.labelstart.setGeometry(QtCore.QRect(40, 30, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Nunito SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelstart.setFont(font)
        self.labelstart.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    color: rgb(2, 112, 108)\n"
"}")
        self.labelstart.setObjectName("labelstart")
        self.labelstop = QtWidgets.QLabel(self.frame)
        self.labelstop.setGeometry(QtCore.QRect(40, 100, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Nunito SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelstop.setFont(font)
        self.labelstop.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    color: rgb(2, 112, 108)\n"
"}")
        self.labelstop.setObjectName("labelstop")
        self.Image = QtWidgets.QLabel(self.frame)
        self.Image.setGeometry(QtCore.QRect(220, 30, 31, 61))
        self.Image.setStyleSheet("background-color: transparent\n"
"")
        self.Image.setText("")
        self.Image.setPixmap(QtGui.QPixmap("C:/Icons/arrow_24px.png"))
        self.Image.setObjectName("Image")
        self.Image2 = QtWidgets.QLabel(self.frame)
        self.Image2.setGeometry(QtCore.QRect(220, 100, 31, 61))
        self.Image2.setStyleSheet("background-color: transparent\n"
"")
        self.Image2.setText("")
        self.Image2.setPixmap(QtGui.QPixmap("C:/Icons/arrow_24px.png"))
        self.Image2.setObjectName("Image2")
        self.startkey = QtWidgets.QLineEdit(self.frame)
        self.startkey.setGeometry(QtCore.QRect(270, 40, 113, 41))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.startkey.setFont(font)
        self.startkey.setAutoFillBackground(False)
        self.startkey.setStyleSheet("QLineEdit {\n"
"    border: 5px solid rgb(0, 170, 0);\n"
"    border-radius: 14px;\n"
"    color: grey;\n"
"}")
        self.startkey.setText("")
        self.startkey.setObjectName("startkey")
        self.stopkey = QtWidgets.QLineEdit(self.frame)
        self.stopkey.setGeometry(QtCore.QRect(270, 110, 113, 41))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.stopkey.setFont(font)
        self.stopkey.setAutoFillBackground(False)
        self.stopkey.setStyleSheet("QLineEdit {\n"
"    border: 5px solid rgb(0, 170, 0);\n"
"    border-radius: 14px;\n"
"    color: grey;\n"
"}")
        self.stopkey.setText("")
        self.stopkey.setObjectName("stopkey")
        self.labelstop_2 = QtWidgets.QLabel(self.frame)
        self.labelstop_2.setGeometry(QtCore.QRect(30, 170, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Nunito SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelstop_2.setFont(font)
        self.labelstop_2.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    color: rgb(2, 112, 108)\n"
"}")
        self.labelstop_2.setObjectName("labelstop_2")
        self.Image2_2 = QtWidgets.QLabel(self.frame)
        self.Image2_2.setGeometry(QtCore.QRect(220, 170, 31, 61))
        self.Image2_2.setStyleSheet("background-color: transparent\n"
"")
        self.Image2_2.setText("")
        self.Image2_2.setPixmap(QtGui.QPixmap("C:/Icons/arrow_24px.png"))
        self.Image2_2.setObjectName("Image2_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(270, 180, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Nunito SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 5px solid rgb(0, 170, 0);\n"
"    border-radius: 14px;\n"
"    color: grey;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_time_delay = QtWidgets.QLabel(self.frame)
        self.label_time_delay.setGeometry(40, 240, 161, 51)
        self.label_time_delay.setText('Time Delay')
        font = QtGui.QFont()
        font.setFamily('Nunito SemiBold')
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        self.label_time_delay.setFont(font)

        self.label_time_delay.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    color: rgb(2, 112, 108)\n"
"}")

        self.Image2_3 = QtWidgets.QLabel(self.frame)
        self.Image2_3.setGeometry(QtCore.QRect(220, 240, 31, 61))
        self.Image2_3.setStyleSheet("background-color: transparent\n"
"")
        self.Image2_3.setText("")
        self.Image2_3.setPixmap(QtGui.QPixmap("C:/Icons/arrow_24px.png"))
        self.Image2_3.setObjectName("Image2_2")


        self.time_delay = QtWidgets.QLineEdit(self.frame)
        self.time_delay.setGeometry(270, 250, 111, 41)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setFamily('Nunito SemiBold')

        self.time_delay.setFont(font)
        self.time_delay.setStyleSheet("QLineEdit {\n"
"    border: 5px solid rgb(0, 170, 0);\n"
"    border-radius: 14px;\n"
"    color: grey;\n"
"}")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

     

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.bykematin.setText(_translate("MainWindow", "by kematin"))
        self.labelstart.setText(_translate("MainWindow", "Start button "))
        self.labelstop.setText(_translate("MainWindow", "Stop button "))
        self.labelstop_2.setText(_translate("MainWindow", "Clicker button "))
        self.comboBox.setItemText(0, _translate("MainWindow", "left"))
        self.comboBox.setItemText(1, _translate("MainWindow", "right"))
        self.comboBox.setItemText(2, _translate("MainWindow", "top"))

        self.startkey.setAlignment(QtCore.Qt.AlignCenter)
        self.stopkey.setAlignment(QtCore.Qt.AlignCenter)
        self.comboBox.setEditable(True)
        self.comboBox.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.time_delay.setAlignment(QtCore.Qt.AlignCenter)

    

        
       