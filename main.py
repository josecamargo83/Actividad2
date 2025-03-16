# Importamos Flask para crear (app web), jsonify (convierte datos a JSON).
from flask import Flask, jsonify

# Crea una instancia de la aplicación Flask.
app = Flask(__name__)

# Define una ruta para la URL "/personas" y especifica que solo acepta solicitudes GET.
@app.route("/personas", methods=["GET"])
def hola(): 
    # Crea una lista de nombres de personas.
    personas =  ["Jose", "Marcela", "Luis", "Pedro", "Ana", "Nicolas", "Camila", "Sebastian"]
    
    return jsonify({"personas": personas})
    # Convierte la lista de personas en un objeto JSON y lo devuelve como respuesta.
    # En este caso, crea un diccionario con la clave "personas" y el valor de la lista de personas.


# Verifica si el script se está ejecutando directamente (no importado como módulo).
if __name__ == "__main__":
    # Inicia el servidor de desarrollo de Flask.
    # debug=True habilita el modo de depuración, lo que permite ver los errores en el navegador y recargar automáticamente el servidor al guardar cambios.
    app.run(debug=True)