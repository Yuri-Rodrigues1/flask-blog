#importa biblioteca sqlite
import sqlite3

#cria o banco de dados relacionado
connection = sqlite3.connect('database.db')

#execução do schema
with open('schema.sql') as f:
    connection.executescript(f.read())

#inicio da conecção com o banco
cur = connection.cursor()

#inserindo 2 registros
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
        )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
        )
#encerra conecção
connection.commit()
connection.close()
