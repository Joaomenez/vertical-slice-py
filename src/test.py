from input import Input
from input_validator import InputValidator
from lib.validation.base_validator import BaseValidator
from lib.validation.validator_decorator import validator

x = ["aa", "cdw"]
y = 2


input_ = Input()

valid = InputValidator().validate(input_)


print(valid)

# @validator
# def lambda_handler(x,z):
#     return {
#         "statusCode": 200,
#         "headers": {
#             "Content-Type": "application/json"
#         },
#         "body":{"message": "hello-world"}
#     }


# lambda_handler(x,y)