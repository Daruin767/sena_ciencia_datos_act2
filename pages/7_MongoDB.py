import streamlit as st
import pandas as pd

st.title("Bases de Datos en la Nube: MongoDB")

st.markdown("""
### Ejercicio
MongoDB es una base de datos NoSQL muy popular que almacena la información de forma muy similar a JSON.

**Instrucciones:**
1. Imagina que tienes acceso a un clúster de MongoDB Atlas. Para este ejercicio no necesitas conectarte realmente a la base de datos a menos que tengas un clúster de prueba.
2. Basándote en el material de clase, escribe el **código necesario (comentado si no tienes conexión)** para conectarte usando `pymongo` y la clase `MongoClient`.
3. Supón que la base de datos se llama `Veterinaria` y la colección se llama `mascotas`.
4. El código debe incluir cómo extraer los documentos y convertirlos en el DataFrame `df_mongo`.
""")

st.subheader("Tu resultado:")
st.markdown("Si no tienes la conexión real, escribe tu código usando `st.code()` para demostrar cómo lo harías teóricamente.")

# ESTUDIANTE: Escribe tu código (o tu st.code teórico) a continuación



# Requiere instalación previa: pip install pymongo pandas
import pandas as pd
from pymongo import MongoClient

# 1. Te conectas con tu usuario y contraseña
cliente = MongoClient('mongodb+srv://tu_usuario:tu_clave@cluster.mongodb.net') 

# 2. Eliges qué cajón revisar
base_datos = cliente["dbTest"]
coleccion = base_datos["user"]

# 3. Pandas convierte los documentos a Tabla automáticamente
df_mongo = pd.DataFrame(list(coleccion.find()))
print(df_mongo)