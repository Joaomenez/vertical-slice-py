from libs.validation.base_validator import BaseValidator
from libs.validation.validation_output import ValidationOutput
from cadastrar_imovel_input import CadastrarImovelInput


class CadastrarImovelValidator(BaseValidator):
    def validate(self, input_usecase: CadastrarImovelInput) -> ValidationOutput:
        self.__validate_rua(input_usecase)
        self.__validate_bairro(input_usecase)
        self.__validate_estado(input_usecase)
        return self._validate()

    def __validate_rua(self, input_usecase: CadastrarImovelInput):
        self.rule_for(input_usecase.rua, 'rua') \
            .str_() \
            .min_length(5)

    def __validate_bairro(self, input_usecase: CadastrarImovelInput):
        self.rule_for(input_usecase.bairro, 'bairro') \
            .str_() \
            .min_length(5)

    def __validate_estado(self, input_usecase: CadastrarImovelInput):
        self.rule_for(input_usecase.estado, 'estado') \
            .str_() \
            .min_length(5)
