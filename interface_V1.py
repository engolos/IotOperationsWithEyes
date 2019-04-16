import sys, threading
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog, QLabel
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import *
import eye

class denemem(QDialog):
    def __init__(self):
        super(denemem,self).__init__()
        loadUi('denemem.ui',self)
        self.setWindowTitle('Tez Deneme UI')
        self.artirBtn.clicked.connect(self.artirBtn_clicked)
        self.azaltBtn.clicked.connect(self.azaltBtn_clicked)
        self.sayac = 0
        
    @pyqtSlot()
    def artirBtn_clicked(self):
        self.sayac=self.sayac + 1
        if int(self.sayac) > 4:
            self.sayac = 1
        self.label.setText(''+str(int(self.sayac)))
        self.listWidget.setCurrentRow(self.sayac-1)
        print(str(self.listWidget.currentItem().text())) #print selected item on listview

    def azaltBtn_clicked(self):
        self.sayac=self.sayac - 1
        if int(self.sayac) <= 0:
            self.sayac = 4
        self.label.setText(''+str(int(self.sayac)))
        self.listWidget.setCurrentRow(self.sayac-1)
        print(str(self.listWidget.currentItem().text()))


    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget=denemem()
    widget.show()
    eye_status = eye.Eye()
    while True:
        print(eye_status.get_frame())
        command = 0
        if(command == "-"):
            widget.azaltBtn_clicked()
        elif(command == "+"):
            widget.artirBtn_clicked()
