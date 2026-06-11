from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/organigrama', methods=['GET'])
def get_organigrama():
    # Respuesta directa sin lógica complicada
    return jsonify({"estructura": [{"puesto": "TEST", "nombre": "CONEXION OK", "link": "#"}]})

if __name__ == '__main__':
    app.run()
