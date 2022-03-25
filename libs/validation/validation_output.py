from validation_rule_output import ValidationRuleOutput


class ValidationOutput:
    def __init__(self):
        self.__isvalid = True
        self.__errors: list[ValidationRuleOutput] = []

    @property
    def isvalid(self):
        return self.__isvalid

    @property
    def errors(self) -> list[ValidationRuleOutput]:
        return self.__errors

    def to_error_messages(self) -> list[str]:
        return [error.to_list_with_argument_and_error_message()
                for error in self.__errors]

    def add_error(self, error: ValidationRuleOutput):
        self.__isvalid = False
        self.__errors.append(error)
