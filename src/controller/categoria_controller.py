import src.model.categoria_model as cateModel


class CategoriaController:
    def __init__(self):
        pass

    @staticmethod
    def insert(nome):
        catm = cateModel.CategoriaModel(nome=nome)
        return catm.insert_categoria()

    @staticmethod
    def update(codigo, nome):
        catm = cateModel.CategoriaModel(codigo=codigo, nome=nome)
        return catm.update_categoria()

    @staticmethod
    def delete(codigo):
        catm = cateModel.CategoriaModel(codigo=codigo)
        return catm.delete_categoria()

    @staticmethod
    def select(nome):
        catm = cateModel.CategoriaModel(nome=nome)
        return catm.select_categoria()

    @staticmethod
    def select_all():
        catm = cateModel.CategoriaModel()
        return catm.select_all_categorias()
