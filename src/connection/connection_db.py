import sqlite3
import os


class Connection:
    def __init__(self):
        self.create_tables()

    def connect_db(self):
        if not os.path.isdir(".sistema_de_vendas/database"):
            os.makedirs(".sistema_de_vendas/database")

        self.conn = sqlite3.connect(".sistema_de_vendas/database/sistema.db")
        self.cursor = self.conn.cursor()

    def close_db(self):
        self.conn.commit()
        self.cursor.close()

    def create_tables(self):
        self.connect_db()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "usuarios" (
                "pk_id_usuario"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "cpf_usua"	TEXT NOT NULL UNIQUE,
                "nome_usua"	TEXT NOT NULL,
                "telefone_usua"	TEXT,
                "senha_usua"	TEXT NOT NULL,
                "endereco_usua"	TEXT,
                "observacao_usua"	TEXT
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "categorias" (
                "pk_id_categoria"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "nome_cate"	TEXT NOT NULL UNIQUE
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "produtos" (
                "pk_id_produto"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "codigo_barra_prod"	TEXT NOT NULL,
                "nome_prod"	TEXT NOT NULL UNIQUE,
                "preco_prod"	REAL NOT NULL,
                "quantidade_prod"	INTEGER NOT NULL,
                "descricao_prod"	TEXT,
                "fk_categoria"	INTEGER NOT NULL,
                FOREIGN KEY("fk_categoria") REFERENCES "categorias"("pk_id_categoria")
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "clientes" (
                "pk_id_cliente"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "cpf_clie"	TEXT NOT NULL UNIQUE,
                "nome_clie"	TEXT NOT NULL,
                "telefone_clie"	TEXT,
                "endereco_clie"	TEXT,
                "observacao_clie"	TEXT
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "compras" (
                "pk_id_compra"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "valor_comp"	REAL NOT NULL,
                "data_comp"	TEXT NOT NULL,
                "status_comp"	TEXT NOT NULL,
                "fk_cliente"	INTEGER NOT NULL,
                FOREIGN KEY("fk_cliente") REFERENCES "clientes"("pk_id_cliente")
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "compra_produto" (
                "pk_id_compra_produto"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "fk_compra"	INTEGER NOT NULL,
                "fk_produto"	INTEGER NOT NULL,
                FOREIGN KEY("fk_compra") REFERENCES "compras"("pk_id_compra"),
                FOREIGN KEY("fk_produto") REFERENCES "produtos"("pk_id_produto")
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "dividas" (
                "pk_id_divida"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "valor_divi"	REAL NOT NULL,
                "observacao_divi"	TEXT,
                "fk_cliente"	INTEGER NOT NULL,
                FOREIGN KEY("fk_cliente") REFERENCES "clientes"("pk_id_cliente")
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "divida_compra" (
                "pk_id_divida_compra"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "fk_divida"	INTEGER NOT NULL,
                "fk_compra"	INTEGER NOT NULL,
                "quantidade_compra_produto"	INTEGER NOT NULL,
                FOREIGN KEY("fk_compra") REFERENCES "compras"("pk_id_compra"),
                FOREIGN KEY("fk_divida") REFERENCES "dividas"("pk_id_divida")
            );
        """)

        self.conn.commit()
        self.close_db()
