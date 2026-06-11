from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def login_post():
    return jsonify({"success": True})

@app.route('/api/organigrama', methods=['GET'])
def get_organigrama():
    return jsonify({
        "estructura": [
            {"puesto": "Gerente", "nombre": "Juan", "link": "#"},
            {"puesto": "Asistente", "nombre": "Ana", "link": "#"}
        ]
    })

if __name__ == '__main__':
    app.run()
