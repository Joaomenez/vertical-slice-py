from lib.validation.base_validator import BaseValidator


class InputValidator(BaseValidator):

    def __init__(self):
        super().__init__()

    def create_rules(self, input):
        super().rule_for(input.age, 'age')\
            .int_()\
            .grater_or_equal_than(18)

        super().rule_for(input.name, 'name')\
            .str_()\
            .includes("joao")
    
    def validate(self, input):
        self.create_rules(input)
        return super().validate()
