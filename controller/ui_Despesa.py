from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

FILE_UI = 'view/despesa.ui'

class Despesa_ui(QWidget):
    def __init__(self):
        super(Despesa_ui, self).__init__()
        uic.loadUi(FILE_UI, self) 