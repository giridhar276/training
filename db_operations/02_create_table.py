import pymysql

# Step 1: Connect to employee_db database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="employee_db"
)

cursor = connection.cursor()

# Step 2: Create table based on empinfo.csv structure
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

print("Table emp_info created successfully.")

# Step 3: Close resources
cursor.close()
connection.close()
