import mysql.connector
from mysql.connector import Error

# Replace these with your actual database credentials
db_config = {
    'host': 'localhost',
    'database': 'sql_store',
    'user': 'dci-student',
    'password': 'Dci1234!'
}

# JSON data
stock = [
   
   {
      "state":"Cheap",
      "category":"Headphones",
      "warehouse":1,
      "date_of_stock":"2019-12-23 05:45:18"
   },
   {
      "state":"Cheap",
      "category":"Monitor",
      "warehouse":1,
      "date_of_stock":"2021-06-17 15:11:42"
   },
   {
      "state":"Cheap",
      "category":"Router",
      "warehouse":2,
      "date_of_stock":"2022-02-04 17:55:19"
   },
   {
      "state":"Almost new",
      "category":"Keyboard",
      "warehouse":1,
      "date_of_stock":"2022-08-08 02:46:35"
   },
   {
      "state":"Almost new",
      "category":"Mouse",
      "warehouse":2,
      "date_of_stock":"2021-08-28 12:41:07"
   },
   {
      "state":"High quality",
      "category":"Tablet",
      "warehouse":1,
      "date_of_stock":"2021-03-17 06:34:07"
   },
   {
      "state":"Cheap",
      "category":"Laptop",
      "warehouse":2,
      "date_of_stock":"2020-11-11 18:50:10"
   },
   {
      "state":"Brand new",
      "category":"Tablet",
      "warehouse":2,
      "date_of_stock":"2020-07-10 17:58:08"
   },
   {
      "state":"Elegant",
      "category":"Mouse",
      "warehouse":1,
      "date_of_stock":"2022-04-03 16:05:11"
   },
   {
      "state":"Elegant",
      "category":"Headphones",
      "warehouse":2,
      "date_of_stock":"2020-01-08 23:59:58"
   },
   {
      "state":"Almost new",
      "category":"Headphones",
      "warehouse":1,
      "date_of_stock":"2023-02-14 17:39:16"
   },
   {
      "state":"Almost new",
      "category":"Smartphone",
      "warehouse":1,
      "date_of_stock":"2019-12-12 05:35:45"
   },
   {
      "state":"Second hand",
      "category":"Monitor",
      "warehouse":1,
      "date_of_stock":"2021-04-30 05:23:35"
   },
   {
      "state":"Cheap",
      "category":"Keyboard",
      "warehouse":2,
      "date_of_stock":"2020-05-06 22:31:19"
   },
   {
      "state":"Cheap",
      "category":"Mouse",
      "warehouse":2,
      "date_of_stock":"2021-04-21 22:56:05"
   },
   {
      "state":"Brand new",
      "category":"Router",
      "warehouse":1,
      "date_of_stock":"2022-08-12 15:21:21"
   },
   {
      "state":"Brand new",
      "category":"Tablet",
      "warehouse":1,
      "date_of_stock":"2019-09-27 16:41:07"
   },
   {
      "state":"Exceptional",
      "category":"Headphones",
      "warehouse":2,
      "date_of_stock":"2021-09-08 03:15:57"
   },
   {
      "state":"Brand new",
      "category":"Smartphone",
      "warehouse":1,
      "date_of_stock":"2021-12-25 18:28:53"
   },
   {
      "state":"Almost new",
      "category":"Headphones",
      "warehouse":2,
      "date_of_stock":"2021-07-12 15:06:53"
   }
]


# Function to create a connection to MySQL
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print(f'Connected to MySQL Server version {connection.get_server_info()}')
            return connection
    except Error as e:
        print(f'Error: {e}')
    return None

# Function to create the stock table
def create_stock_table(connection):
    try:
        cursor = connection.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS stock (
            id INT AUTO_INCREMENT PRIMARY KEY,
            state VARCHAR(255) NOT NULL,
            category VARCHAR(255) NOT NULL,
            warehouse INT NOT NULL,
            date_of_stock DATETIME NOT NULL
        )
        '''
        cursor.execute(create_table_query)
        connection.commit()
        print('Stock table created successfully.')
    except Error as e:
        print(f'Error: {e}')

# Function to insert data into the stock table
def insert_stock_data(connection, stock_data):
    try:
        cursor = connection.cursor()
        insert_query = '''
        INSERT INTO stock (state, category, warehouse, date_of_stock)
        VALUES (%s, %s, %s, %s)
        '''
        cursor.executemany(insert_query, stock_data)
        connection.commit()
        print(f'{cursor.rowcount} rows inserted into stock table.')
    except Error as e:
        print(f'Error: {e}')

# Main program
try:
    # Create a connection to MySQL
    connection = create_connection()

    if connection:
        # Create the stock table
        create_stock_table(connection)

        # Insert data into the stock table
        insert_stock_data(connection, [(item['state'], item['category'], item['warehouse'], item['date_of_stock']) for item in stock])
        
except Error as e:
    print(f'Error: {e}')

finally:
    # Close the connection
    if connection and connection.is_connected():
        connection.close()
        print('MySQL connection closed.')
