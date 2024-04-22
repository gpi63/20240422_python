def main() -> None:
    while True:
        ## get a inout form the user
        command = input("Enter a command: ")

        if command == "exit":
            break

        print(f"Received command: {command}")


## code is only run if file is executed directly and not imported as a library
if __name__ == "__main__":
    main()
