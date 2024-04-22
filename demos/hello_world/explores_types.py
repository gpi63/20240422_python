from typing import Any


def main() -> None:
    some_var: Any = "Hellow, World!"
    print(type(some_var))

    some_var = 42
    print(type(some_var))

    some_var = 42.0
    print(type(some_var))

    some_var = True
    print(type(some_var))

    some_var = None
    print(type(some_var))

    some_var = None
    print(type(some_var))

    def my_func() -> None:
        pass

    some_var = my_func
    print(type(some_var))

    class Person: ...

    some_var = Person
    print(type(some_var))

    num_str = "8"
    num = int(num_str)
    print(type(num))
    print(num)

    num_str = "8.5"
    num_float = float(num_str)
    print(type(num_float))
    print(num_float)


## code is only run if file is executed directly and not imported as a library
if __name__ == "__main__":
    main()
