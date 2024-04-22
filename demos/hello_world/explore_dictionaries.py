person = {
    "first_name": "Bob",
    "last_name": "Smith",
    "age": 23,
}

print(person["first_name"])
print(person["last_name"])
print(person["age"])

print(person)

### Udpate the value of an existing key pair
person["age"] = 24

### Adds a new key pair to dictionary
person["hair_colour"] = "brown"

print(person)

for key in person:
    print(key, person[key])

# try to access a key that does not exist, you will get a KeyError
try:
    print(person["middle_name"])
except KeyError:
    print("KeyError: middle_name")

### safely get a key that may not exist and define a default value if not found
print(person.get("middle_name", "Not Found"))

### remove a keypair
# del person["hair_colour"]

### delete dictionary
# person = None
