from flask import Blueprint, render_template
from services.indicadores_service import obtener_indicadores

indicadores_bp = Blueprint(
    'indicadores',
    __name__
)

@indicadores_bp.route('/indicadores')
def indicadores():
    datos = obtener_indicadores()
    return render_template('indicadores.html', **datos)