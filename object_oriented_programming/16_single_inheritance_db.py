

import pymysql


# Parent class
# This class contains common database connection logic
class MySQLDatabase:
    def __init__(self, host, user, password, database, port=3306):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )

        self.cursor = self.connection.cursor()
        print("Database connected successfully")

    def commit_changes(self):
        self.connection.commit()
        print("Changes committed successfully")

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        print("Database connection closed")


# Child class
# EmployeeDB inherits database connection features from MySQLDatabase
class EmployeeDB(MySQLDatabase):

    def create_employee_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS employees_oop (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100),
            salary FLOAT
        )
        """

        self.cursor.execute(query)
        self.commit_changes()
        print("Employee table created successfully")

    def insert_employee(self, name, department, salary):
        query = """
        INSERT INTO employees_oop (name, department, salary)
        VALUES (%s, %s, %s)
        """

        self.cursor.execute(query, (name, department, salary))
        self.commit_changes()
        print("Employee inserted successfully")

    def display_employees(self):
        query = "SELECT * FROM employees_oop"

        self.cursor.execute(query)

        employees = self.cursor.fetchall()

        print("\nEmployee Records:")
        for employee in employees:
            print(employee)

    def update_employee_salary(self, employee_id, new_salary):
        query = """
        UPDATE employees_oop
        SET salary = %s
        WHERE id = %s
        """

        self.cursor.execute(query, (new_salary, employee_id))
        self.commit_changes()
        print("Employee salary updated successfully")

    def delete_employee(self, employee_id):
        query = """
        DELETE FROM employees_oop
        WHERE id = %s
        """

        self.cursor.execute(query, (employee_id,))
        self.commit_changes()
        print("Employee deleted successfully")


# Usage
# Make sure employee_db database already exists in MySQL

db = EmployeeDB(
    host="localhost",
    user="root",
    password="your_password",
    database="employee_db"
)

db.create_employee_table()

db.insert_employee("Kiran", "Finance", 60000)
db.insert_employee("Ravi", "IT", 75000)
db.insert_employee("Anita", "HR", 55000)

db.display_employees()

db.update_employee_salary(1, 70000)

db.display_employees()

db.delete_employee(2)

db.display_employees()

db.close_connection()



'''
Without inheritance, you may write database connection code again and again:

EmployeeDB has connection code
DepartmentDB has connection code
ProductDB has connection code
CustomerDB has connection code

With inheritance:

MySQLDatabase has connection code once
EmployeeDB reuses it
DepartmentDB reuses it
ProductDB reuses it
CustomerDB reuses it

So inheritance helps in:

Code reusability
Cleaner structure
Less duplicate code
Easy maintenance
Real-time project organization

'''