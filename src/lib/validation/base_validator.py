from __future__ import annotations
from typing import Any

from lib.validation.rule import Rule



class BaseValidator:
    def __init__(self):
        self.rules = []
    
    def rule_for(self, arg: Any, name_arg: str):
        new_rule = Rule(arg, name_arg)
        self.rules.append(new_rule)
        return new_rule


    def validate(self):
        validation_outputs = []
        for rule in self.rules:
            output = rule.validate()
            if output != None:
                validation_outputs.append(output)
        return validation_outputs