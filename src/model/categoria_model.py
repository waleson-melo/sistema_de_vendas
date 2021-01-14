import src.connection.connection_db as conn


class CategoriaModel:
    def __init__(self, nome):
        self.nome = nome

        self.conn = conn.Connection()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, var):
        self._nome = str(var).strip().upper()
