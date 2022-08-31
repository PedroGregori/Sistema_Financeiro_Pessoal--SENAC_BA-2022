from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import uic
from controller.home import Home

from theme.app_theme import LIGHT, DARK


FILE_UI = 'view/main_window.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(FILE_UI, self)  
        
        self.pageHome = Home()
        
        self.stackedWidget.addWidget(self.pageHome)
        self.stackedWidget.addWidget(self.pageReceita)
        self.stackedWidget.addWidget(self.pageDespesa)
        
        self.homeBtn.clicked.connect(self.actionMenu)
        self.receitaBtn.clicked.connect(self.actionMenu)
        self.despesaBtn.clicked.connect(self.actionMenu)
        self.themeBtn.clicked.connect(self.actionMenu)
        
    def checkButton(self):
        if self.themeBtn.isChecked():
            self.setStyleSheet(DARK)
        else:
            self.setStyleSheet(LIGHT)

    def actionMenu(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "homeBtn":
            self.stackedWidget.setCurrentIndex(0)
        if btnName == "receitaBtn":
            self.stackedWidget.setCurrentIndex(1)
        if btnName == "despesaBtn":
            self.stackedWidget.setCurrentIndex(2)
        
        if btnName == 'themeBtn':
            self.checkButton()