from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from currency_converter import CurrencyConverter
import math


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Curency Convertor")
        MainWindow.resize(484, 405)
        MainWindow.setStyleSheet("background-color: #302C2C")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 601, 141))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: #F36B6B\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.image = QtWidgets.QLabel(self.frame)
        self.image.setGeometry(QtCore.QRect(210, 0, 71, 81))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("C:/Icons/creative_commons_64px.png"))
        self.image.setObjectName("image")
        self.tittle = QtWidgets.QLabel(self.frame)
        self.tittle.setGeometry(QtCore.QRect(120, 70, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Orbitron SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tittle.setFont(font)
        self.tittle.setStyleSheet("color: white")
        self.tittle.setObjectName("tittle")
        self.inter = QtWidgets.QLineEdit(self.centralwidget)
        self.inter.setGeometry(QtCore.QRect(20, 180, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.inter.setFont(font)
        self.inter.setStyleSheet("QLineEdit {\n"
"    font-size: 12;\n"
"    color: white;\n"
"    border: 3px solid #F5651D;\n"
"    border-radius:50;\n"
"}")
        self.inter.setText("")
        self.inter.setObjectName("inter")
        self.arrow = QtWidgets.QLabel(self.centralwidget)
        self.arrow.setGeometry(QtCore.QRect(210, 190, 51, 61))
        self.arrow.setText("")
        self.arrow.setPixmap(QtGui.QPixmap("C:/Icons/right_48px.png"))
        self.arrow.setObjectName("arrow")
        self.inter_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.inter_2.setGeometry(QtCore.QRect(310, 180, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.inter_2.setFont(font)
        self.inter_2.setStyleSheet("QLineEdit {\n"
"    font-size: 12;\n"
"    color: white;\n"
"    border: 3px solid #F5651D;\n"
"    border-radius: 50px\n"
"}")
        self.inter_2.setText("")
        self.inter_2.setObjectName("inter_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 240, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    color: white;\n"
"    border: 3px solid #F5651D;\n"
"    border-radius:50;\n"
"}\n"
"QComboBox:hover {\n"
"    color: #F36B6B;\n"
"    border: 3px solid #F36B6B;\n"
"    border-radius:50;\n"
"\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 240, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    color: white;\n"
"    border: 3px solid #F5651D;\n"
"    border-radius:50;\n"
"}\n"
"QComboBox:hover {\n"
"    color: #F36B6B;\n"
"    border: 3px solid #F36B6B;\n"
"    border-radius:50;\n"
"\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 290, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Old Standard TT")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #F36B6B\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #F8FF16\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FF9027;\n"
"    color: #000000\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


#мои переменные и вызовы функций

        self.function()
        self.c = CurrencyConverter()
        self.init_ui_window()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tittle.setText(_translate("MainWindow", "Currency Converter"))
        self.comboBox.setItemText(0, _translate("MainWindow", "USD"))
        self.comboBox.setItemText(1, _translate("MainWindow", "EUR"))
        self.comboBox.setItemText(2, _translate("MainWindow", "RUB"))
        self.comboBox.setItemText(3, _translate("MainWindow", "BGN"))

        self.comboBox_2.setItemText(0, _translate("MainWindow", "USD"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "EUR"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "RUB"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "BGN"))

        self.pushButton.setText(_translate("MainWindow", "CONVERT"))



#мои функции 

    def init_ui_window(self):
        MainWindow.setWindowTitle('Currency Converter')
        MainWindow.setWindowIcon(QtGui.QIcon('icons8_currency_exchange'))
        MainWindow.setFixedSize(484, 405)

        self.inter.setPlaceholderText('From')
        self.inter_2.setPlaceholderText('To')



    def function(self):
        self.pushButton.clicked.connect(self.find_value)



    def find_value(self):
        first_value = self.comboBox.currentText()
        second_value = self.comboBox_2.currentText()
        numbers = float(self.inter.text())


        total = self.c.convert(numbers, first_value, second_value)
        total = round(total, 2)
        self.inter_2.setText(str(total))







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
