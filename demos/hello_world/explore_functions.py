def num_input(prompt: str) -> int:
    return int(input(prompt))


def sum_numbers(a: int, b: int) -> int:
    return a + b


def main() -> None:  ### ('-> None' means no return)
    num1 = num_input("Enter a number: ")
    num2 = num_input("Enter another number: ")
    print(f"Sum: {sum_numbers(num1, num2)}")


## code is only run if file is executed directly and not imported as a library
if __name__ == "__main__":
    main()
