from cadastrar_imovel_request import CadastrarImovelRequest


def event_to_request_dto(event: dict) -> CadastrarImovelRequest:
    body = event['body']
    request = CadastrarImovelRequest()
    request.rua = body['rua']
    request.estado = body['estado']
    request.bairro = body['bairro']
    request.cidade = body['cidade']
    return request
