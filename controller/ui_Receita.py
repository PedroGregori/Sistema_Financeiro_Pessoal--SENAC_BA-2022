from PyQt5.QtWidgets import QWidget,  QTableWidgetItem, QHeaderView
from PyQt5 import uic

from model.receita import receitaOBJ as r_OBJ
from model.receitaDAO import Receita_dao as r_DAO

FILE_UI = 'view/receita.ui'

class Receita_ui(QWidget):
    def __init__(self):
        super(Receita_ui, self).__init__()
        uic.loadUi(FILE_UI, self) 
        
        self.saveBtn.clicked.connect(self.add)
        self.editBtn.clicked.connect(self.edit)
        self.delBtn.clicked.connect(self.delete)
        
        self.table.horizontalHeader().setStretchLastSection(True) 
        self.table.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch)
        
        self.loadData()

    def loadData(self):
        list_receita = r_DAO.selectALL()
        for r  in list_receita:
            self.addTableWidget(r)
            
    def add(self):
        descricao = self.descricao.text()
        valor = self.valor.text()
        valor = valor.replace(",", ".")
        nova_receita = r_OBJ(-1,descricao, float(valor))
        id = r_DAO.add(nova_receita)
        nova_receita.id = id   
        
        self.addTableWidget(nova_receita)
        
        self.descricao.clear()
    
    def edit(self):
        line = self.table.currentRow()
        lineItem = self.table.item(line, 0)
        
        id = lineItem.text()
        descricao = self.descricao.text()
        valor = self.valor.text()
        
        edit = r_OBJ(id,descricao,valor)
        r_DAO.edit(edit)
        self.updateTable(edit)

        self.descricao.clear()
    
    def delete(self):
        line = self.table.currentRow()
        lineItem = self.table.item(line, 0)
        id  = lineItem.text()
        self.table.removeRow(line)
        r_DAO.delete(int(id))
    
    def addTableWidget(self, r: r_OBJ):
        line = self.table.rowCount()
        self.table.insertRow(line)
        
        id = QTableWidgetItem(str(r.id))
        descricao = QTableWidgetItem(r.descricao)
        valor = QTableWidgetItem(str(r.valor))
        
        self.table.setItem(line, 0, id)
        self.table.setItem(line, 1, descricao)
        self.table.setItem(line, 2, valor)
        
    def updateTable(self, r: r_OBJ):
        line = self.table.currentRow()
        
        descricao = QTableWidgetItem(r.descricao)
        valor = QTableWidgetItem(str(r.valor))
        
        self.table.setItem(line, 1, descricao)
        self.table.setItem(line, 2, valor)