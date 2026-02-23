import streamlit as st
import pandas as pd

st.title("Método 1: Juntando varias Series")

st.markdown("""
### Ejercicio
En este ejercicio debes crear un DataFrame agrupando información sobre **películas favoritas**.

1. Crea tres Series de Pandas diferentes:
    - Una serie llamada `titulos` con al menos 4 nombres de películas.
    - Una serie llamada `directores` con los directores de esas películas.
    - Una serie llamada `años` con el año de estreno.
2. Une estas tres series en un único DataFrame llamado `df_peliculas`, asignando nombres descriptivos a las columnas (por ejemplo: `Título`, `Director`, `Año de Estreno`).
3. Muestra el DataFrame en la aplicación usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación



peliculas = {
    "titulos": ["Interestelar", "v de vendetta", "John Wick 3: Parabellum", "Misión de rescate 2"],
    "directores": ["Christopher Nolan", "James McTeigue", "Chad Stahelski", "Sam Hargrave"],
    "años": [2014, 2005, 2019 , 2023]
}


df = pd.DataFrame(peliculas)


print("Nuestra tabla de peliculas favoritas:")
print(df)


st.dataframe(df)

