
class ImovelDataInsert:
    rua: str
    numero: int
    bairro: str
    cidade: str
    estado: str
    id_proprietario: int

    def __init__(self,
                 rua:str,
                 numero: int,
                 bairro: str,
                 cidade: str,
                 estado: str
                 ) -> None:
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado