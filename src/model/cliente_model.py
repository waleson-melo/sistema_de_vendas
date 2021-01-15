import src.connection.connection_db as conn


class ClienteModel:
    def __init__(self, codigo='', cpf='', nome='', telefone='', endereco='',
                 observacao=''):

        self.codigo = codigo
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.observacao = observacao

        self.dados = (self.cpf, self.nome, self.telefone, self.endereco,
                      self.observacao)

        self.conn = conn.Connection()

    @property
    def codigo(self):
        return self._codigo

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @property
    def endereco(self):
        return self._endereco

    @property
    def observacao(self):
        return self._observacao

    @codigo.setter
    def codigo(self, value):
        self._codigo = str(value).strip()

    @cpf.setter
    def cpf(self, value):
        self._cpf = str(value).strip()

    @nome.setter
    def nome(self, value):
        self._nome = str(value).strip().upper()

    @telefone.setter
    def telefone(self, value):
        self._telefone = str(value).strip()

    @endereco.setter
    def endereco(self, value):
        self._endereco = str(value).strip().upper()

    @observacao.setter
    def observacao(self, value):
        self._observacao = str(value).strip().upper()
