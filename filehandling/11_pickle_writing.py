

import pickle

employee = {
    "id": 101,
    "name": "Ravi",
    "department": "IT",
    "salary": 50000
}

# wb means write binary
with open("employee.pkl", "wb") as file:
    pickle.dump(employee, file)

print("Pickle file created successfully")