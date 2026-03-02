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
st.code("""

from pymongo import MongoClient
import pandas as pd

# 1. Conexión teórica a MongoDB Atlas
# Reemplazar tu_usuario, tu_clave y cluster por los datos reales
cliente = MongoClient('mongodb+srv://tu_usuario:tu_clave@cluster.mongodb.net')

# 2. Seleccionar la base de datos correcta
base_datos = cliente["Veterinaria"]

# 3. Seleccionar la colección correcta
coleccion = base_datos["mascotas"]

# 4. Extraer los documentos
documentos = coleccion.find()

# 5. Convertir los documentos en DataFrame
df_mongo = pd.DataFrame(list(documentos))

# 6. Mostrar en Streamlit
st.dataframe(df_mongo)
""")