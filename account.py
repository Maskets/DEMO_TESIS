# account.py
import streamlit as st

def app():
    st.title("🔐 Iniciar Sesión")
    
    # Contenedor principal centrado
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Acceso al Sistema de Predicción de Deserción")
        
        with st.form("login_form"):
            st.markdown("#### Credenciales de Acceso")
            
            username = st.text_input("👤 Usuario", placeholder="Ingrese su usuario")
            password = st.text_input("🔒 Contraseña", type="password", placeholder="Ingrese su contraseña")
            
            col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
            with col_btn2:
                login_button = st.form_submit_button("Iniciar Sesión", use_container_width=True)
        
        if login_button:
            if username and password:
                # Aquí se conectaría con Django backend para validar credenciales
                # Por ahora simulamos login exitoso
                if username == "admin" and password == "123":  # Credenciales de prueba
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.success("✅ Login exitoso!")
                    st.balloons()
                    
                    # Navegar a Home después del login
                    st.session_state["navigate_to"] = "Home"
                    st.rerun()
                else:
                    st.error("❌ Credenciales incorrectas")
            else:
                st.warning("⚠️ Por favor complete todos los campos")
    
    # Información adicional
    st.markdown("---")
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.info("🎓 **Sistema Académico**\n\nSistema para la predicción de deserción estudiantil basado en machine learning.")
    
    with col_info2:
        st.info("🔧 **Credenciales de Prueba**\n\nUsuario: admin\nContraseña: 123")