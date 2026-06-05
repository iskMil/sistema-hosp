from flask import Blueprint, render_template
from services.personal_service import obtener_personal

personal_bp = Blueprint(
    'personal',
    __name__
)

@personal_bp.route('/personal')
def personal():

    datos = obtener_personal()

    return render_template(
        'personal.html',
        **datos
    )