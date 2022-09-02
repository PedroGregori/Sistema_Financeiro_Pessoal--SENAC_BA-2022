import sqlite3

FILE_DB = 'database/financas.db'

def connect():
    conn = sqlite3.connect(FILE_DB)
    return conn