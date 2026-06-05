import pyodbc

def get_connection():

    conexion = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-22LIJGK;'
        'DATABASE=borr;'
        'Trusted_Connection=yes;'
    )

    return conexion