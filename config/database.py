import pyodbc

def get_connection():

    conexion = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=INFORMATICA\\SQLEXPRESS;'
        'DATABASE=SIGH;'
        'Trusted_Connection=yes;'
    )

    return conexion