from flask import Flask

from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.indicadores_routes import indicadores_bp
from routes.epidemiologia_routes import epidemiologia_bp
from routes.personal_routes import personal_bp
from routes.importacion_routes import importacion_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(indicadores_bp)
app.register_blueprint(epidemiologia_bp)
app.register_blueprint(personal_bp)
app.register_blueprint(importacion_bp)

if __name__ == '__main__':
    app.run(debug=True)