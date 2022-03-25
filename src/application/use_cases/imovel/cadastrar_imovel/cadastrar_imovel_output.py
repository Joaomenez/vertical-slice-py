class CadastrarImovelOutput:
    id: str
    status: bool
    status_message: str

    def __init__(self, id: int, status: bool, status_message: str = ""):
        self.id = id
        self.status = status
        self.status_message = status_message
