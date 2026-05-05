

import csv

# Process large CSV file row by row
# For big CSV files, process row by row instead of loading the full file.


def process_large_csv(file_path):
    total_salary = 0
    employee_count = 0

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Convert salary from string to integer
            salary = int(row["salary"])

            total_salary += salary
            employee_count += 1

    average_salary = total_salary / employee_count

    print("Total employees:", employee_count)
    print("Average salary:", average_salary)


process_large_csv("employees.csv")