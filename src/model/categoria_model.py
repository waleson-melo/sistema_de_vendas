import src.connection.connection_db as conn


class CategoriaModel:
    def __init__(self):
        self.conn = conn.Connection()

    def insert_categoria(self, nome):
        self.conn.connect_db()
        last_id = self.conn.cursor.execute("""
            INSERT INTO compras (valor_comp, data_comp, status_comp, fk_cliente)
            VALUES (25.50, '14/01/2021', 'pendente', '1')
        """).lastrowid
        self.conn.close_db()

        print(last_id)
