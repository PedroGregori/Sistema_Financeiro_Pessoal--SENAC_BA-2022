from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from model.homeDAO import Home_dao as h_DAO
from controller.main_window import MainWindow

FILE_UI = 'view/home.ui'

class Home_ui(QWidget):
    def __init__(self):
        super(Home_ui, self).__init__()
        uic.loadUi(FILE_UI, self)  
        
        self.aviso()
        
    def r_total(self):
        valor = h_DAO.receitaSUM()
        return valor[0] [0]
        
    def d_total(self):
        valor = h_DAO.despesaSUM()
        return valor[0] [0]
        
    def calc(self):
        calc = (self.r_total()-self.d_total())
        return calc
    
    def aviso(self):
        receitas = self.r_total()
        despesas = self.d_total()
        calc = self.calc()
        
        self.total_receita.setText(f"Total de Receitas R$ {receitas}")
        self.total_despesa.setText(f"Total de Despesas R$ {despesas}")
        
        if calc < 0:
            self.total.setText(f"Prejuízo de R$ {calc}")
        else:
            self.total.setText(f"Lucro de R$ {calc}")
    
    def update(self):
        update = self.aviso()
        btn = MainWindow.updateHome(update)
        return btn