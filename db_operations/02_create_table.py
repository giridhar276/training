import os
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

# Create table based on empinfo.csv structure
create_table_query = """
CREATE TABLE IF NOT EXISTS emp_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    workclass VARCHAR(100),
    fnlwgt INT,
    education VARCHAR(100),
    educational_num INT,
    marital_status VARCHAR(100),
    occupation VARCHAR(100),
    relationship VARCHAR(100),
    race VARCHAR(100),
    gender VARCHAR(20),
    capital_gain INT,
    capital_loss INT,
    hours_per_week INT,
    native_country VARCHAR(100),
    income VARCHAR(50)
)
"""

cursor.execute(create_table_query)

print("Table 'emp_info' created successfully.")

cursor.close()
connection.close()
