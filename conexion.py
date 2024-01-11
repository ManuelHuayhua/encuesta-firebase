import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def inicializar_firebase():
    try:
        # Configurar credenciales
        firebase_sdk = credentials.Certificate('encuesta-firebase-42c25-firebase-adminsdk-bbj6i-46e9044821.json')

        # Inicializar la aplicación
        firebase_admin.initialize_app(firebase_sdk, {'databaseURL': 'https://encuesta-firebase-42c25-default-rtdb.firebaseio.com/'})
        
        print("Conexión a Firebase exitosa")
    except Exception as e:
        print(f"Error al conectar a Firebase: {e}")

# Llamar a la función
inicializar_firebase()