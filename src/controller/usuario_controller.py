import src.model.usuario_model as usuaMode


class UsuarioModel:
    def __init__(self):
        pass

    @staticmethod
    def insert(cpf='', nome='', telefone='', senha='', endereco='',
               observacao=''):
        usum = usuaMode.UsuarioModel(cpf=cpf, nome=nome, telefone=telefone,
                                     senha=senha, endereco=endereco,
                                     observacao=observacao)
        return usum.insert_usuario()

    @staticmethod
    def update(codigo='' ,cpf='', nome='', telefone='', senha='', endereco='',
               observacao=''):
        usum = usuaMode.UsuarioModel(codigo=codigo, cpf=cpf, nome=nome, telefone=telefone,
                                     senha=senha, endereco=endereco,
                                     observacao=observacao)
        return usum.update_usuario()

    @staticmethod
    def delete(codigo=''):
        usum = usuaMode.UsuarioModel(codigo=codigo)
        return usum.delete_usuario()

    @staticmethod
    def select(cpf=''):
        usum = usuaMode.UsuarioModel(cpf=cpf)
        return usum.select_usuario()

    @staticmethod
    def select_all():
        usum = usuaMode.UsuarioModel()
        return usum.select_all_usuario()
