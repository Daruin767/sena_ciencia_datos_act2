import streamlit as st
import pandas as pd

st.title("Bases de Datos en la Nube: Firebase Firestore")

st.markdown("""
### Ejercicio
Firebase es otra opción excelente adoptada por múltiples startups para almacenar datos en tiempo real.

**Instrucciones:**
1. Asume que se te proporcionó un archivo de credenciales de servicio `llave_secreta.json`.
2. Escribe el **código teórico (usando st.code() o conectándote si tienes tu propia bd)** que emplearías con `firebase_admin` para arrancar la aplicación y obtener el cliente de la base de datos.
3. El objetivo sería conectarse a la colección `vehiculos` de tu Firestore y traer todos los documentos.
4. Indica cómo convertirías la respuesta iterando los documentos para extraer su `to_dict()`.
5. Convierte esa lista a un DataFrame `df_firebase` final.
""")

st.subheader("Tu resultado:")
st.markdown("Escribe en la parte de abajo el código que usarías para lograr el objetivo. Si usas código comentado/teórico, compártelo adentro de `st.code()`.")

# ESTUDIANTE: Escribe tu código a continuación
st.code("""

import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# 1. Inicializar Firebase con el archivo de credenciales proporcionado
# (Código teórico si no tienes conexión real)
credenciales = credentials.Certificate('llave_secreta.json')
firebase_admin.initialize_app(credenciales)

# 2. Obtener el cliente de Firestore
bd_firestore = firestore.client()

# 3. Acceder a la colección 'vehiculos'
vehiculos_documentos = bd_firestore.collection('vehiculos').stream()

# 4. Convertir los documentos a diccionarios usando to_dict()
datos_lista = [documento.to_dict() for documento in vehiculos_documentos]

# 5. Convertir la lista a DataFrame
df_firebase = pd.DataFrame(datos_lista)

# 6. Mostrar el DataFrame en Streamlit
st.dataframe(df_firebase)
""")


