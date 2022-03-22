from lib.validation.validator_decorator import validator


@validator
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body":{"message": "hello-world"}
    }