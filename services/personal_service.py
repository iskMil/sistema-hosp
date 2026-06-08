from config.database import get_connection

def obtener_personal():

    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM Empleados
        WHERE FechaAlta IS NULL
    """)
    
    personal_activo = cursor.fetchone()[0]

    cursor.execute("""
    SELECT
        e.ApellidoPaterno + ' ' + e.ApellidoMaterno + ' ' + e.Nombres AS Nombre,
        te.Descripcion AS Cargo,
        s.Nombre AS Area,
        CAST(a.FechaIngreso AS DATE) AS Fecha,
        'Asistió' AS Asistencia,
        COUNT(a.IdAtencion) AS Atenciones,
        CASE
            WHEN COUNT(a.IdAtencion) >= 8 THEN 'Alto'
            WHEN COUNT(a.IdAtencion) BETWEEN 4 AND 7 THEN 'Bueno'
            WHEN COUNT(a.IdAtencion) BETWEEN 1 AND 3 THEN 'Regular'
            ELSE 'Sin atención'
        END AS Cumplimiento
    FROM Atenciones a
    INNER JOIN Medicos m
        ON a.IdMedicoIngreso = m.IdMedico
    INNER JOIN Empleados e
        ON m.IdEmpleado = e.IdEmpleado
    LEFT JOIN TiposEmpleado te
        ON e.IdTipoEmpleado = te.IdTipoEmpleado
    LEFT JOIN Servicios s
        ON a.IdServicioIngreso = s.IdServicio
    WHERE a.IdMedicoIngreso IS NOT NULL
      AND YEAR(a.FechaIngreso) >= 2025
    GROUP BY
        e.ApellidoPaterno,
        e.ApellidoMaterno,
        e.Nombres,
        te.Descripcion,
        s.Nombre,
        CAST(a.FechaIngreso AS DATE)
    ORDER BY Fecha DESC, Atenciones DESC
""")

    personal = cursor.fetchall()

    nombres_personal = [fila.Nombre for fila in personal[:10]]
    atenciones_personal = [fila.Atenciones for fila in personal[:10]]

    cursor.close()
    conexion.close()

    return {
        "personal_activo": personal_activo,
        "personal": personal,
        "nombres_personal": nombres_personal,
        "atenciones_personal": atenciones_personal
    }