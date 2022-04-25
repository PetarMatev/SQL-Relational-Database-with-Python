import mysql.connector
from mysql.connector import Error
import xlrd
from cleaner import create_table_cleaner, populate_table_cleaner
from guest import create_table_guest, populate_table_guest
from host import create_table_host, populate_table_host
from reservation import create_table_reservation, populate_table_reservation
from takes_apartment import create_table_takes_apartment, populate_table_takes_apartment
from database_queries import *


# Function to connect to our database:
def create_db_connection(host_name, user_name, user_password, auth_plugin, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            auth_plugin=auth_plugin,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


# Function to execute a query into our database:
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.executemany(query, my_list)  # cursor.execute(query) ор cursor.executemany(query, my_list)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


# Function to read a query from our database:
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


location = ("D:\\03_python\\python_projects\\mysql_database_connector\\rental_database\\rental_ERD.xls")
file_object = xlrd.open_workbook(location)
sheet = file_object.sheet_by_index(5)
sheet.cell_value(0, 0)

my_list = []

for i in range(1, 26):
    my_list.append(tuple(sheet.row_values(i)))

connection = create_db_connection("localhost", "root", "1234", "mysql_native_password", "rental")
results = read_query(connection, query_on_inner_joints_on_host_11)


for result in results:
    print(result)