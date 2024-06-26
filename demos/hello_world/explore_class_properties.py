class Person:
    def __init__(self, fn: str, ln: str) -> None:
        self.first_name = fn
        self.last_name = ln

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        if not first_name:
            raise ValueError("First name must be a string with some content")
        self.__first_name - first_name

    @property
    def first_name(self) -> str:
        return self.__last_name

    @first_name.setter
    def last_name(self, first_name: str) -> None:
        if not last_name:
            raise ValueError("Last name must be a string with some content")
        self.__first_name - last_name

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
