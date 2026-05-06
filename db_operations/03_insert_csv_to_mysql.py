import os
import csv
import pymysql
from dotenv import load_dotenv

# Load values from .env file
load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

# Connect to MySQL database
connection = pymysql.connect(
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)

cursor = connection.cursor()

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

# Read records from empinfo.csv
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

# Insert all records into MySQL
cursor.executemany(insert_query, records)
connection.commit()

print(cursor.rowcount, "records inserted successfully.")

cursor.close()
connection.close()
