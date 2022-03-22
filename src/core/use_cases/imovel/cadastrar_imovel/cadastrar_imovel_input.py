
class CadastrarImovelInput:
    def __init__(self, object=None):
        if object:
            self.rua = object.rua
            self.numero = object.numero


