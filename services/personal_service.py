from config.database import get_connection

def obtener_personal():

    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM Personal
        WHERE estado = 'Activo'
    """)

    personal_activo = cursor.fetchone()[0]

    cursor.execute("""
        SELECT
            p.nombres,
            p.cargo,
            p.area,
            d.fecha,
            d.asistencia,
            d.atenciones_realizadas,
            d.cumplimiento
        FROM Personal p
        INNER JOIN DesempenoPersonal d
        ON p.id_personal = d.id_personal
    """)

    personal = cursor.fetchall()

    nombres_personal = [fila.nombres for fila in personal]
    atenciones_personal = [fila.atenciones_realizadas for fila in personal]

    cursor.close()
    conexion.close()

    return {
        "personal_activo": personal_activo,
        "personal": personal,
        "nombres_personal": nombres_personal,
        "atenciones_personal": atenciones_personal
    }