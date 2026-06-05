from flask import Blueprint, render_template, request

auth_bp = Blueprint(
    'auth',
    __name__
)

@auth_bp.route('/')
def login():
    return render_template('login.html')

@auth_bp.route('/validar_login', methods=['POST'])
def validar_login():

    usuario = request.form['usuario'].strip()
    contrasena = request.form['contrasena'].strip()

    # Ambos vacíos
    if usuario == '' and contrasena == '':
        return render_template(
            'login.html',
            error_usuario='El usuario es obligatorio',
            error_contrasena='La contraseña es obligatoria',
            usuario=''
        )

    # Usuario vacío
    if usuario == '':
        return render_template(
            'login.html',
            error_usuario='El usuario es obligatorio',
            usuario=''
        )

    # Contraseña vacía
    if contrasena == '':
        return render_template(
            'login.html',
            error_contrasena='La contraseña es obligatoria',
            usuario=usuario
        )

    # Credenciales correctas
    if usuario == 'admin' and contrasena == '123456':

        return render_template(
            'login.html',
            success='¡Acceso concedido! Redirigiendo...',
            usuario=usuario
        )

    # Credenciales incorrectas
    return render_template(
        'login.html',
        error='Usuario o contraseña incorrectos',
        usuario=usuario
    )
@auth_bp.route('/logout')
def logout():
    return render_template(
        'login.html',
        success='Sesión cerrada correctamente'
    )