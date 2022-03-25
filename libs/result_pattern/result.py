from typing import Generic, TypeVar

T = TypeVar("T")


class Result(Generic[T]):
    __result: T

    def __init__(self):
        self.__result = None
        self.__isvalid = True
        self.__messages = []
        self.__error_messages = []

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, result: T) -> None:
        self.__result = result

    @property
    def isvalid(self) -> bool:
        return self.__isvalid

    @property
    def messages(self) -> list:
        return self.__messages

    @property
    def error_messages(self) -> list:
        return self.__error_messages

    def add_error_message(self, error_message: str) -> None:
        self.__isvalid = False
        self.__error_messages.append(error_message)

    def add_error_messages(self, error_messages: list[str]) -> None:
        self.__isvalid = False
        self.__error_messages = [*self.__error_messages, *error_messages]
