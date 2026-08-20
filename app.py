import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Modelo de áreas para factorizar", layout="centered")

# Título de la actividad
st.title("Modelo de áreas para factorizar")
st.write("""
Esta simulación representa el modelo de áreas usado para factorizar polinomios 
de la forma **a² + pa + q**. Selecciona uno de los casos disponibles para ver 
cómo se arman las fichas, cómo se forma el rectángulo y cuál es su factorización.
""")

# Diccionario con los 5 casos fijos
casos = {
    "Caso 1: a² + 3a + 2": {"p": 3, "q": 2, "factoriza": True, "factor1": 1, "factor2": 2},
    "Caso 2: a² + 4a + 3": {"p": 4, "q": 3, "factoriza": True, "factor1": 1, "factor2": 3},
    "Caso 3: a² + 5a + 6": {"p": 5, "q": 6, "factoriza": True, "factor1": 2, "factor2": 3},
    "Caso 4: a² + 2a + 3": {"p": 2, "q": 3, "factoriza": False},
    "Caso 5: a² + 3a + 5": {"p": 3, "q": 5, "factoriza": False},
}

# Selector de caso
caso_elegido = st.selectbox("Selecciona un caso:", list(casos.keys()))

datos = casos[caso_elegido]

st.write(f"**Polinomio seleccionado:** a² + {datos['p']}a + {datos['q']}")
