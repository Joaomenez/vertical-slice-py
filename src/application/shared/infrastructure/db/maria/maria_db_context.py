import mariadb
from maria_db_settings import MariaDbSettings


class MariaDbContext:
    __settings: MariaDbSettings

    def __init__(self, settings: MariaDbSettings) -> None:
        self.__settings = settings

    def get_connection(self):
        conn = None
        try:
            conn = mariadb.connect(
                user=self.__settings.user,
                password=self.__settings.password,
                host=self.__settings.host,
                port=self.__settings.port,
                database=self.__settings.database
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            raise e
        return conn.cursor()
