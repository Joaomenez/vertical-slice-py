from cadastrar_imovel_validator import CadastrarImovelValidator
from cadastrar_imovel_use_case import CadastrarImovelUseCase
from data.cadastrar_imovel_repository import CadastrarImovelRepository
import src.application.shared.infrastructure.db.maria.maria_db_builder as maria_db_builder


def build() -> CadastrarImovelUseCase:
    validator = CadastrarImovelValidator()
    context = maria_db_builder.build()
    repository = CadastrarImovelRepository(context)
    use_case = CadastrarImovelUseCase(validator, repository)
    return use_case
