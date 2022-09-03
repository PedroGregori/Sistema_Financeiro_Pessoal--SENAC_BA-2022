from .db import connect

class Home_dao():
    def receitaSUM():
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT SUM(valor) FROM receitas;"
        cursor.execute(SQL)
        total_receitas = cursor.fetchall()
        conn.close()
        
        return total_receitas 
    
    def despesaSUM():
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT SUM(valor) FROM despesas;"
        cursor.execute(SQL)
        total_despesas = cursor.fetchall()
        conn.close()
    
        return total_despesas 