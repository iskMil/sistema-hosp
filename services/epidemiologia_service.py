from config.database import get_connection

def obtener_epidemiologia():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            CASE
                WHEN d.Descripcion LIKE '%dengue%' THEN 'Dengue'
                WHEN d.Descripcion LIKE '%respir%' 
                  OR d.Descripcion LIKE '%bronqu%' THEN 'IRA'
                WHEN d.Descripcion LIKE '%neumon%' THEN 'Neumonía'
                WHEN d.Descripcion LIKE '%tuberc%' THEN 'Tuberculosis'
                WHEN d.Descripcion LIKE '%covid%' THEN 'COVID-19'
            END AS enfermedad,
            COUNT(*) AS total_casos
        FROM AtencionesDiagnosticos ad
        INNER JOIN Diagnosticos d
            ON ad.IdDiagnostico = d.IdDiagnostico
        WHERE d.Descripcion LIKE '%dengue%'
           OR d.Descripcion LIKE '%respir%'
           OR d.Descripcion LIKE '%bronqu%'
           OR d.Descripcion LIKE '%neumon%'
           OR d.Descripcion LIKE '%tuberc%'
           OR d.Descripcion LIKE '%covid%'
        GROUP BY
            CASE
                WHEN d.Descripcion LIKE '%dengue%' THEN 'Dengue'
                WHEN d.Descripcion LIKE '%respir%' 
                  OR d.Descripcion LIKE '%bronqu%' THEN 'IRA'
                WHEN d.Descripcion LIKE '%neumon%' THEN 'Neumonía'
                WHEN d.Descripcion LIKE '%tuberc%' THEN 'Tuberculosis'
                WHEN d.Descripcion LIKE '%covid%' THEN 'COVID-19'
            END
    """)

    resumen = cursor.fetchall()

    cursor.execute("""
        SELECT TOP 100
            d.Descripcion AS enfermedad,
            COUNT(*) AS total_casos
        FROM AtencionesDiagnosticos ad
        INNER JOIN Diagnosticos d
            ON ad.IdDiagnostico = d.IdDiagnostico
        WHERE d.Descripcion LIKE '%dengue%'
           OR d.Descripcion LIKE '%respir%'
           OR d.Descripcion LIKE '%bronqu%'
           OR d.Descripcion LIKE '%neumon%'
           OR d.Descripcion LIKE '%tuberc%'
           OR d.Descripcion LIKE '%covid%'
        GROUP BY d.Descripcion
        ORDER BY total_casos DESC
    """)

    casos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return {
        "resumen": resumen,
        "casos": casos
    }