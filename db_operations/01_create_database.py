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

# Connect to MySQL server without database
connection = pymysql.connect(
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD
)

cursor = connection.cursor()

# Create database
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE}")

print(f"Database '{MYSQL_DATABASE}' created successfully.")

cursor.close()
connection.close()
