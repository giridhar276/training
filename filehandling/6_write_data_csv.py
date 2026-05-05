

import csv

# Sample employee data
employees = [
    ["id", "name", "department", "salary"],
    [1, "Ravi", "IT", 50000],
    [2, "Sita", "HR", 45000],
    [3, "Kiran", "Finance", 60000]
]

# Open file in write mode
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write all rows into CSV
    writer.writerows(employees)

print("CSV file created successfully")