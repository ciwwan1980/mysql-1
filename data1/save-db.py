import os
from dotenv import load_dotenv
import mysql.connector

# Load environment variables from .env file
load_dotenv()

# Replace these values with your MySQL connection details
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Create a connection to the MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)
# Create a cursor object to interact with the database
cursor = connection.cursor()

# Replace 'your_database' with the desired database name
database_name = 'ajil_db1'

# Create the database
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

# Use the specified database
cursor.execute(f"USE {database_name}")

# Create a more complex table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        birth_date DATE,
        hire_date DATE,
        salary DECIMAL(10, 2)
    )
""")

# Insert more sample data
data = [
    ('John', 'Doe', '1990-01-15', '2021-05-10', 50000.00),
    ('Johnn', 'Doee', '1990-01-15', '2021-05-10', 630000.00),
    ('Alice', 'Smith', '1985-08-22', '2022-01-20', 60000.00),
    ('Bob', 'Johnson', '1988-04-30', '2020-11-05', 55000.00),
    ('ciwan', 'Johnson', '1988-04-30', '2020-11-05', 55000.00)
]

cursor.executemany("""
    INSERT INTO employees 
    (first_name, last_name, birth_date, hire_date, salary) 
    VALUES (%s, %s, %s, %s, %s)
""", data)

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
