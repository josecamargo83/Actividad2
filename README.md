API de Nombres de Personas

Esta API proporciona una lista de nombres de personas en formato JSON.

Endpoints

`/personas`

-Método: `GET`
-Descripción: Devuelve una lista de nombres de personas.
-Formato de respuesta: JSON
    
Cómo Consumir la API
Puedes consumir esta API utilizando cualquier cliente HTTP, Ejemplo: `Postman`, o desde tu navegador web.

Notas

- Asegúrate de que la API esté en ejecución antes de intentar consumirla.
- Si estás ejecutando la API localmente, la URL base será `http://127.0.0.1:5000/personas`. Si la API está alojada en otro servidor, deberás usar la URL correspondiente.

Ejecutar la API localmente

1.  Asegúrate de tener Python y Flask instalados.
2.  Guarda el código de la API en un archivo llamado `main.py`.
3.  Abre tu terminal, navega hasta el directorio donde guardaste `main.py`, y ejecuta el siguiente comando:
    
    python main.py
    
4.  La API estará disponible en `http://127.0.0.1:5000/personas`.

