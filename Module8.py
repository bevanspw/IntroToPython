import pandas as pd
import pyodbc

connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=pragmaticworks.database.windows.net;DATABASE=Demo;UID=DemoUser;PWD=DemoPW123'
connection = pyodbc.connect(connection_string)

df = pd.read_sql_query('SELECT * FROM [dbo].[VetClinic]', connection)

print(df)
