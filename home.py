import streamlit as st

def app():
    if not st.session_state.get("logged_in", False):
        st.error("🚫 Debe iniciar sesión para acceder a esta página")
        st.session_state["current_page"] = "Account"
        st.rerun()
        return

    st.title("🏠 Panel Principal")
    st.markdown(f"### Bienvenido, {st.session_state.get('username', 'Usuario')}")

    if st.button("🚀 Iniciar Registro de Estudiante"):
        st.session_state["workflow_active"] = True
        st.session_state["workflow_step"] = "student"
        st.session_state["student_completed"] = False
        st.session_state["formulation_completed"] = False
        st.session_state["prediction_completed"] = False
        st.session_state["current_page"] = "Student"
        st.rerun()
