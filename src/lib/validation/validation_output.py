from lib.validation.validation_exception import ValidationException


class ValidationOutput:
    def __init__(self):
        self.__error_messages = []
        self.__messages = []
        self.__isvalid = False

    def add_var_type_error_message(self, var, var_name: str, expected_type: str):
        self.__error_messages.append(f'[ {var_name} + "] o tipo esperado e {expected_type}, mas foi informado um valor do tipo {type(var)}')
        self.__isvalid = True
        # else:
        #     raise Exception("invalid argument")
   
    def add__message(self, message: str):
        if isinstance(message, str):
            self.__messages.append(message)
        else:
            raise ValidationException("invalid argument")
    
    def get_isvalid(self) -> bool:
        return self.__isvalid
    
    def get_error_messages(self) -> list[str]:
        return self.__error_messages
    
    def get_messages(self) -> list[str]:
        return self.__messages