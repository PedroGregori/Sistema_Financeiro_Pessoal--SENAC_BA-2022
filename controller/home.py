from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic

FILE_UI = 'view/home.ui'

class Home(QWidget):
    def __init__(self):
        super(Home, self).__init__()
        uic.loadUi(FILE_UI, self)  