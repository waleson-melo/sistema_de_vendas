import src.model.cliente_model as clieMode


class ClienteController:
    def __init__(self):
        pass

    @staticmethod
    def insert(cpf = '', nome='', telefone='', endereco='', observacao=''):
        clim = clieMode.ClienteModel(cpf=cpf, nome=nome, telefone=telefone,
                                     endereco=endereco, observacao=observacao)
        return clim.insert_cliente()

    @staticmethod
    def update(codigo='', cpf = '', nome='', telefone='', endereco='',
               observacao=''):
        clim = clieMode.ClienteModel(codigo=codigo, cpf=cpf, nome=nome,
                                     telefone=telefone, endereco=endereco,
                                     observacao=observacao)
        return clim.update_cliente()

    @staticmethod
    def delete(codigo=''):
        clim = clieMode.ClienteModel(codigo=codigo)
        return clim.delete_cliente()

    @staticmethod
    def select(cpf=''):
        clim = clieMode.ClienteModel(cpf=cpf)
        return clim.select_cliente()

    @staticmethod
    def select_all():
        clim = clieMode.ClienteModel()
        return clim.select_all_cliente()
