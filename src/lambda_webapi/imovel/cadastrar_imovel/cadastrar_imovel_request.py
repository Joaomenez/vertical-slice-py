from src.application.\
    use_cases.\
    imovel.\
    cadastrar_imovel.\
    cadastrar_imovel_input import CadastrarImovelInput


class CadastrarImovelRequest:
    rua: str
    numero: int
    bairro: str
    cidade: str
    estado: str

    def to_input_usecase(self):
        input_usecase = CadastrarImovelInput()
        input_usecase.rua = self.rua
        input_usecase.bairro = self.bairro
        input_usecase.estado = self.estado
        input_usecase.numero = self.numero
        input_usecase.cidade = self.cidade