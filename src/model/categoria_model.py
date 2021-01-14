import src.connection.connection_db as conn


class CategoriaModel:
    def __init__(self, nome=""):
        self.nome = nome

        self.dados = (self.nome,)

        self.conn = conn.Connection()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, var):
        self._nome = str(var).strip().upper()

    def not_vazio(self):
        if self.nome != "":
            return True
        else:
            return False

    def insert_categoria(self):
        if self.not_vazio():
            self.conn.connect_db()

            self.conn.cursor.execute("""
                INSERT INTO categorias (nome_cate)
                VALUES (?)
            """, self.dados)
            print('inserido com sucesso')

            self.conn.close_db()
        else:
            print('esta vazio')
            return False
