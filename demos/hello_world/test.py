import re

input_string = "add 5"
pattern = r"(add|subtract|multiply|divide|remove|load|save) (\d+)"

match = re.match(pattern, input_string)
if match:
    operation = match.group(1)
    number = int(match.group(2))
    print(f"command: {operation}")
    print(f"operand: {number}")
else:
    print("No match found.")
