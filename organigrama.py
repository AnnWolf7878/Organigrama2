from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Ruta de Login corregida para leer JSON
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    password = datos.get('password')
    
    # Aquí puedes poner tu lógica de validación real
    if usuario == "admin" and password == "123":
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

@app.route('/api/organigrama')
def get_organigrama():
    return jsonify({
        "estructura": [
            {"puesto": "Gerente", "nombre": "Juan Pérez", "link": "#"}
        ]
    })

if __name__ == '__main__':
    app.run()
