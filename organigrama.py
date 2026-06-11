from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/organigrama')
def get_organigrama():
    return jsonify({
        "estructura": [
            {"puesto": "Gerente", "nombre": "Juan Pérez", "link": "#"}
        ]
    })

if __name__ == '__main__':
    # Render necesita usar la variable de entorno PORT si está disponible
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)