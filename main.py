from helper_functions import *
from database import conn

conn.autocommit = True
cursor = conn.cursor()

# create_database = "CREATE DATABASE Auto_Garage;"
# cursor.execute(create_database)

# Create Table
# create_table = """USE Auto_Garage
#                   CREATE TABLE Customers(
#                   CustomerID int IDENTITY(1,1) PRIMARY KEY,
#                   First_Name varchar(30),
#                   Last_Name varchar(30));"""
# cursor.execute(create_table)

test_insert = """
              USE Auto_Garage
              INSERT INTO Customers VALUES ('Jordan', 'Gopie');
              """

cursor.execute(test_insert)
cursor.close()
