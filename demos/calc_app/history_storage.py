import json

from history import History


class HistoryStorage:
    def __init__(self, history: History) -> None:
        self.__history = history

    def save_history(self, history_file) -> None:
        with open(history_file, "w") as file:
            json.dump(list(self.__history), file)

    def load_history(self, history_file) -> None:
        with open(history_file, "r") as file:
            self.__history.bulk_import(json.load(file))
