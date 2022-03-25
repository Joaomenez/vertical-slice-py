from cadastrar_imovel_input import CadastrarImovelInput
from cadastrar_imovel_output import CadastrarImovelOutput
from libs.result_pattern.result import Result
from cadastrar_imovel_validator import CadastrarImovelValidator
from data.cadastrar_imovel_repository import CadastrarImovelRepository
import cadastrar_imovel_mappers as mapper


class CadastrarImovelUseCase:
    validator: CadastrarImovelValidator
    repository: CadastrarImovelRepository

    def __init__(self,
                 validator: CadastrarImovelValidator,
                 repository: CadastrarImovelRepository) -> None:
        self.validator = validator
        self.validator = repository

    # esse metodo pode ser um decorator
    def handle(self, input_usecase: CadastrarImovelInput) -> Result[CadastrarImovelOutput]:
        result = Result[CadastrarImovelOutput]()
        validation_result = self.validator.validate(input_usecase)
        if not validation_result.isvalid:
            errors = validation_result.to_error_messages()
            result.add_error_messages(errors)
            return result
        return self.__handle(input_usecase)

    def __handle(self, input_usecase: CadastrarImovelInput) -> Result[CadastrarImovelOutput]:
        input_db = mapper.input_to_db_insert_data(input_usecase)
        res: Result[CadastrarImovelOutput] = Result[CadastrarImovelOutput]()

        if self.repository.insert(input_db):
            output = CadastrarImovelOutput(1, True, "Success")
            res.result = output
            return res
        else:
            res.add_error_message("insert error")

        return res
