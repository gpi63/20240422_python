### seeing if sync will work
from typing import Protocol
from user_input import get_command, get_operand, get_entry_id
from user_output import (
    HistoryConsoleReporter,
    HistoryFileReporter,
    print_invalid_command,
    print_result,
    print_error,
)
from calculator import calculator_result, calc_fns
from history_obj import HistoryObj
from history_dict import HistoryDict
from history import History


class CalculatorTool:
    def __init__(self, history: History):
        self.history = history

    def run(self) -> None:
        while True:
            command = get_command()

            if command in calc_fns:
                operand = get_operand()
                if command == "divide" and operand == 0:
                    print_error("Cannot divide by zero")
                    continue
                self.history.append_history_entry(command, operand)
            elif command == "history":
                HistoryConsoleReporter(self.history).print_history_entries()
                HistoryFileReporter(
                    self.history, "entries.txt"
                ).print_history_entries()
            elif command == "remove":
                self.history.remove_history_entry(get_entry_id())
            elif command == "clear":
                self.history.clear_history_entries()
            elif command == "exit":
                return
            else:
                print_invalid_command(command)
                continue

            print_result(calculator_result(self.history))


def main() -> None:
    history = HistoryObj()
    calculator_tool = CalculatorTool(history)
    calculator_tool.run()


if __name__ == "__main__":
    main()