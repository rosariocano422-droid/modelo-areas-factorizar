import streamlit as st

st.set_page_config(page_title="Modelo de áreas para factorizar", layout="centered")

st.title("Modelo de áreas para factorizar")
st.write("""
Esta simulación representa el modelo de áreas usado para factorizar polinomios 
de la forma **a² + pa + q**. Selecciona uno de los casos disponibles y sigue 
los pasos para armar el rectángulo y ver su factorización.
""")

casos = {
    "Caso 1: a² + 3a + 2": {"p": 3, "q": 2, "factoriza": True, "m": 1, "n": 2},
    "Caso 2: a² + 4a + 3": {"p": 4, "q": 3, "factoriza": True, "m": 1, "n": 3},
    "Caso 3: a² + 5a + 6": {"p": 5, "q": 6, "factoriza": True, "m": 2, "n": 3},
    "Caso 4: a² + 2a + 3": {"p": 2, "q": 3, "factoriza": False},
    "Caso 5: a² + 3a + 5": {"p": 3, "q": 5, "factoriza": False},
}

caso_elegido = st.selectbox("Selecciona un caso:", list(casos.keys()))
datos = casos[caso_elegido]

if "caso_actual" not in st.session_state or st.session_state["caso_actual"] != caso_elegido:
    st.session_state["caso_actual"] = caso_elegido
    st.session_state["paso"] = 0

st.write(f"**Polinomio seleccionado:** a² + {datos['p']}a + {datos['q']}")

# Medidas reales en centímetros
MEDIDA_1 = 5    # lado "1" = 5 cm
MEDIDA_A = 10   # lado "a" = 10 cm

# Tamaños en pixeles para dibujar (proporcionales a las medidas reales)
U = MEDIDA_1 * 8   # 40 px
A = MEDIDA_A * 8   # 80 px

def etiqueta(texto, cm):
    return f'<div style="font-size:11px; color:#333; text-align:center;">{texto}<br>{cm} cm</div>'

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("1️⃣ Mostrar fichas"):
        st.session_state["paso"] = 1
with col2:
    if st.button("2️⃣ Armar rectángulo"):
        st.session_state["paso"] = 2
with col3:
    if st.button("3️⃣ Ver factorización"):
        st.session_state["paso"] = 3

paso = st.session_state.get("paso", 0)

st.divider()

# ---------- PASO 1: fichas sueltas ----------
if paso >= 1:
    st.subheader("Fichas necesarias")
    st.write(f"- 1 ficha de área a² (lados de {MEDIDA_A} cm cada uno)")
    st.write(f"- {datos['p']} fichas de área a (largo {MEDIDA_A} cm, ancho {MEDIDA_1} cm)")
    st.write(f"- {datos['q']} fichas de área 1 (lados de {MEDIDA_1} cm cada uno)")

    fichas_html = '<div style="display:flex; flex-wrap:wrap; gap:16px; align-items:flex-end;">'

    # Ficha a²
    fichas_html += '<div style="text-align:center;">'
    fichas_html += f'<div style="width:{A}px; height:{A}px; background:#f4a3a3; border:2px solid #b33; display:flex; align-items:center; justify-content:center; font-weight:bold;">a²</div>'
    fichas_html += f'<div style="font-size:11px;">{MEDIDA_A} cm × {MEDIDA_A} cm</div>'
    fichas_html += '</div>'

    # Fichas a
    for _ in range(datos["p"]):
        fichas_html += '<div style="text-align:center;">'
        fichas_html += f'<div style="width:{U}px; height:{A}px; background:#a3c6f4; border:2px solid #3366b3; display:flex; align-items:center; justify-content:center; font-weight:bold;">a</div>'
        fichas_html += f'<div style="font-size:11px;">{MEDIDA_1} cm × {MEDIDA_A} cm</div>'
        fichas_html += '</div>'

    # Fichas 1
    for _ in range(datos["q"]):
        fichas_html += '<div style="text-align:center;">'
        fichas_html += f'<div style="width:{U}px; height:{U}px; background:#a3f4b3; border:2px solid #339955; display:flex; align-items:center; justify-content:center; font-weight:bold;">1</div>'
        fichas_html += f'<div style="font-size:11px;">{MEDIDA_1} cm × {MEDIDA_1} cm</div>'
        fichas_html += '</div>'

    fichas_html += '</div>'
    st.markdown(fichas_html, unsafe_allow_html=True)

# ---------- PASO 2: armar el rectángulo ----------
if paso >= 2:
    st.subheader("Rectángulo armado")
    if datos["factoriza"]:
        m, n = datos["m"], datos["n"]
        base_cm = MEDIDA_A + m * MEDIDA_1
        altura_cm = MEDIDA_A + n * MEDIDA_1

        rect_html = '<div style="display:inline-block; border:3px solid #333;">'
        rect_html += '<div style="display:flex;">'
        rect_html += f'<div style="width:{A}px; height:{A}px; background:#f4a3a3; border:1px solid #b33; display:flex; align-items:center; justify-content:center; font-weight:bold;">a²</div>'
        for _ in range(m):
            rect_html += f'<div style="width:{U}px; height:{A}px; background:#a3c6f4; border:1px solid #3366b3; display:flex; align-items:center; justify-content:center; font-weight:bold;">a</div>'
        rect_html += '</div>'
        for _ in range(n):
            rect_html += '<div style="display:flex;">'
            rect_html += f'<div style="width:{A}px; height:{U}px; background:#a3c6f4; border:1px solid #3366b3; display:flex; align-items:center; justify-content:center; font-weight:bold;">a</div>'
            for _ in range(m):
                rect_html += f'<div style="width:{U}px; height:{U}px; background:#a3f4b3; border:1px solid #339955; display:flex; align-items:center; justify-content:center; font-weight:bold;">1</div>'
            rect_html += '</div>'
        rect_html += '</div>'

        st.markdown(rect_html, unsafe_allow_html=True)
        st.write(f"**Base:** a + {m}  →  {MEDIDA_A} cm + {m}×{MEDIDA_1} cm = **{base_cm} cm**")
        st.write(f"**Altura:** a + {n}  →  {MEDIDA_A} cm + {n}×{MEDIDA_1} cm = **{altura_cm} cm**")
    else:
        st.error("⚠️ No es posible armar un rectángulo con lados enteros positivos usando estas fichas.")
        st.write(f"Se intentó organizar 1 ficha a² ({MEDIDA_A} cm × {MEDIDA_A} cm), {datos['p']} fichas de a "
                 f"y {datos['q']} fichas de 1, pero no existen dos números enteros positivos que multiplicados "
                 f"den {datos['q']} y sumados den {datos['p']}.")

# ---------- PASO 3: factorización ----------
if paso >= 3:
    st.subheader("Factorización")
    if datos["factoriza"]:
        m, n = datos["m"], datos["n"]
        st.success(f"a² + {datos['p']}a + {datos['q']} = (a + {m})(a + {n})")
    else:
        st.warning(f"a² + {datos['p']}a + {datos['q']} no se puede factorizar como producto de dos "
                   f"binomios con términos enteros positivos.")
