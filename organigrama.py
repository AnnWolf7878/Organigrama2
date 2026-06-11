from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('seguridad.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS licitaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT,
            institucion TEXT,
            encargado TEXT,
            apertura TEXT,
            cierre TEXT,
            nombre TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def login_api():
    data = request.json
    if data.get('usuario') == 'admin' and data.get('password') == '123':
        return jsonify({"success": True})
    return jsonify({"success": False})

@app.route('/api/guardar_licitacion', methods=['POST'])
def guardar_licitacion():
    data = request.json
    conn = sqlite3.connect('seguridad.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO licitaciones (numero, institucion, encargado, apertura, cierre, nombre) VALUES (?, ?, ?, ?, ?, ?)',
                   (data['numero'], data['institucion'], data['encargado'], data['apertura'], data['cierre'], data['nombre']))
    conn.commit()
    conn.close()
    return jsonify({"success": True})

@app.route('/api/licitaciones', methods=['GET'])
def obtener_licitaciones():
    conn = sqlite3.connect('seguridad.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM licitaciones')
    rows = cursor.fetchall()
    conn.close()
    licitaciones = [{'numero': r[1], 'institucion': r[2], 'encargado': r[3], 'apertura': r[4], 'cierre': r[5], 'nombre': r[6]} for r in rows]
    return jsonify({"licitaciones": licitaciones})

if __name__ == '__main__':
    app.run(debug=True)
