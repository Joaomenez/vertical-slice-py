from __future__ import annotations
from core.use_cases.imovel.cadastrar_imovel.cadastrar_imovel_input import CadastrarImovelInput
from lib.validation.validation_output import ValidationOutput

class CadastrarImovelValidation:
    def __init__(self):
        self.__validation_output = ValidationOutput()

    def validate(self, input: CadastrarImovelInput) -> ValidationOutput:
        self.__validate_instancetype(input)\
            .__validate_numero(input)\
            .__validate_rua(input)
        
        return self.__validation_output
        
    def __validate_instancetype(self, input) -> CadastrarImovelValidation:
        if isinstance(input, CadastrarImovelInput) != True:
            self.__validation_output.add__message("tipo de instancia invalido")
        return self

    def __validate_rua(self, input: CadastrarImovelInput) -> CadastrarImovelValidation:
        if isinstance(input.rua, int) != True:
            self.__validation_output.add_var_type_error_message(input.rua,f'{input.rua}', type(int))
        return self

    def __validate_numero(self, input: CadastrarImovelInput)-> CadastrarImovelValidation:
        if isinstance(input.numero, int):
            self.__validation_output.add_var_type_error_message(input.numero, f'{input.numero}', type(int))
        return self