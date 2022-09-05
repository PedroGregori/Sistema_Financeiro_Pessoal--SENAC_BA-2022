from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from model.homeDAO import Home_dao as h_DAO


FILE_UI = 'view/home.ui'

class Home_ui(QWidget):
    def __init__(self):
        super(Home_ui, self).__init__()
        uic.loadUi(FILE_UI, self)  
        #self.mainWindow = mainWindow
        
        self.aviso()
        
    def r_total(self):
        valor = h_DAO.receitaSUM()
        return valor[0] [0]
        
    def d_total(self):
        valor = h_DAO.despesaSUM()
        return valor[0] [0]
        
    def calc(self):
        receitas = self.r_total()
        despesas = self.d_total()
        if despesas == None:
            despesas = 0
        elif receitas == None:
            receitas = 0
        calc = receitas - despesas
        return calc
    
    def aviso(self):
        receitas = self.r_total()
        despesas = self.d_total()
        if despesas == None:
            despesas = 0
        elif receitas == None:
            receitas = 0
        
        calc = self.calc()
        
        self.total_receita.setText(f"Total de Receitas R$ {receitas}")
        self.total_despesa.setText(f"Total de Despesas R$ {despesas}")
        
        if calc < 0:
            self.total.setText(f"Prejuízo de R$ {calc}")
        else:
            self.total.setText(f"Lucro de R$ {calc}")
        print(calc)
    def update(self):
        return "s"