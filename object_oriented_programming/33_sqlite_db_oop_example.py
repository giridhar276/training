# 33. OOP with SQLite Database
# This example creates a database, table, inserts records, and reads records.
# SQLite is used because it works without installing MySQL server.

import sqlite3

class EmployeeDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                department TEXT,
                salary REAL
            )
        """)
        self.connection.commit()
        print("Table created successfully")

    def insert_employee(self, name, department, salary):
        self.cursor.execute(
            "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
            (name, department, salary)
        )
        self.connection.commit()
        print("Employee inserted successfully")

    def show_employees(self):
        self.cursor.execute("SELECT * FROM employees")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def close(self):
        self.connection.close()
        print("Database connection closed")

# Usage
emp_db = EmployeeDB("employees.db")
emp_db.create_table()
emp_db.insert_employee("Ravi", "IT", 50000)
emp_db.insert_employee("Priya", "HR", 45000)
emp_db.show_employees()
emp_db.close()
