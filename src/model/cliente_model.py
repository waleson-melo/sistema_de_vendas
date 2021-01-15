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

    # Functions

    def not_empty(self):
        cond = [
            self.cpf != '',
            self.nome != ''
        ]

        if all(cond):
            return True
        else:
            return False

    def insert_cliente(self):
        if self.not_empty():
            try:
                self.conn.connect_db()

                self.conn.cursor.execute("""
                    INSERT INTO clientes (cpf_clie, nome_clie, telefone_clie,
                    endereco_clie, observacao_clie)
                    VALUES (?, ?, ?, ?, ?)
                """, self.dados)

                self.conn.close_db()
                print('cliente inserido com sucesso')

                return True
            except:
                print('erro ao inserir cliente')
                return False
        else:
            print('preencha os campos obrigatorios')
            return False

    def update_cliente(self):
        if self.codigo != '':
            if self.not_empty():
                try:
                    self.conn.connect_db()

                    self.conn.cursor.execute("""
                        UPDATE clientes
                        SET cpf_clie=?, nome_clie=?, telefone_clie=?,
                        endereco_clie=?, observacao_clie=?
                        WHERE pk_id_cliente=?
                    """, (self.cpf, self.nome, self.telefone, self.endereco,
                          self.observacao, self.codigo))

                    self.conn.close_db()
                    print('cliente alterado com sucesso')

                    return True
                except:
                    print('erro ao atualizar usuario')
                    return False
            else:
                print('preencha os campos obrigatorios')
                return False
        else:
            print('passe o codigo do cliente para alterar')
            return False

    def delete_cliente(self):
        if self.codigo != '':
            try:
                self.conn.connect_db()

                self.conn.cursor.execute("""
                    DELETE FROM clientes WHERE pk_id_cliente=?
                """, (self.codigo,))
                print('cliente apagado com sucesso')

                self.conn.close_db()

                return True
            except:
                print('erro ao deletar cliente')
                return False
        else:
            print('passe o codigo do cliente para deletar')
            return False

