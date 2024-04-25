from pathlib import Path
import csv


def write_csv() -> None:
    names_file_path = Path("names.csv")
    with names_file_path.open("w", encoding="UTF-8") as names_file:
        names_csv_write = csv.writer(names_file, delimiter=",")
        names_csv_write.writerow(["first_name", "last_name"])
        names_csv_write.writerow(["Bob", "Smith"])
        names_csv_write.writerow(["Alicae", "Springs"])
        names_csv_write.writerow(["Jim", "Timmons"])
        names_csv_write.writerow(["Sally", "Wakefield"])


def read_csv() -> None:
    names_file_path = Path("names.csv")
    with names_file_path.open("r", encoding="UTF-8") as names_file:
        names_csv_reader = csv.reader(names_file, delimiter=",")

        next(names_csv_reader)

        for name_row in names_csv_reader:
            print(name_row)


def write_csv_dic() -> None:
    names_file_path = Path("names_dic.csv")
    field_names = ["first_name", "last_name"]
    with names_file_path.open("w", encoding="UTF-8") as names_file:
        names_csv_write = csv.DictWriter(
            names_file, fieldnames=field_names, delimiter="\t"
        )
        names_csv_write.writeheader()
        names_csv_write.writerow({"first_name": "Bob", "last_name": "Smith"})
        names_csv_write.writerow(
            {"first_name": "Alice", "last_name": "Springs"}
        )
        names_csv_write.writerow({"first_name": "Jim", "last_name": "Timmons"})
        names_csv_write.writerow(
            {"first_name": "Sally", "last_name": "Wakefield"}
        )


def read_csv_dic() -> None:
    names_file_path = Path("names_dic.csv")
    field_names = ["first_name", "last_name"]
    with names_file_path.open("r", encoding="UTF-8") as names_file:
        names_csv_dict_reader = csv.DictReader(names_file, delimiter="\t")

        for names_row in names_csv_dict_reader:
            print(names_row)


def main() -> None:
    read_csv_dic()


if __name__ == "__main__":
    main()
