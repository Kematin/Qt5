from interface import Ui_MainWindow

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets, QtGui, QtCore

import sys
from bs4 import BeautifulSoup
import requests
import lxml

class YoutubeDownload(QtWidgets.QMainWindow):
    def __init__(self):
        super(YoutubeDownload, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.set_url.clicked.connect(self.get_url)

        self.headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
        }

    def get_url(self):
        url = self.ui.url.text()
        if 'https://www.youtube.com/watch?' not in url:
            error = QMessageBox()
            error.setWindowTitle('ERRROR')
            error.setText('YOU ARE DOLBAEB. WHERE IS NORMALI URL')
            error.exec_()
        else:
            self.collect_info(url)



    def collect_info(self, href):
        req = requests.get(href, headers=self.headers)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')  

        name_and_data = soup.find_all('yt-formatted-string', class_='style-scope ytd-video-primary-info-renderer')
        print(name_and_data)

        '''
        data = name_and_data.text
        name = name_and_data.text
        likes = soup.find('yt-formatted-string', class_='style-scope ytd-toggle-button-renderer style-default-active').text


        self.ui.get_info.setText('')
        self.ui.get_info.setText(f'{name}\n{likes}\n{data}')
        '''


    def download(self, href):
        


#Инцилизация интерфейса
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = YoutubeDownload()
    application.show()
    sys.exit(app.exec_())
