import src.connection.connection_db as conn


class CategoriaModel:
    def __init__(self, codigo="", nome=""):
        self.codigo = codigo
        self.nome = nome

        self.dados = (self.nome,)

        self.conn = conn.Connection()

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @codigo.setter
    def codigo(self, var):
        self._codigo = str(var).strip()

    @nome.setter
    def nome(self, var):
        self._nome = str(var).strip().upper()

    # Funçoes

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

    def update_categoria(self):
        if self.codigo != "":
            if self.not_vazio():
                try:
                    self.conn.connect_db()

                    self.conn.cursor.execute("""
                        UPDATE categorias SET nome_cate=? WHERE pk_id_categoria=?
                    """, (self.nome, self.codigo))

                    self.conn.close_db()
                    print('categoria alterada com sucesso')

                    return True
                except:
                    return False
            else:
                print('passe um nome da categoria')
                return False
        else:
            print('passe o codigo da categoria para alterar')
            return False

    def delete_categoria(self):
        if self.codigo != "":
            try:
                self.conn.connect_db()

                self.conn.cursor.execute("""
                    DELETE FROM categorias WHERE pk_id_categoria=?
                """, self.codigo)

                self.conn.close_db()
                print('categoria apagada com sucesso')

                return True
            except:
                print('erro ao apagar a categoria')
                return False
        else:
            print('passe o codigo da categoria para apagar')
            return False

    def select_categoria(self):
        if self.not_vazio():
            try:
                self.conn.connect_db()

                dados = self.conn.cursor.execute("""
                    SELECT * FROM categorias WHERE nome_cate=?
                """, self.dados).fetchone()

                self.conn.close_db()

                return dados
            except:
                print('erro ao pesquisar categoria')
                return None
        else:
            print('passar o nome da categoria')
            return None

    def select_all_categorias(self):
        try:
            self.conn.connect_db()

            dados = self.conn.cursor.execute("""
                SELECT pk_id_categoria, nome_cate FROM categorias
            """).fetchall()

            self.conn.close_db()

            return dados
        except:
            print('erro ao pesquisar categorias')
            return None
