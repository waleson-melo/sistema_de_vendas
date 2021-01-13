import sqlite3
import os


class Connection:
    def __init__(self):
        self.create_tables()

    def connect_db(self):
        if not os.path.isdir(".sistema_de_vendas/database"):
            os.makedirs("./sistema_de_vendas/database")

        self.conn = sqlite3.connect("./sistema_de_vendas/database")
        self.cursor = self.conn.cursor()

    def close_db(self):
        self.cursor.close()

    def create_tables(self):
        self.connect_db()

        self.cursor.execute("""
            CREATE TABLE "usuario" (
                "pk_id_usuario"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "cpf_usua"	TEXT NOT NULL UNIQUE,
                "nome_usua"	TEXT NOT NULL,
                "telefone_usua"	TEXT,
                "endereco_usua"	TEXT,
                "senha_usua"	TEXT NOT NULL,
                "observacao_usua"	TEXT
            );
        """)

        self.cursor.execute("""
            CREATE TABLE "categorias" (
                "pk_id_categoria"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "nome_cate"	TEXT NOT NULL UNIQUE
            );
        """)
        # Criar chave estrangeira aqui
        self.cursor.execute("""
            CREATE TABLE "produtos" (
                "pk_id_produto"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "codigo_barra_prod"	TEXT NOT NULL,
                "nome_prod"	TEXT NOT NULL UNIQUE,
                "preco_prod"	REAL NOT NULL,
                "quantidade_prod"	INTEGER NOT NULL,
                "descricao_prod"	TEXT,
                "fk_categoria"	INTEGER
            );
        """)

        self.conn.commit()
        self.close_db()
