from flask import Blueprint, render_template
from services.epidemiologia_service import obtener_epidemiologia

epidemiologia_bp = Blueprint(
    'epidemiologia',
    __name__
)

@epidemiologia_bp.route('/epidemiologia')
def epidemiologia():
    datos = obtener_epidemiologia()
    return render_template('epidemiologia.html', **datos)