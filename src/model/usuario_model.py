import src.connection.connection_db as conn


class UsuarioModel:
    def __init__(self, codigo="", cpf="", nome="", telefone="", senha="",
                 endereco="", observacao=""):

        self.codigo = codigo
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.senha = senha
        self.endereco = endereco
        self.observacao = observacao

        self.dados = (self.cpf, self.nome, self.telefone, self.senha,
                      self.endereco, self.observacao)

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
    def senha(self):
        return self._senha

    @property
    def endereco(self):
        return self._endereco

    @property
    def observacao(self):
        return self._observacao

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @cpf.setter
    def cpf(self, value):
        self._cpf = str(value).strip()

    @nome.setter
    def nome(self, value):
        self._nome = str(value).strip().upper()

    @telefone.setter
    def telefone(self, value):
        self._telefone = str(value).strip()

    @senha.setter
    def senha(self, value):
        self._senha = str(value).strip()

    @endereco.setter
    def endereco(self, value):
        self._endereco = str(value).strip().upper()

    @observacao.setter
    def observacao(self, value):
        self._observacao = str(value).strip().upper()

    # Functions

    def not_empty(self):
        cond = [
            self.cpf != "",
            self.nome != "",
            self.senha != ""
        ]
        if all(cond):
            return True
        else:
            return False

    def insert_usuario(self):
        if self.not_empty():
            try:
                self.conn.connect_db()

                self.conn.cursor.execute("""
                    INSERT INTO usuarios (cpf_usua, nome_usua, telefone_usua,
                        senha_usua, endereco_usua, observacao_usua) 
                    VALUES (?, ?, ?, ?, ?, ?)
                """, self.dados)

                self.conn.close_db()
                print('usuario inserido com sucesso')

                return True
            except:
                print('erro ao inserir usuario')
                return False
        else:
            print('campos obrigatorios precisam ser preenchidos')
            return False

    def update_usuario(self):
        if self.codigo != "":
            if self.not_empty():
                try:
                    self.conn.connect_db()

                    self.conn.cursor.execute("""
                        UPDATE usuarios
                        SET cpf_usua=?, nome_usua=?, telefone_usua=?,
                            senha_usua=?, endereco_usua=?, observacao_usua=?
                        WHERE pk_id_usuario=?
                    """, (self.cpf, self.nome, self.telefone, self.senha,
                        self.endereco, self.observacao, self.codigo))

                    self.conn.close_db()

                    print('usuario alterado com sucesso')

                    return True
                except:
                    print('erro ao alterar usuario: ')
                    return False
            else:
                print('preencha os campos obrigatorios')
                return False
        else:
            print('passe o codigo do usuario para alterar')
            return False

    def delete_usuario(self):
        if self.codigo != "":
            try:
                self.conn.connect_db()

                self.conn.cursor.execute("""
                    DELETE FROM usuarios WHERE pk_id_usuario=?
                """, (self.codigo,))
                print('usuario apagado com sucesso')

                self.conn.close_db()

                return True
            except:
                print('erro ao deletar usuario')
                return False
        else:
            print('passe o codigo do usuario para deletar')
            return False

    def select_usuario(self):
        if self.cpf != "":
            try:
                self.conn.connect_db()

                dados = self.conn.cursor.execute("""
                    SELECT pk_id_usuario, cpf_usua, nome_usua, telefone_usua,
                        senha_usua, endereco_usua, observacao_usua 
                    FROM usuarios
                    WHERE cpf_usua=?
                """, (self.cpf,)).fetchone()

                self.conn.close_db()

                return dados
            except:
                print('erro ao buscar usuario')
                return None
        else:
            print('passe o cpf do usuario para pesquisar')
            return None

    def select_all_usuario(self):
        try:
            self.conn.connect_db()

            dados = self.conn.cursor.execute("""
                SELECT pk_id_usuario, cpf_usua, nome_usua, telefone_usua,
                senha_usua, endereco_usua, observacao_usua 
                FROM usuarios
            """).fetchall()

            self.conn.close_db()

            return dados
        except:
            print('erro ao pesquisar usuarios')
            return None
