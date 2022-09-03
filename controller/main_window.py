from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from controller.ui_home import Home_ui
from controller.ui_Receita import Receita_ui
from controller.ui_Despesa import Despesa_ui

from theme.app_theme import LIGHT, DARK

FILE_UI = 'view/main_window.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(FILE_UI, self)  
        
        self.setStyleSheet(LIGHT)
        
        self.pageHome = Home_ui()
        self.pageReceita = Receita_ui()
        self.pageDespesa = Despesa_ui()
        
        self.stackedWidget.addWidget(self.pageHome)
        self.stackedWidget.addWidget(self.pageReceita)
        self.stackedWidget.addWidget(self.pageDespesa)
        
        self.homeBtn.clicked.connect(self.actionMenu)
        self.receitaBtn.clicked.connect(self.actionMenu)
        self.despesaBtn.clicked.connect(self.actionMenu)
        self.themeBtn.clicked.connect(self.actionMenu)
        
    def updateHome(self,action):
        btn = self.homeBtn.clicked.connect(action)
        return btn
    
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
            self.updateHome()
        if btnName == "receitaBtn":
            self.stackedWidget.setCurrentIndex(1)
        if btnName == "despesaBtn":
            self.stackedWidget.setCurrentIndex(2)

        
        if btnName == 'themeBtn':
            self.checkButton()