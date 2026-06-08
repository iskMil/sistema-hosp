from config.database import get_connection

def obtener_indicadores():

    conexion = get_connection()
    cursor = conexion.cursor()

    # Camas disponibles
    cursor.execute("""
        SELECT COUNT(*)
        FROM Camas
        WHERE IdEstadoCama = 1
    """)
    camas_disponibles = cursor.fetchone()[0]

    # Camas ocupadas
    cursor.execute("""
        SELECT COUNT(*)
        FROM Camas
        WHERE IdEstadoCama = 3
    """)
    camas_ocupadas = cursor.fetchone()[0]

    # Pacientes hospitalizados
    cursor.execute("""
        SELECT COUNT(*)
        FROM Camas
        WHERE IdPaciente IS NOT NULL
    """)
    pacientes_hospitalizados = cursor.fetchone()[0]

    # Altas médicas (temporal)
    cursor.execute("""
        SELECT COUNT(*)
        FROM Atenciones
        WHERE FechaEgreso IS NOT NULL
    """)
    altas_medicas = cursor.fetchone()[0]

    # Listado de camas
    cursor.execute("""
        SELECT
            c.Codigo,
            ec.Descripcion
        FROM Camas c
        INNER JOIN EstadosCama ec
            ON c.IdEstadoCama = ec.IdEstadoCama
    """)
    camas = cursor.fetchall()

    # Pacientes hospitalizados (simplificado)
    cursor.execute("""
        SELECT
            p.ApellidoPaterno,
            p.ApellidoMaterno,
            p.PrimerNombre,
            p.NroDocumento
        FROM Camas c
        INNER JOIN Pacientes p
            ON c.IdPaciente = p.IdPaciente
        WHERE c.IdPaciente IS NOT NULL
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