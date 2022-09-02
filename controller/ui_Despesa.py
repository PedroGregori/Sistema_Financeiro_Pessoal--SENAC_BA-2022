from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5 import uic

from model.despesa import despesaOBJ as d_OBJ
from model.despesaDAO import Depesa_dao as d_DAO

FILE_UI = 'view/despesa.ui'

class Despesa_ui(QWidget):
    def __init__(self):
        super(Despesa_ui, self).__init__()
        uic.loadUi(FILE_UI, self) 
        
        self.saveBtn.clicked.connect(self.add)
        self.editBtn.clicked.connect(self.edit)
        self.delBtn.clicked.connect(self.delete)
        
        self.tabela.horizontalHeader().setStretchLastSection(True) 
        self.tabela.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch) 
        
        self.loadData()

    def loadData(self):
        list_Despesa = d_DAO.selectALL()
        for d  in list_Despesa:
            self.addTableWidget(d)
            
    def add(self):
        descricao = self.descricao.text()
        valor = self.valor.text()
        nova_despesa = d_OBJ(-1,descricao, float(valor))
        id = d_DAO.add(nova_despesa)
        nova_despesa.id = id 
    
    def edit():
        pass
    
    def delete():
        pass