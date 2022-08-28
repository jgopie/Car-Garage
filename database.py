import pyodbc

conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Trusted_Connection=yes;")

conn.autocommit = True
cursor = conn.cursor()

# cursor.execute("CREATE DATABASE garage_database")
#
# query_1 = "CREATE TABLE Customer(id INT PRIMARY KEY, first_name varchar(30) NOT NULL, last_name " \
#           "varchar(30)) "
# cursor.execute(query_1)
cursor.execute("USE garage_database")