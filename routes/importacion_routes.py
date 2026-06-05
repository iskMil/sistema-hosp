from flask import Blueprint, render_template, request
import pandas as pd
import os

importacion_bp = Blueprint('importacion', __name__)

@importacion_bp.route('/importacion', methods=['GET', 'POST'])
def importacion():
    datos = []
    columnas = []

    if request.method == 'POST':
        archivo = request.files['archivo']

        if archivo.filename.endswith('.csv'):
            df = pd.read_csv(archivo)
        else:
            df = pd.read_excel(archivo)

        columnas = df.columns.tolist()
        datos = df.values.tolist()

    return render_template(
        'importacion.html',
        columnas=columnas,
        datos=datos
    )