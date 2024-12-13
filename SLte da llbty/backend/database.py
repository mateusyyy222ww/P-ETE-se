import sqlite3

def init_db():
    conn = sqlite3.connect('atracoes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS atracoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT NOT NULL,
                    descricao TEXT NOT NULL,
                    arquivo TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

def add_atracao(tipo, descricao, arquivo):
    conn = sqlite3.connect('atracoes.db')
    c = conn.cursor()
    c.execute("INSERT INTO atracoes (tipo, descricao, arquivo) VALUES (?, ?, ?)", (tipo, descricao, arquivo))
    conn.commit()
    conn.close()
