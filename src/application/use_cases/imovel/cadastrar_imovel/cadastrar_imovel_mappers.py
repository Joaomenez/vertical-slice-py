from cadastrar_imovel_input import CadastrarImovelInput
from data.imovel_data_insert import ImovelDataInsert


def input_to_db_insert_data(inp: CadastrarImovelInput) -> ImovelDataInsert:
    input_db = ImovelDataInsert(
        rua=inp.rua,
        bairro= inp.bairro,
        cidade=inp.cidade,
        estado=inp.estado,
        numero=inp.numero
    )
    return input_db

