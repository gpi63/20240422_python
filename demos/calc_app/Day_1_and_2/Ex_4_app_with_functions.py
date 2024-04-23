from typing import Any


def add_hist(cmdhistory: Any, idvalue: int, command: str, value: Any) -> None:
    cmdhistory.append({"id": idvalue, "command": command, "value": value})


def domath(a: int | float, b: int, command: str) -> Any:
    if command == "add":
        return a + b
    elif command == "subtract":
        return a - b
    elif command == "multiply":
        return a * b
    elif command == "divide":
        return a / b


def get_item(prompt: str) -> int:
    return int(input(prompt + ": "))


def main() -> None:
    ### setup a base number to work from
    constant: int | float = 0
    idvalue = 0
    cmdhistory: list[dict[str, Any]] = []

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
            or command == "history"
            or command == "remove"
            or command == "exit"
        ):
            ## echo back the comamnd
            print(f"Received command: {command}")
            idvalue += 1

            ## restet the constant back to 0, no number need be input
            if command == "clear":
                print("I'm restiing the result to 0")
                constant = 0
                print(f"the result is {constant}")
                cmdhistory.clear

            elif command == "history":
                print("Showing History")
                add_hist(cmdhistory, idvalue, command, "")
                for action in cmdhistory:
                    print(action["id"], action["command"], action["value"])

            elif command == "remove":
                removeitem = get_item("What item do you want removed")
                print(f"removing item {removeitem}")
                for entry in cmdhistory:
                    if entry["id"] == removeitem:
                        cmdhistory.remove(entry)

            ## If exit entered break the loop
            elif command == "exit":
                break

            else:
                numberinput = get_item("Please enter an operand")
                if command == "add":
                    print(f"I'm adding {constant} to {numberinput}")
                    constant = domath(constant, numberinput, command)
                    print(f"the result is {constant}")
                    add_hist(cmdhistory, idvalue, command, numberinput)

                elif command == "subtract":
                    print(f"I'm subtracting {constant} from {numberinput}")
                    constant = domath(constant, numberinput, command)
                    print(f"the result is {constant}")
                    add_hist(cmdhistory, idvalue, command, numberinput)

                elif command == "multiply":
                    print(f"I'm multiplying {constant} with {numberinput}")
                    constant = domath(constant, numberinput, command)
                    print(f"the result is {constant}")
                    add_hist(cmdhistory, idvalue, command, numberinput)

                elif command == "divide":
                    print(f"I'm dividing {constant} by {numberinput}")
                    constant = domath(constant, numberinput, command)
                    print(f"the result is {constant}")
                    add_hist(cmdhistory, idvalue, command, numberinput)

        else:
            ### if command not reccognised tell them
            print(f"Unknow command - {command} - please retry")


## code is only run if file is executed directly and not imported as a library
if __name__ == "__main__":
    main()
