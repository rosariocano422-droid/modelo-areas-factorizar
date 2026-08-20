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

if "caso_actual" not in st.session_state or st.session_state["caso_actual"] != caso_elegido:
    st.session_state["caso_actual"] = caso_elegido
    st.session_state["paso"] = 0

if caso_elegido == "Personalizado: ingresa tus propios coeficientes":
    clave_actual = "personalizado_" + str(datos["p"]) + "_" + str(datos["q"])
    if st.session_state.get("clave_personalizado") != clave_actual:
        st.session_state["clave_personalizado"] = clave_actual
        st.session_state["paso"] = 0

p_val = datos["p"]
q_val = datos["q"]

st.write("**Polinomio seleccionado:** a2 + " + str(p_val) + "a + " + str(q_val))

MEDIDA_1 = 5
MEDIDA_A = 10
U = MEDIDA_1 * 8
A = MEDIDA_A * 8

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("1 - Mostrar fichas"):
        st.session_state["paso"] = 1
with col2:
    if st.button("2 - Armar rectangulo"):
        st.session_state["paso"] = 2
with col3:
    if st.button("3 - Ver factorizacion"):
        st.session_state["paso"] = 3

paso = st.session_state.get("paso", 0)

st.divider()

if paso >= 1:
    st.subheader("Fichas necesarias")
    st.write("- 1 ficha de area a2 (lados de " + str(MEDIDA_A) + " cm cada uno)")
    st.write("- " + str(p_val) + " fichas de area a (largo " + str(MEDIDA_A) + " cm, ancho " + str(MEDIDA_1) + " cm)")
    st.write("- " + str(q_val) + " fichas de area 1 (lados de " + str(MEDIDA_1) + " cm cada uno)")

    fichas_html = '<div style="display:flex; flex-wrap:wrap; gap:16px; align-items:flex-end;">'
    fichas_html += '<div style="text-align:center;">'
    fichas_html += '<div style="width:' + str(A) + 'px; height:' + str(A) + 'px; background:#f4a3a3; border:2px solid #b33; display:flex; align-items:center; justify-content:center; font-weight:bold;">a2</div>'
    fichas_html += '<div style="font-size:11px;">' + str(MEDIDA_A) + ' cm x ' + str(MEDIDA_A) + ' cm</div>'
    fichas_html += '</div>'
    for _ in range(p_val):
        fichas_html += '<div style="text-align:center;">'
        fichas_html += '<div style="width:' + str(U) + 'px; height:' + str(A) + 'px; background:#a3c6f4; border:2px solid #3366b3; display:flex; align-items:center; justify-content:center; font-weight:bold;">a</div>'
        fichas_html += '<div style="font-size:11px;">' + str(MEDIDA_1) + ' cm x ' + str(MEDIDA_A) + ' cm</div>'
        fichas_html += '</div>'
    for _ in range(q_val):
        fichas_html += '<div style="text-align:center;">'
        fichas_html += '<div style="width:' + str(U) + 'px; height:' + str(U) + 'px; background:#a3f4b3; border:2px solid #339955; display:flex; align-items:center; justify-content:center; font-weight:bold;">1</div>'
        fichas_html += '<div style="font-size:11px;">' + str(MEDIDA_1) + ' cm x ' + str(MEDIDA_1) + ' cm</div>'
        fichas_html += '</div>'
    fichas_html += '</div>'
    st.markdown(fichas_html, unsafe_allow_html=True)

if paso >= 2:
    st.subheader("Rectangulo armado")
    if datos["factoriza"]:
        m = datos["m"]
        n = datos["n"]
        base_cm = MEDIDA_A + m * MEDIDA_1
        altura_cm = MEDIDA_A + n * MEDIDA_1

        rect_html = '<div style="display:inline-block; border:3px solid #333;">'
        rect_html += '<div style="display:flex;">'
        rect_html += '<div style="width:' + str(A) + 'px; height:' + str(A) + 'px; background:#f4a3a3; border:1px solid #b33; display:flex; align-items:center; justify-content:center; font-weight:bold;">a2</div>'
        for _ in range(m):
            rect_html += '<div style="width:' + str(U) + 'px; height:' + str(A) + 'px; background:#a3c6f4; border:1px solid #3366b3; display:flex; align-items:center; justify-content:center; font-weight:bold;">a</div>'
        rect_html += '</div>'
        for _ in range(n):
            rect_html += '<div style="display:flex;">'
            rect_html += '<div style="width:' + str(A) + 'px; height:' + str(U) + 'px; background:#a3c6f4; border:1px solid #3366b3; display:flex; align-items:center; justify-content:center; font-weight:bold;">a</div>'
            for _ in range(m):
                rect_html += '<div style="width:' + str(U) + 'px; height:' + str(U) + 'px; background:#a3f4b3; border:1px solid #339955; display:flex; align-items:center; justify-content:center; font-weight:bold;">1</div>'
            rect_html += '</div>'
        rect_html += '</div>'

        st.markdown(rect_html, unsafe_allow_html=True)
        st.write("**Base:** a + " + str(m) + "  ->  " + str(MEDIDA_A) + " cm + " + str(m) + "x" + str(MEDIDA_1) + " cm = **" + str(base_cm) + " cm**")
        st.write("**Altura:** a + " + str(n) + "  ->  " + str(MEDIDA_A) + " cm + " + str(n) + "x" + str(MEDIDA_1) + " cm = **" + str(altura_cm) + " cm**")
    else:
        st.error("No es posible armar un rectangulo con lados enteros positivos usando estas fichas.")
        st.write("Se intento organizar 1 ficha a2 (" + str(MEDIDA_A) + " cm x " + str(MEDIDA_A) + " cm), " + str(p_val) + " fichas de a y " + str(q_val) + " fichas de 1, pero no existen dos numeros enteros positivos que multiplicados den " + str(q_val) + " y sumados den " + str(p_val) + ".")

if paso >= 3:
    st.subheader("Factorizacion")
    if datos["factoriza"]:
        m = datos["m"]
        n = datos["n"]
        st.success("a2 + " + str(p_val) + "a + " + str(q_val) + " = (a + " + str(m) + ")(a + " + str(n) + ")")
    else:
        st.warning("a2 + " + str(p_val) + "a + " + str(q_val) + " no se puede factorizar como producto de dos binomios con terminos enteros positivos.")
