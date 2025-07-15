from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Función para crear la tabla si no existe
def crear_tabla():
    conn = sqlite3.connect('correos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS correos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        email = request.form['email']
        
        # Validación básica del email
        if '@' not in email or '.' not in email:
            return render_template('formulario.html', error="Por favor ingresa un email válido")
        
        try:
            conn = sqlite3.connect('correos.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO correos (email) VALUES (?)', (email,))
            conn.commit()
            conn.close()
            return redirect(url_for('exito'))
        except sqlite3.IntegrityError:
            return render_template('formulario.html', error="Este email ya está registrado")
    
    return render_template('formulario.html')

@app.route('/exito')
def exito():
    return "¡Gracias por registrarte!"

if __name__ == '__main__':
    crear_tabla()
    app.run(debug=True)