#Импорт интерфейса
from AC import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep as sl
import mouse
import keyboard
import threading
import sys

#Основной класс
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Вызов функций
        self.init_ui_widnow()


    def init_ui_widnow(self):
  

        self.ui.start_button.clicked.connect(self.per)

    #Основной метод
    def run(self):
        while True:
            if keyboard.is_pressed(self.start):
                mouse.is_pressed(button = self.button)
                while True:
                    sl(self.time_delay)
                    mouse.double_click(button=self.button)
                    if keyboard.is_pressed(self.stop):
                        break

    def per(self):       
        #Сбор данных
        self.start = self.ui.startkey.text().lower()
        self.stop = self.ui.stopkey.text().lower()
        self.time_delay = float(self.ui.time_delay.text())
        self.button = self.ui.comboBox.currentText()
        #Запуск в отдельном потоке
        threading.Thread(target=self.run).start()


#Инцилизация интерфейса
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = Main()
    application.show()
    sys.exit(app.exec_())

