import os
import pymysql
from dotenv import load_dotenv
from openpyxl import Workbook
from openpyxl.styles import Font

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

select_query = """
SELECT 
    id,
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
FROM emp_info
"""

cursor.execute(select_query)
rows = cursor.fetchall()

columns = [
    "id",
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "educational_num",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "gender",
    "capital_gain",
    "capital_loss",
    "hours_per_week",
    "native_country",
    "income"
]

# Create Excel workbook
workbook = Workbook()
sheet = workbook.active
sheet.title = "Employee Data"

# Write header row
sheet.append(columns)

# Make header bold
for cell in sheet[1]:
    cell.font = Font(bold=True)

# Write database records
for row in rows:
    sheet.append(row)

# Auto-adjust column width
for column_cells in sheet.columns:
    max_length = 0
    column_letter = column_cells[0].column_letter

    for cell in column_cells:
        if cell.value is not None:
            max_length = max(max_length, len(str(cell.value)))

    sheet.column_dimensions[column_letter].width = max_length + 2

# Save Excel file
workbook.save("employee_output.xlsx")

print("Data exported successfully to employee_output.xlsx")

cursor.close()
connection.close()
