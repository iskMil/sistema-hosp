from config.database import get_connection

def obtener_resumen_dashboard():
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

    cursor.execute("SELECT ISNULL(SUM(cantidad_casos), 0) FROM Epidemiologia WHERE enfermedad = 'Dengue'")
    casos_dengue = cursor.fetchone()[0]

    cursor.execute("SELECT ISNULL(SUM(cantidad_casos), 0) FROM Epidemiologia WHERE enfermedad = 'Anemia'")
    casos_anemia = cursor.fetchone()[0]

    cursor.close()
    conexion.close()

    return {
        "camas_disponibles": camas_disponibles,
        "camas_ocupadas": camas_ocupadas,
        "pacientes_hospitalizados": pacientes_hospitalizados,
        "altas_medicas": altas_medicas,
        "casos_dengue": casos_dengue,
        "casos_anemia": casos_anemia
    }