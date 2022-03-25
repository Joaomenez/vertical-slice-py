from imovel_data_insert import ImovelDataInsert


def insert_query(data: ImovelDataInsert) -> tuple:
    query = "INSERT INTO IMOVEL " \
            "(BAIRRO, RUA, ESTADO)" \
            " Values (?,?,?)"
    params = (data.bairro, data.rua, data.estado)
    return query, params
