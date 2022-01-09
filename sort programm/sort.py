from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication
from PyQt5.QtGui import QIcon
import watchdog
from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler
import sys
import threading
import shutil

class Ui_MainWindow(FileSystemEventHandler):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1151, 671))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.653409, x2:0, y2:0.267, stop:0.233831  #fdfbfb, stop:0.616915 #ebedee);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_sort = QtWidgets.QLabel(self.frame)
        self.label_sort.setGeometry(QtCore.QRect(290, 10, 451, 51))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_sort.setFont(font)
        self.label_sort.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    color: grey\n"
"}")
        self.label_sort.setObjectName("label_sort")
        self.all_files = QtWidgets.QCheckBox(self.frame)
        self.all_files.setGeometry(QtCore.QRect(40, 110, 221, 51))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.all_files.setFont(font)
        self.all_files.setStyleSheet("QCheckBox {\n"
"    background-color: transparent;\n"
"    color: grey\n"
"}")
        self.all_files.setObjectName("all_files")
        self.image = QtWidgets.QCheckBox(self.frame)
        self.image.setGeometry(QtCore.QRect(340, 110, 171, 51))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.image.setFont(font)
        self.image.setStyleSheet("QCheckBox {\n"
"    background-color: transparent;\n"
"    color: grey\n"
"}")
        self.image.setObjectName("image")
        self.video = QtWidgets.QCheckBox(self.frame)
        self.video.setGeometry(QtCore.QRect(570, 110, 111, 51))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.video.setFont(font)
        self.video.setStyleSheet("QCheckBox {\n"
"    background-color: transparent;\n"
"    color: grey\n"
"}")
        self.video.setObjectName("video")
        self.txt = QtWidgets.QCheckBox(self.frame)
        self.txt.setGeometry(QtCore.QRect(40, 200, 281, 51))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.txt.setFont(font)
        self.txt.setStyleSheet("QCheckBox {\n"
"    background-color: transparent;\n"
"    color: grey\n"
"}")
        self.txt.setObjectName("txt")
        self.files_exe = QtWidgets.QCheckBox(self.frame)
        self.files_exe.setGeometry(QtCore.QRect(340, 200, 171, 51))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.files_exe.setFont(font)
        self.files_exe.setStyleSheet("QCheckBox {\n"
"    background-color: transparent;\n"
"    color: grey\n"
"}")
        self.files_exe.setObjectName("files_exe")
        self.rar = QtWidgets.QCheckBox(self.frame)
        self.rar.setGeometry(QtCore.QRect(570, 200, 121, 51))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.rar.setFont(font)
        self.rar.setStyleSheet("QCheckBox {\n"
"    background-color: transparent;\n"
"    color: grey\n"
"}")
        self.rar.setObjectName("rar")
        self.checkBox_9 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_9.setGeometry(QtCore.QRect(740, 200, 211, 51))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setStyleSheet("QCheckBox {\n"
"    background-color: transparent;\n"
"    color: grey\n"
"}")
        self.checkBox_9.setObjectName("checkBox_9")
        self.audio = QtWidgets.QCheckBox(self.frame)
        self.audio.setGeometry(QtCore.QRect(740, 110, 111, 51))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.audio.setFont(font)
        self.audio.setStyleSheet("QCheckBox {\n"
"    background-color: transparent;\n"
"    color: grey\n"
"}")
        self.audio.setObjectName("audio")
        self.label_folder = QtWidgets.QLabel(self.frame)
        self.label_folder.setGeometry(QtCore.QRect(40, 300, 570, 51))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_folder.setFont(font)
        self.label_folder.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    color: grey\n"
"}")
        self.label_folder.setObjectName("label_folder")
        self.label_folder_out = QtWidgets.QLabel(self.frame)
        self.label_folder_out.setGeometry(QtCore.QRect(40, 440, 650, 70))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_folder_out.setFont(font)
        self.label_folder_out.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    color: grey\n"
"}")
        self.label_folder_out.setObjectName("label_folder_out")
        self.input_folder = QtWidgets.QLineEdit(self.frame)
        self.input_folder.setGeometry(QtCore.QRect(40, 380, 571, 41))
        self.input_folder.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(222, 222, 222);\n"
"    border: 1px solid rgb(222, 222, 222);\n"
"    border-radius: 10px;\n"
"    color: grey\n"
"}")
        self.input_folder.setObjectName("input_folder")
        self.output_folder = QtWidgets.QLineEdit(self.frame)
        self.output_folder.setGeometry(QtCore.QRect(40, 540, 571, 41))
        self.output_folder.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(222, 222, 222);\n"
"    border: 1px solid rgb(222, 222, 222);\n"
"    border-radius: 10px;\n"
"    color: grey\n"
"}")
        self.output_folder.setObjectName("output_folder")
        self.bt_of_input = QtWidgets.QPushButton(self.frame)
        self.bt_of_input.setGeometry(QtCore.QRect(560, 390, 51, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_of_input.setFont(font)
        self.bt_of_input.setStyleSheet("background-color: transparent")
        self.bt_of_input.setObjectName("bt_of_input")
        self.bt_of_output = QtWidgets.QPushButton(self.frame)
        self.bt_of_output.setGeometry(QtCore.QRect(560, 550, 51, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_of_output.setFont(font)
        self.bt_of_output.setStyleSheet("background-color: transparent")
        self.bt_of_output.setObjectName("bt_of_output")
        self.start = QtWidgets.QPushButton(self.frame)
        self.start.setGeometry(QtCore.QRect(740, 310, 241, 271))
        font = QtGui.QFont()
        font.setFamily("a_AlternaSw")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet("QPushButton {\n"
"    background-color: rgb(222, 222, 222);\n"
"    border: 1px solid rgb(222, 222, 222);\n"
"    border-radius: 35px;\n"
"    color: grey\n"
"}\n"
"QPushButton:hover {\n"
"    color: black\n"
"}\n"
"QPushButton:pressed {\n"
"    color: white;\n"
"    background-color: rgb(108, 108, 108)\n"
"}")
        self.start.setObjectName("start")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.init_ui()
        self.main_functions()
        threading.Thread(target=self.check).start()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_sort.setText(_translate("MainWindow", "Выбери тип файлов для сортировки"))
        self.all_files.setText(_translate("MainWindow", "Все виды файлов"))
        self.image.setText(_translate("MainWindow", "Фотографии"))
        self.video.setText(_translate("MainWindow", "Видео"))
        self.txt.setText(_translate("MainWindow", "Текстовые документы"))
        self.files_exe.setText(_translate("MainWindow", "Приложения"))
        self.rar.setText(_translate("MainWindow", "Архивы"))
        self.checkBox_9.setText(_translate("MainWindow", "Файлы расчётов"))
        self.audio.setText(_translate("MainWindow", "Аудио"))
        self.label_folder.setText(_translate("MainWindow", "Выбери папку которую хочешь отсартировать"))
        self.label_folder_out.setText(_translate("MainWindow", "Выбери в какую папку будут сохраняться файлы\n(В ней автомотически создаться папка программы)"))
        self.bt_of_input.setText(_translate("MainWindow", "..."))
        self.bt_of_output.setText(_translate("MainWindow", "..."))
        self.start.setText(_translate("MainWindow", "Start"))


#DISIGN
    def init_ui(self):
        MainWindow.setWindowTitle('Clever sort')
        MainWindow.setFixedSize(1024, 654)
        MainWindow.setWindowIcon(QIcon('C:/Icons/sort.ico'))

#Check boxes
    def check(self):
        while True:  
            if self.all_files.isChecked():
                self.rar.setChecked(False)
                self.files_exe.setChecked(False)
                self.checkBox_9.setChecked(False)
                self.audio.setChecked(False)
                self.video.setChecked(False)
                self.image.setChecked(False)
                self.txt.setChecked(False)

            else:
                if self.image.isChecked():
                    self.all_files.setChecked(False)

                elif self.video.isChecked():
                    self.all_files.setChecked(False)

                elif self.audio.isChecked():
                    self.all_files.setChecked(False)

                elif self.checkBox_9.isChecked():
                    self.all_files.setChecked(False)

                elif self.txt.isChecked():
                    self.all_files.setChecked(False)

                elif self.files_exe.isChecked():
                    self.all_files.setChecked(False)

                elif self.rar.isChecked():
                    self.all_files.setChecked(False)

                else:
                    continue 


#Function location
    def function_input_folder(self):
        location = QFileDialog()
        self.input_folder.setText(location.getExistingDirectory())



    def function_output_folder(self):
        location = QFileDialog
        self.output_folder.setText(location.getExistingDirectory())


#Main function
    def sort(self):
        threading.Thread(target=self.quick_sort).start()


    def quick_sort(self):
        if os.path.exists(self.input_folder.text()) == True and os.path.exists(self.output_folder.text()) == True:
            self.location_of_input = self.input_folder.text()
            self.location_of_output = self.output_folder.text()
        else:
            error = QMessageBox()

            error.setText('Выбранного каталогая не существует')
            error.setWindowTitle('Ошибка')
            error.setStandardButtons(QMessageBox.Ok)
            error.setWindowIcon(QIcon('sort.png'))

            error.exec_()


        if os.path.exists(self.location_of_output + '/Sort') == False:
            os.mkdir(self.location_of_output + '/Sort')
            os.mkdir(self.location_of_output + '/Sort' + '/Изображения')
            os.mkdir(self.location_of_output + '/Sort' + '/Аудио')
            os.mkdir(self.location_of_output + '/Sort' + '/Видео')
            os.mkdir(self.location_of_output + '/Sort' + '/Тексты')
            os.mkdir(self.location_of_output + '/Sort' + '/Приложения')
            os.mkdir(self.location_of_output + '/Sort' + '/Архивы')
            os.mkdir(self.location_of_output + '/Sort' + '/Файлы расчётов')



        image = ['png', 'jpg', 'svg', 'ico', 'webp', 'bmp', 'gif', 'jpeg', 'psd', 'tiff', 'ai']
        video = ['mp4', 'avi', 'webm', 'mpg', 'mpeg']
        audio = ['mp3', 'amr']
        txt = ['txt', 'docx', 'csv']
        app = ['exe', 'apk']
        zip_rar = ['zip', 'rar', 'iso', '7z']
        calculation = ['html', 'py', 'xls', 'pdf']



        for fl in os.listdir(self.location_of_input):
            ex = fl.split('.')
            if self.all_files.isChecked():
                if len(ex) > 1 and ex[1].lower() in image:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Изображения/" + fl
                    shutil.move(file, new_path)

                elif len(ex) > 1 and ex[1].lower() in video:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Видео/" + fl
                    shutil.move(file, new_path)

                elif len(ex) > 1 and ex[1].lower() in audio:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Аудио/" + fl
                    shutil.move(file, new_path)
        
                elif len(ex) > 1 and ex[1].lower() in txt:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Тексты/" + fl
                    shutil.move(file, new_path)

                elif len(ex) > 1 and ex[1].lower() in app:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Приложения/" + fl
                    shutil.move(file, new_path)

                elif len(ex) > 1 and ex[1].lower() in zip_rar:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Архивы/" + fl
                    shutil.move(file, new_path)  

                elif len(ex) > 1 and ex[1].lower() in calculation:
                    file = self.location_of_input + "/" + fl
                    new_path = self.location_of_output + '/Sort' + "/Файлы расчётов/" + fl
                    shutil.move(file, new_path)


            else:
                for_sort = []
                if self.image.isChecked():
                    for_sort.append('image')

                if self.audio.isChecked():
                    for_sort.append('audio')

                if self.video.isChecked():
                    for_sort.append('video')

                if self.txt.isChecked():
                    for_sort.append('txt')

                if self.rar.isChecked():
                    for_sort.append('rar')

                if self.files_exe.isChecked():
                    for_sort.append('files_exe')

                if self.checkBox_9.isChecked():
                    for_sort.append('checkBox_9')


                
                if len(for_sort) < 1:
                    error = QMessageBox()

                    error.setText('Не был выбран ни один тип файлов')
                    error.setWindowTitle('Ошибка')
                    error.setStandardButtons(QMessageBox.Ok)
                    error.setWindowIcon(QIcon('C:/Icons/error.ico'))

                    error.exec_()
                    break

                else:
                    for type_ in for_sort:
                        if type_ == 'image':
                            if len(ex) > 1 and ex[1].lower() in image:
                                file = self.location_of_input + "/" + fl
                                new_path = self.location_of_output + '/Sort' + "/Изображения/" + fl
                                shutil.move(file, new_path)
                        elif type_ == 'video':
                            if len(ex) > 1 and ex[1].lower() in video:
                                file = self.location_of_input + '/' + file
                                new_path = self.location_of_output + '/Sort' + '/Видео/' + fl
                                shutil.move(file, new_path)

                        elif type_ == 'audio':
                            if len(ex) > 1 and ex[1].lower() in audio:
                                file = self.location_of_input + '/' + file
                                new_path = self.location_of_output + '/Sort' + '/Аудио/' + fl
                                shutil.move(file, new_path) 

                        elif type_ == 'zip_rar':
                            if len(ex) > 1 and ex[1].lower() in zip_rar:
                                file = self.location_of_input + '/' + file
                                new_path = self.location_of_output + '/Sort' + '/Архивы/' + fl
                                shutil.move(file, new_path)
                                     
                        elif type_ == 'app':
                            if len(ex) > 1 and ex[1].lower() in app:
                                file = self.location_of_input + '/' + file
                                new_path = self.location_of_output + '/Sort' + '/Приложения/' + fl
                                shutil.move(file, new_path) 

                        elif type_ == 'calculation':
                            if len(ex) > 1 and ex[1].lower() in calculation:
                                file = self.location_of_input + '/' + file
                                new_path = self.location_of_output + '/Sort' + '/Файлы расчётов/' + fl
                                shutil.move(file, new_path)
                                     
                        elif type_ == 'txt':
                            if len(ex) > 1 and ex[1].lower() in txt:
                                file = self.location_of_input + '/' + file
                                new_path = self.location_of_output + '/Sort' + '/Тексты/' + fl
                                shutil.move(file, new_path)


        done = QMessageBox()

        done.setText('Сортировка окончена')
        done.setWindowTitle('Конец')
        done.setStandardButtons(QMessageBox.Ok)
        done.setWindowIcon(QIcon('C:/Icons/done.ico'))

        done.exec_()




#Main method
    def main_functions(self):
        self.bt_of_input.clicked.connect(self.function_input_folder)
        self.bt_of_output.clicked.connect(self.function_output_folder)
        self.start.clicked.connect(self.sort)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())