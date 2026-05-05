

import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print("Name:", data["name"])
print("Skills:", data["skills"])