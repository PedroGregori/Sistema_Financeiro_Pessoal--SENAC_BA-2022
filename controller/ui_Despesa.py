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
        
        self.table.horizontalHeader().setStretchLastSection(True) 
        self.table.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch) 
        
        self.loadData()

    def loadData(self):
        list_Despesa = d_DAO.selectALL()
        for d  in list_Despesa:
            self.addTableWidget(d)
            
    def add(self):
        descricao = self.descricao.text()
        valor = self.valor.text()
        valor = valor.replace(",", ".")
        nova_despesa = d_OBJ(-1,descricao, float(valor))
        id = d_DAO.add(nova_despesa)
        nova_despesa.id = id 
        
        self.addTableWidget(nova_despesa)
        
        self.descricao.clear()
    
    def edit(self):
        line = self.table.currentRow()
        lineItem = self.table.item(line, 0)
        
        id = lineItem.text()
        descricao = self.descricao.text()
        valor = self.valod.text()
        
        edit = d_OBJ(id,descricao,valor)
        d_DAO.edit(edit)
        self.updateTable(edit)

        self.descricao.clear()
    
    def delete(self):
        line = self.table.currentRow()
        lineItem = self.table.item(line, 0)
        id  = lineItem.text()
        self.table.removeRow(line)
        d_DAO.delete(int(id))
    
    def addTableWidget(self, d: d_OBJ):
        line = self.table.rowCount()
        self.table.insertRow(line)
        
        id = QTableWidgetItem(str(d.id))
        descricao = QTableWidgetItem(d.descricao)
        valor = QTableWidgetItem(str(d.valor))
        
        self.table.setItem(line, 0, id)
        self.table.setItem(line, 1, descricao)
        self.table.setItem(line, 2, valor)
        
    def updateTable(self, d: d_OBJ):
        line = self.table.currentRow()
        
        descricao = QTableWidgetItem(d.descricao)
        valor = QTableWidgetItem(str(d.valor))
        
        self.table.setItem(line, 1, descricao)
        self.table.setItem(line, 2, valor)