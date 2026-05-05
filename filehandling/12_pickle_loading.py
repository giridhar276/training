

import pickle

# rb means read binary
with open("employee.pkl", "rb") as file:
    data = pickle.load(file)

print(data)
print("Employee name:", data["name"])