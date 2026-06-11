from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template('login.html')

# Ruta del Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Ruta de la API
@app.route('/api/organigrama')
def get_organigrama():
    return jsonify({
        "estructura": [
            {"puesto": "Gerente", "nombre": "Juan Pérez", "link": "#"}
        ]
    })

if __name__ == '__main__':
    app.run()
