from .db import connect
from .receita import receitaOBJ as r_OBJ

class Receita_dao():
    def add(r: r_OBJ):
        conn = connect()
        cursor = conn.cursor()
        SQL = "INSERT INTO receitas(descricao, valor) VALUES (?,?);"
        dados = [r.descricao,r.valor]
        cursor.execute(SQL, dados)
        id_return = cursor.execute("SELECT last_insert_rowid();")
        id = id_return.fetchall()[0] [0]
        conn.commit()
        conn.close()
            
        return id

    def edit(r: r_OBJ):
        conn = connect()
        cursor = conn.cursor()
        SQL = "UPDATE receitas SET descricao=?, valor=? WHERE id=?;"
        dados = [r.descricao,r.valor,r.id]
        cursor.execute(SQL, dados)
        conn.commit()
        conn.close()

    def delete(id: int):
        conn = connect()
        cursor = conn.cursor()
        SQL = "DELETE FROM receitas WHERE id=?;"
        cursor.execute(SQL,[id])
        conn.commit()
        conn.close()

    def selectALL():
        receitas_lst = []
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT * FROM receitas;"
        cursor.execute(SQL)
        return_list = cursor.fetchall()
        for c  in return_list:
            nova_despesa = r_OBJ([0],[1],[2])
            receitas_lst.append(nova_despesa)
                
        conn.close()
            
        return receitas_lst