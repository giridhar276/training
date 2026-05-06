import csv
import pymysql

# Step 1: Connect to employee_db database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="employee_db"
)

cursor = connection.cursor()

# Step 2: Prepare insert query
insert_query = """
INSERT INTO emp_info (
    age,
    workclass,
    fnlwgt,
    education,
    educational_num,
    marital_status,
    occupation,
    relationship,
    race,
    gender,
    capital_gain,
    capital_loss,
    hours_per_week,
    native_country,
    income
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

records = []

# Step 3: Read records from empinfo.csv
with open("empinfo.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        record = (
            int(row["age"]),
            row["workclass"].strip(),
            int(row["fnlwgt"]),
            row["education"].strip(),
            int(row["educational-num"]),
            row["marital-status"].strip(),
            row["occupation"].strip(),
            row["relationship"].strip(),
            row["race"].strip(),
            row["gender"].strip(),
            int(row["capital-gain"]),
            int(row["capital-loss"]),
            int(row["hours-per-week"]),
            row["native-country"].strip(),
            row["income"].strip()
        )

        records.append(record)

# Step 4: Insert all records into MySQL
cursor.executemany(insert_query, records)

# Step 5: Commit changes
connection.commit()

print(cursor.rowcount, "records inserted successfully.")

# Step 6: Close resources
cursor.close()
connection.close()
