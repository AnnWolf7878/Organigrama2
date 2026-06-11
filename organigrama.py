from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/organigrama')
def get_organigrama():
    return jsonify({
        "estructura": [
            {"puesto": "Gerente General", "nombre": "Juan Pérez", "link": "#"},
            {"puesto": "Gerente Comercial", "nombre": "Ana López", "link": "#"}
        ]
    })

if __name__ == '__main__':
    app.run()
