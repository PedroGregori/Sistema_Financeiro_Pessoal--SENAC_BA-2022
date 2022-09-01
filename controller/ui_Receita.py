from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

FILE_UI = 'view/receita.ui'

class Receita_ui(QWidget):
    def __init__(self):
        super(Receita_ui, self).__init__()
        uic.loadUi(FILE_UI, self) 