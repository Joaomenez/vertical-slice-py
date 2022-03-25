import src.\
    application.\
    use_cases.\
    imovel.\
    cadastrar_imovel.\
    cadastrar_imovel_builder as usecase_builder
from src\
    .application\
    .use_cases\
    .imovel\
    .cadastrar_imovel.cadastrar_imovel_output import CadastrarImovelOutput
from libs.result_pattern.result import Result
import cadastrar_imovel_lambda_mapper as mapper


def lambda_handler(event, context):
    request = mapper.event_to_request_dto(event)
    input_usecase = request.to_input_usecase()
    usecase = usecase_builder.build()
    output_usecase: Result[CadastrarImovelOutput] = usecase.handle(input_usecase)


