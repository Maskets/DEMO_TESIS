# main.py
import streamlit as st
from streamlit_option_menu import option_menu
# Importa los archivos .py como módulos
import account
import home
import student
import formulation
import prediction
import history
import about

def main():
    st.set_page_config(page_title="Sistema de Deserción", layout="wide")
    
    # Inicializar el estado de navegación si no existe
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Account"  # página por defecto
    
    # Lista de páginas para facilitar el manejo de índices
    pages = ['Account', 'Home', 'Student', 'Formulation', 'Prediction', 'History', 'About']
    
    # Determinar el índice por defecto basado en la página actual
    try:
        default_index = pages.index(st.session_state["current_page"])
    except ValueError:
        default_index = 0
        st.session_state["current_page"] = "Account"
    
    with st.sidebar:
        app = option_menu(
            menu_title='Sistema de Deserción',
            options=pages,
            icons=['person-circle', 'house-fill', 'people-fill', 'file-earmark-text', 'bar-chart', 'clock-history', 'info-circle'],
            menu_icon='chat-text-fill',
            default_index=default_index,
            key="main_menu",  # Clave única para el componente
            styles={
                "container": {"padding": "5!important", "background-color": 'black'},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )
    
    # Actualizar el estado cuando se selecciona del menú
    if app != st.session_state["current_page"]:
        st.session_state["current_page"] = app
    
    # También permitir cambios programáticos desde otros módulos
    if "navigate_to" in st.session_state:
        st.session_state["current_page"] = st.session_state["navigate_to"]
        del st.session_state["navigate_to"]  # Limpiar después de usar
        st.rerun()  # Forzar actualización para reflejar el cambio en el menú
    
    # Navegación basada en el estado actual
    current_page = st.session_state["current_page"]
    
    if current_page == 'Account':
        account.app()
    elif current_page == 'Home':
        home.app()
    elif current_page == 'Student':
        student.app()
    elif current_page == 'Formulation':
        formulation.app()
    elif current_page == 'Prediction':
        prediction.app()
    elif current_page == 'History':
        history.app()
    elif current_page == 'About':
        about.app()

if __name__ == '__main__':
    main()