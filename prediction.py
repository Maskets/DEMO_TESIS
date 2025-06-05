import streamlit as st

def app():
    if not st.session_state.get("logged_in", False):
        st.error("🚫 Debe iniciar sesión para acceder a esta página")
        st.session_state["current_page"] = "Account"
        st.rerun()
        return

    if not st.session_state.get("formulation_completed", False):
        st.warning("⚠️ Debe completar el formulario de evaluación antes de acceder a esta página")
        st.session_state["current_page"] = "Formulation"
        st.rerun()
        return

    st.title("🔮 Resultado de la Predicción")

    st.info("Aquí se mostrarán los resultados del modelo de deserción deportiva.")
    st.metric("Probabilidad de Deserción", "42%")  # Simulado
    st.write("Aquí se mostrará la gráfica SHAP (próximamente)")

    st.markdown("---")
    if st.button("💾 Guardar y ver historial"):
        st.success("Guardado y redirigiendo al historial...")
        st.session_state["prediction_completed"] = True
        st.session_state["workflow_step"] = "history"
        st.session_state["current_page"] = "History"
        st.rerun()
