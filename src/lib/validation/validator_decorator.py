
def validator(func):
    def validate(*args, **kargs):
        print("1 - test decorator")
        func(*args, **kargs)
        print("2 - test decorator")
    return validate
