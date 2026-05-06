# 34. OOP with PyMySQL Database
# This example shows how to structure MySQL logic using a class.
# Update credentials before running.

import pymysql

class MySQLEmployeeDB:
    def __init__(self, host, user, password, database, port=3306):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS employees_oop (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100),
            salary FLOAT
        )
        """
        self.cursor.execute(query)
        print("Table created successfully")

    def insert_employee(self, name, department, salary):
        query = "INSERT INTO employees_oop (name, department, salary) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (name, department, salary))
        self.connection.commit()
        print("Employee inserted successfully")

    def display_employees(self):
        self.cursor.execute("SELECT * FROM employees_oop")
        for row in self.cursor.fetchall():
            print(row)

    def close(self):
        self.cursor.close()
        self.connection.close()
        print("Connection closed")

# Usage
# Make sure the database already exists before running this script.
db = MySQLEmployeeDB("localhost", "root", "your_password", "employee_db")
db.create_table()
db.insert_employee("Kiran", "Finance", 60000)
db.display_employees()
db.close()

print("Uncomment the usage section after updating MySQL credentials.")
