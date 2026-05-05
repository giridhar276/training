

import json

student = {
    "name": "Ravi",
    "age": 25,
    "skills": ["Python", "SQL", "Machine Learning"],
    "is_active": True
}

# Write dictionary into JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully")