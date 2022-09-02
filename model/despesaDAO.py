from .db import connect
from .despesa import despesaOBJ as d_OBJ

class Depesa_dao():
    def add(d: d_OBJ):
        conn = connect()
        cursor = conn.cursor()
        SQL = "INSERT INTO despesas(descricao, valor) VALUES (?,?);"
        dados = [d.descricao,d.valor]
        cursor.execute(SQL, dados)
        id_return = cursor.execute("SELECT last_insert_rowid();")
        id = id_return.fetchall()[0] [0]
        conn.commit()
        conn.close()
            
        return id

    def edit(d: d_OBJ):
        conn = connect()
        cursor = conn.cursor()
        SQL = "UPDATE despesas SET descricao=?, valor=? WHERE id=?;"
        dados = [d.descricao,d.valor,d.id]
        cursor.execute(SQL, dados)
        conn.commit()
        conn.close()

    def delete(id: int):
        conn = connect()
        cursor = conn.cursor()
        SQL = "DELETE FROM despesas WHERE id=?;"
        cursor.execute(SQL,[id])
        conn.commit()
        conn.close()

    def selectALL():
        despesas_lst = []
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT * FROM despesas;"
        cursor.execute(SQL)
        return_list = cursor.fetchall()
        for d  in return_list:
            nova_despesa = d_OBJ(d[0],d[1],d[2])
            despesas_lst.append(nova_despesa)
                
        conn.close()
            
        return despesas_lst