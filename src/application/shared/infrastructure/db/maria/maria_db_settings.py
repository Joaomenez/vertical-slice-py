class MariaDbSettings:
    user: str
    password: str
    host: str
    port: int
    database: str

    def __init__(self,
                 user: str,
                 password: str,
                 host: str,
                 port: int,
                 database:str) -> None:
        self.user = user
        self.password = password
        self.port = port
        self.host = host
        self.database = database