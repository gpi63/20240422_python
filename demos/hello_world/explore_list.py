from typing import Any

nums: list[int] = [1, 2, 3, 4, 5]

letters: list[str] = ["a", "b", "c", "d", "e"]

people: list[dict[str, Any]] = [
    {"name": "Bob", "age": 23},
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 27},
]

for person in people:
    print(person["name"], person["age"])

# add a new dictionary to the list
people.append({"name": "David", "age": 29, "hair_color": "brown"})

for person in people:
    print(person["name"], person["age"])

for i in range(len(nums)):
    print(nums[i], letters[i])
