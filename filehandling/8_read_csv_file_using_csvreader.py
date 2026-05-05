

import csv

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["department"], row["salary"])