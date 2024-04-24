import json

people_dict = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Amy", "age": 20, "city": "London"},
    {"name": "Sri", "age": 40, "city": "Hyderabad"},
]


class Person:
    def __init__(self, name: str, age: int, city: str) -> None:
        self.name = name
        self.age = age
        self.city = city


people_obj = [
    Person("John", 30, "New York"),
    Person("Amy", 20, "London"),
    Person("Sri", 40, "Hyderabad"),
]


def main() -> None:
    ### 'with' statment, files closes file when done
    with open("data.json", "w") as file:
        # json.dump(people_dict, file)
        json.dump([p.__dict__ for p in people_obj], file)

    with open("data.json", "r") as file:
        people2 = json.load(file)
        # print(person2)
        print([Person(p["name"], p["age"], p["city"]) for p in people2])


if __name__ == "__main__":
    main()

################### my attempt
# import json

# people_dict = [
#     {"name": "John", "age": 30, "city": "New York"},
#     {"name": "Amy", "age": 20, "city": "London"},
#     {"name": "Sri", "age": 40, "city": "Hyderabad"},
# ]


# class Person:
#     def __init__(self, name: str, age: int, city: str) -> None:
#         self.name = name
#         self.age = age
#         self.city = city


# people_obj = [
#     Person("John", 30, "New York"),
#     Person("Amy", 20, "London"),
#     Person("Sri", 40, "Hyderabad"),
# ]


# def main() -> None:
#     with open("data.json", "w") as file:
#         json.dump(people_dict, file)


# with open("data.json", "r") as file:
#     person2 = json.load(file)
#     print(person2)


# if __name__ == "__main__":
#     main()
