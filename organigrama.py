from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor Operativo"

@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')

@app.route('/api/organigrama')
def api():
    return jsonify({"estructura": [{"puesto": "TEST", "nombre": "CONEXION OK", "link": "#"}]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
