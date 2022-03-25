from src.application.shared.infrastructure.db.maria.maria_db_context import MariaDbContext
from imovel_data_insert import ImovelDataInsert
import cadastrar_imovel_queries as queries


class CadastrarImovelRepository:
    __context: MariaDbContext

    def __init__(self, context: MariaDbContext) -> None:
        self.__context = context

    def insert(self, data: ImovelDataInsert) -> bool:
        try:
            conn = self.__context.get_connection()
            query = queries.insert_query(data)
            conn.execute( query[0], query[1])
            return True
        except Exception as e:
            print(e)
            return False
