from __future__ import annotations
from typing import Any
from validation_output import ValidationOutput
from rule import Rule


class BaseValidator:
    def __init__(self):
        self.rules: list[Rule] = []

    def rule_for(self, arg: Any, name_arg: str):
        new_rule = Rule(arg, name_arg)
        self.rules.append(new_rule)
        return new_rule

    def _validate(self) -> ValidationOutput:
        validation_output = ValidationOutput()
        for rule in self.rules:
            output = rule.validate()
            if output is not None:
                validation_output.add_error(output)
        return validation_output
