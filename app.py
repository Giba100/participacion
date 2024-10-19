from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Necesario para usar sesiones

# Datos (esto normalmente estaría en una base de datos)
users = {
    "LIMBERT69": "LIMBERT69",
    "CRISPAJERO": "CRISPAJERO"
}

# Ruta para la página de inicio de sesión
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Validar usuario y contraseña
        if username in users and users[username] == password:
            session['username'] = username  # Guardar usuario en sesión
            return redirect(url_for('bienvenido'))  # Redirigir a la página de bienvenida
        else:
            flash('Nombre de usuario o contraseña incorrectos......')
            return redirect(url_for('login'))

    return render_template('login.html')

# Ruta para la página de bienvenida personalizada
@app.route('/bienvenido')
def bienvenido():
    if 'username' in session:
        username = session['username']  # Obtener el nombre de usuario de la sesión
        return render_template('bienvenido.html', username=username)
    else:
        return redirect(url_for('login'))  # Si no está autenticado, redirigir al login

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('username', None)  # Eliminar usuario de la sesión
    flash('Has cerrado sesión correctamente.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
