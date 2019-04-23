import sys, threading, requests, time
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog, QLabel
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5 import *


class Television(QMainWindow):
    def __init__(self):
        super(Television, self).__init__()
        loadUi('Interface/television.ui',self)
        self.setWindowTitle('Televizyon Kontrol Arayüzü')
        self.tvCount = 0
        self.tvArtirBtn.clicked.connect(self.tvArtirBtn_clicked)
        self.tvAzaltBtn.clicked.connect(self.tvAzaltBtn_clicked)
        self.tvCh1Link = "http://192.168.137.103/3/kanal1"
        self.tvCh2Link = "http://192.168.137.103/3/kanal2"
        self.tvCloseLink = "http://192.168.137.103/3/kapat"
        self.statusLink = "http://192.168.137.103/3"

    @pyqtSlot()
    def tvArtirBtn_clicked(self):
        self.tvCount = self.tvCount + 1
        if int(self.tvCount) > len(self.tvListWidget):
            self.tvCount = 1
        self.label.setText(''+str(int(self.tvCount)))
        self.tvListWidget.setCurrentRow(self.tvCount-1)
        print(str(self.tvListWidget.currentItem().text()))

    def tvAzaltBtn_clicked(self):
        self.tvCount = self.tvCount - 1
        if int(self.tvCount) <= 0:
            self.tvCount = len(self.tvListWidget)
        self.label.setText(''+str(int(self.tvCount)))
        self.tvListWidget.setCurrentRow(self.tvCount-1)
        print(str(self.tvListWidget.currentItem().text()))

    def tvStatus(self):
        try:
            tv_status = requests.post(self.statusLink)
            return tv_status.json()
        except:
            return 0
    
    def chStatusShow(self): #showing channel status
        if self.tvStatus() == 1:
            chStat = "Kanal 1 Acik"
        elif self.tvStatus() == 2:
            chStat = "Kanal 2 Acik"
        else:
            chStat = "TV Kapali"
        self.tvStatusLbl.setText(chStat)
        
