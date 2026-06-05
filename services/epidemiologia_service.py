from config.database import get_connection

def obtener_epidemiologia():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT enfermedad, SUM(cantidad_casos) AS total_casos
        FROM Epidemiologia
        GROUP BY enfermedad
    """)
    resumen = cursor.fetchall()

    cursor.execute("""
        SELECT enfermedad, cantidad_casos, area, fecha_registro, observacion
        FROM Epidemiologia
        ORDER BY fecha_registro DESC
    """)
    casos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return {
        "resumen": resumen,
        "casos": casos
    }