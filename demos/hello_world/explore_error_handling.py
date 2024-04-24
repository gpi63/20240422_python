import logging

logging.basicConfig(level=logging.INFO)

# logging.debug("This is a debug mesage")
# logging.info("This is an ingo message")
# logging.warning("This is an warning message")
# logging.error("This is an error message")
# logging.critical("This is an critical message")


class CalcAppDivideByZeroError(Exception): ...


def divide(x: float, y: float) -> float:
    if y == 0:
        raise CalcAppDivideByZeroError("Calc app cannot divide by zero")
    return x / y


# def do_it() -> None:
#     ##raise FileNotFoundError("File no found")
#     num = int("k")
#     print(num)


def main() -> None:
    # try:
    #     do_it()
    # except ValueError as e:
    #     logging.error(f"Value Error: {e}")
    # except Exception as e:
    #     logging.error(f"General Error: {e}")
    try:
        result = divide(1, 0)
        print(result)
    except CalcAppDivideByZeroError as e:
        logging.error(f"Calc App Divide By Zero Error: {e}")
    # more general purpose error to catch anything unexpected
    except Exception as e:
        logging.error(f"General Purpose Error: {e}")


if __name__ == "__main__":
    main()
