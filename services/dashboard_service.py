from config.database import get_connection

def obtener_resumen_dashboard():

    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM Camas
        WHERE IdEstadoCama = 1
    """)
    camas_disponibles = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM Camas
        WHERE IdEstadoCama = 3
    """)
    camas_ocupadas = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM Camas
        WHERE IdPaciente IS NOT NULL
    """)
    pacientes_hospitalizados = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM Atenciones
        WHERE FechaEgreso IS NOT NULL
          AND YEAR(FechaEgreso) >= 2025
    """)
    altas_medicas = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM AtencionesDiagnosticos ad
        INNER JOIN Diagnosticos d
            ON ad.IdDiagnostico = d.IdDiagnostico
        WHERE d.Descripcion LIKE '%dengue%'
    """)
    casos_dengue = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM AtencionesDiagnosticos ad
        INNER JOIN Diagnosticos d
            ON ad.IdDiagnostico = d.IdDiagnostico
        WHERE d.Descripcion LIKE '%neumon%'
    """)
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