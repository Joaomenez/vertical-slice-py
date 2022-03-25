class ValidationRuleOutput:
    argument: str
    errors: list

    def __init__(self, argument: str, errors: list):
        self.argument = argument
        self.errors = errors

    def to_list_with_argument_and_error_message(self):
        list_errors = []
        for error in self.errors:
            list_errors.append(f'{self.argument}: {error}')
        return list_errors
