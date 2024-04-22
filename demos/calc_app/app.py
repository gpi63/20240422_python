def main() -> None:
    ### setup a base number to work from
    constant: int | float = 0

    ### Loop around to get imputs until exit called
    while True:
        ### get a inout form the user
        command = (input("Enter a command: ")).lower()

        ###  Acts on the input if one of the predefined actions used
        if (
            command == "add"
            or command == "subtract"
            or command == "multiply"
            or command == "divide"
            or command == "clear"
        ):
            ## echo back the comamnd
            print(f"Received command: {command}")

            ## restet the constant back to 0, no number need be input
            if command == "clear":
                print("I'm restiing the result to 0")
                constant = 0
                print(f"the result is {constant}")
            else:
                numberinput = input("Please enter an operand: ")
                if command == "add":
                    print(f"I'm adding {constant} to {numberinput}")
                    constant = constant + int(numberinput)
                    print(f"the result is {constant}")
                elif command == "subtract":
                    print(f"I'm subtracting {constant} from {numberinput}")
                    constant = constant - int(numberinput)
                    print(f"the result is {constant}")
                elif command == "multiply":
                    print(f"I'm multiplying {constant} with {numberinput}")
                    constant = constant * int(numberinput)
                    print(f"the result is {constant}")
                elif command == "divide":
                    print(f"I'm dividing {constant} by {numberinput}")
                    constant = constant / int(numberinput)
                    print(f"the result is {constant}")
        else:
            ### if command not reccognised tell them
            print(f"Unknow command - {command} - please retry")

        ## If no command entered break the loop
        if command == "exit":
            break


## code is only run if file is executed directly and not imported as a library
if __name__ == "__main__":
    main()
