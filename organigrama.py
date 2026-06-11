from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor funcionando correctamente"

@app.route('/test-api')
def test_api():
    return jsonify({"status": "La API está viva"})

@app.route('/api/organigrama')
def get_organigrama():
    return jsonify({"estructura": [{"puesto": "Prueba", "nombre": "Funciona", "link": "#"}]})

if __name__ == '__main__':
    app.run()
