from flask import Flask, jsonify, request, render_template
import urllib.parse

app = Flask(__name__, template_folder="c:/Users/ann_m/Downloads/templates")

# --- LÓGICA DE LA API ---
@app.route("/api/organigrama")
def get_datos():
    empresa = request.args.get("nombre", "Empresa")
    puestos = ["Gerente General", "Gerente Comercial", "Director de Tecnología"]
    
    estructura = []
    for p in puestos:
        query = f'"{p}" {empresa} site:linkedin.com/in/'
        url_busqueda = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
        
        estructura.append({
            "puesto": p.upper(), 
            "nombre": "VER RESULTADOS", 
            "link": url_busqueda
        })
    
    response = jsonify({"estructura": estructura})
    # Cabeceras para asegurar conexión con el frontend
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# --- RUTAS DE NAVEGACIÓN ---
@app.route("/")
def index(): 
    return render_template("login.html")

@app.route("/dashboard")
def dashboard(): 
    return render_template("dashboard.html")

# --- AUTENTICACIÓN ---
@app.route("/login", methods=["POST"])
def login():
    datos = request.json
    # Credenciales de prueba
    if datos.get("usuario") == "admin" and datos.get("password") == "123":
        return jsonify({"success": True})
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

if __name__ == "__main__":
    # Servidor configurado para escuchar en la interfaz local
    app.run(host="127.0.0.1", port=5000, debug=True)
