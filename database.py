import pyodbc

conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};"
                      "Server=localhost;"
                      "Trusted_Connection=yes;"
                      "TrustServerCertificate=yes;")

