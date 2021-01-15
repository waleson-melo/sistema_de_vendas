import src.connection.connection_db as conn


class ProdutoModel:
    def __init__(self, codigo='', codigo_barra='', nome='', preco='',
                 quantidade='', descricao='', fk_categoria=''):

        self.codigo = codigo
        self.codigo_barra = codigo_barra
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.descricao = descricao
        self.fk_categoria = fk_categoria

        self.dados = (
            self.codigo_barra,
            self.nome,
            self.preco,
            self.quantidade,
            self.descricao,
            self.fk_categoria
        )

        self.conn = conn.Connection()

    @property
    def codigo(self):
        return self._codigo

    @property
    def codigo_barra(self):
        return self._codigo_barra

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @property
    def quantidade(self):
        return self._quantidade

    @property
    def descricao(self):
        return self._descricao

    @property
    def fk_categoria(self):
        return self._fk_categoria

    @codigo.setter
    def codigo(self, value):
        self._codigo = str(value).strip()

    @codigo_barra.setter
    def codigo_barra(self, value):
        self._codigo_barra = str(value).strip()

    @nome.setter
    def nome(self, value):
        self._nome = str(value).strip().upper()

    @preco.setter
    def preco(self, value):
        self._preco = str(value).strip()

    @quantidade.setter
    def quantidade(self, value):
        self._quantidade = str(value).strip()

    @descricao.setter
    def descricao(self, value):
        self._descricao = str(value).strip().upper()

    @fk_categoria.setter
    def fk_categoria(self, value):
        self._fk_categoria = str(value).strip()

    # Functions

    def not_empty(self):
        cond = [
            self.codigo_barra != '',
            self.nome != '',
            self.preco != '',
            self.quantidade != '',
            self.fk_categoria != ''
        ]

        if all(cond):
            return True
        else:
            return False

    def insert_produto(self):
        if self.not_empty():
            try:
                self.conn.connect_db()

                self.conn.cursor.execute("""
                    INSERT INTO produtos (codigo_barra_prod, nome_prod,
                        preco_prod, quantidade_prod, descricao_prod,
                        fk_categoria)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, self.dados)

                self.conn.close_db()
                print('produto inserido com sucesso')

                return True
            except:
                print('erro ao inserir produto')
                return False
        else:
            print('preencha os campos obrigatorios')
            return False
