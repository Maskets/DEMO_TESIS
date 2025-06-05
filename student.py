import streamlit as st
from datetime import datetime

def app():
    if not st.session_state.get("logged_in", False):
        st.error("🚫 Debe iniciar sesión para acceder a esta página")
        st.session_state["current_page"] = "Account"
        st.rerun()
        return

    st.title("📋 Registro de Estudiante")
    st.markdown("### Ingrese los datos básicos del estudiante")

    with st.form("student_form"):
        nombres = st.text_input("Nombres del estudiante *")
        apellidos = st.text_input("Apellidos del estudiante *")
        codigo_estudiante = st.text_input("Código del estudiante *")

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            guardar = st.form_submit_button("💾 Guardar", use_container_width=True)
        with col3:
            siguiente = st.form_submit_button("➡️ Siguiente", use_container_width=True)

        if guardar:
            if not all([nombres, apellidos, codigo_estudiante]):
                st.error("❌ Todos los campos son obligatorios")
            else:
                nuevo = {
                    "nombres": nombres.strip(),
                    "apellidos": apellidos.strip(),
                    "codigo_estudiante": codigo_estudiante.strip(),
                    "fecha_registro": datetime.now()
                }
                st.session_state.setdefault("evaluaciones", []).append(nuevo)
                st.session_state["student_data"] = nuevo
                st.session_state["student_completed"] = True
                st.success("✅ Estudiante guardado correctamente")

        if siguiente:
            if not st.session_state.get("student_completed"):
                st.error("❌ Debe guardar los datos antes de continuar")
            else:
                st.session_state["workflow_step"] = "formulation"
                st.session_state["current_page"] = "Formulation"
                st.rerun()
