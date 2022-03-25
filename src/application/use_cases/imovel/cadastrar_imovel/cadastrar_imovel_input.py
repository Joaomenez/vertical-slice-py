class CadastrarImovelInput:
    rua: str
    numero: int
    bairro: str
    cidade: str
    estado: str

    def __init__(self, obj: dict = None):
        if obj:
            self.rua = obj['rua']
            self.numero = obj['numero']
            self.bairro = obj['bairro']
            self.cidade = obj['cidade']
            self.estado = obj['estado']
