import streamlit as st

st.set_page_config(page_title="Modelo de areas para factorizar", layout="centered")

st.title("Modelo de areas para factorizar")
st.write("Esta simulacion representa el modelo de areas usado para factorizar polinomios de la forma a^2 + pa + q. Selecciona uno de los casos disponibles, o elige Personalizado para ingresar tus propios coeficientes, y sigue los pasos para armar el rectangulo y ver su factorizacion.")

casos = {
    "Caso 1: a2 + 3a + 2": {"p": 3, "q": 2, "factoriza": True, "m": 1, "n": 2},
    "Caso 2: a2 + 4a + 3": {"p": 4, "q": 3, "factoriza": True, "m": 1, "n": 3},
    "Caso 3: a2 + 5a + 6": {"p": 5, "q": 6, "factoriza": True, "m": 2, "n": 3},
    "Caso 4: a2 + 2a + 3": {"p": 2, "q": 3, "factoriza": False, "m": None, "n": None},
    "Caso 5: a2 + 3a + 5": {"p": 3, "q": 5, "factoriza": False, "m": None, "n": None},
    "Personalizado: ingresa tus propios coeficientes": None,
}

caso_elegido = st.selectbox("Selecciona un caso:", list(casos.keys()))

if caso_elegido == "Personalizado: ingresa tus propios coeficientes":
    col_p, col_q = st.columns(2)
    with col_p:
        p_usuario = st.number_input("Coeficiente p (de 'pa'):", min_value=1, max_value=20, value=3, step=1)
    with col_q:
        q_usuario = st.number_input("Coeficiente q:", min_value=1, max_value=50, value=2, step=1)

    factoriza = False
    m_final = None
    n_final = None
    for m in range(1, q_usuario + 1):
        if q_usuario % m == 0:
            n = q_usuario // m
            if m + n == p_usuario:
                factoriza = True
                m_final = m
                n_final = n
                break

    datos = {"p": p_usuario, "q": q_usuario, "factoriza": factoriza, "m": m_final, "n": n_final}
else:
    datos = casos[caso_elegido]

if "caso_actual" not in st.session_state or st.session_state["caso_actual"] !=
