from config.database import get_connection

def obtener_indicadores():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM Camas WHERE estado = 'Disponible'")
    camas_disponibles = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Camas WHERE estado = 'Ocupada'")
    camas_ocupadas = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE estado = 'Hospitalizado'")
    pacientes_hospitalizados = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM AltasMedicas")
    altas_medicas = cursor.fetchone()[0]

    cursor.execute("""
        SELECT codigo_cama, area, estado
        FROM Camas
    """)
    camas = cursor.fetchall()

    cursor.execute("""
        SELECT nombres, dni, edad, sexo, diagnostico, fecha_ingreso, estado
        FROM Pacientes
    """)
    pacientes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return {
        "camas_disponibles": camas_disponibles,
        "camas_ocupadas": camas_ocupadas,
        "pacientes_hospitalizados": pacientes_hospitalizados,
        "altas_medicas": altas_medicas,
        "camas": camas,
        "pacientes": pacientes
    }