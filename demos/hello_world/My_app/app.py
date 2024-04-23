from lib import add, subtract


def main() -> None:  ### ('-> None' means no return)
    result = add(1, subtract(3, 7))
    print(result)


## code is only run if file is executed directly and not imported as a library
if __name__ == "__main__":
    main()
