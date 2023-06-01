import pyodbc
import pandas as pd

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-R6JITBG;"
            "Database=LIBTNB;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()

cursor.execute('''CREATE TABLE table_name (
    PersonID int,
    LastName varchar(255));'''
               )

cnxn.commit()

# data = pd.read_sql("SELECT TOP(100) * FROM associates", cnxn)
cnxn.close()