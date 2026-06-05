from flask import Blueprint, render_template
from services.dashboard_service import obtener_resumen_dashboard

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    datos = obtener_resumen_dashboard()
    return render_template('dashboard.html', **datos)