import pymysql

# Step 1: Connect to MySQL server
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="your_mysql_password"
)

cursor = connection.cursor()

# Step 2: Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS employee_db")

print("Database created successfully.")

# Step 3: Close resources
cursor.close()
connection.close()
