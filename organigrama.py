from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/organigrama')
def get_organigrama():
    # Esta es la parte que causa el error si no está bien definida
    # Ahora devuelve siempre una lista, incluso si está vacía
    return jsonify({
        "estructura": [
            {"puesto": "Gerente General", "nombre": "Juan Pérez", "link": "https://linkedin.com"},
            {"puesto": "Gerente Comercial", "nombre": "Ana López", "link": "https://linkedin.com"}
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)
