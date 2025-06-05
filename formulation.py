import streamlit as st

def app():
    if not st.session_state.get("logged_in", False):
        st.error("🚫 Debe iniciar sesión para acceder a esta página")
        st.session_state["current_page"] = "Account"
        st.rerun()
        return

    if not st.session_state.get("workflow_active", False) or not st.session_state.get("student_completed", False):
        st.warning("⚠️ Debe completar el registro del estudiante primero")
        st.session_state["current_page"] = "Student"
        st.rerun()
        return

    st.title("📝 Formulario de Evaluación - Estudiantes Deportistas")
    st.markdown("### Complete el cuestionario para el análisis predictivo")
    st.progress(0.66, text="Paso 2 de 3: Formulario de Evaluación")

    if st.session_state.get("student_data"):
        student = st.session_state["student_data"]
        st.info(f"👤 **Estudiante:** {student['nombres']} {student['apellidos']} - {student['codigo_estudiante']}")

    with st.form("formulation_form", clear_on_submit=False):
        st.markdown("#### 📋 Sección 1: Datos Generales")
        col1, col2 = st.columns(2)
        with col1:
            edad = st.text_input("1. Edad (en años) *")
            if edad and not edad.isdigit():
                st.error("Por favor, ingresa solo números enteros en el campo de edad.")
            genero = st.selectbox("2. Género *", ["Seleccionar", "Masculino", "Femenino"])
            facultad = st.selectbox("3. Facultad Universitaria *", [
                "Seleccionar", "Administración en Hotelería y Turismo", "Arquitectura", "Artes Contemporáneas",
                "Ciencias de la Salud", "Ciencias Humanas", "Comunicaciones", "Derecho", "Diseño",
                "Economía", "Educación", "Ingeniería", "Negocios", "Psicología"
            ])
        with col2:
            ciclo_actual = st.selectbox("4. Ciclo Actual *", ["Seleccionar"] + [str(i) for i in range(1, 11)])
            nivel_socioeconomico = st.selectbox("5. Nivel socioeconómico aproximado *", 
                ["Seleccionar", "Bajo", "Medio bajo", "Medio", "Medio alto", "Alto"])
            apoyo_economico_deporte = st.selectbox("6. ¿Recibes algún tipo de apoyo económico relacionado al deporte? *", [
                "Seleccionar", "Beca completa", "Beca parcial", "Apoyo en movilidad / alimentación", "No recibo apoyo"
            ])

        st.markdown("#### 📚 Sección 2: Rendimiento Académico")
        col3, col4 = st.columns(2)
        with col3:
            promedio_academico = st.text_input("1. Promedio académico del último semestre o ciclo (0 a 20) *")
            try:
                if promedio_academico:
                    float(promedio_academico)
            except ValueError:
                st.error("Por favor, ingresa solo números decimales válidos en el promedio académico.")
            afectan_ausencias = st.selectbox("2. ¿Cuánto han afectado tus ausencias a clases debido al deporte? *", 
                ["Seleccionar", "1", "2", "3", "4", "5"])
        with col4:
            carga_academica = st.selectbox("3. ¿Cómo calificarías la carga académica? *", 
                ["Seleccionar", "1", "2", "3", "4", "5"])
            estudios_afectan_deporte = st.selectbox("4. ¿Tus estudios afectan tu rendimiento deportivo? *", 
                ["Seleccionar", "Nunca", "Rara vez", "A veces", "Frecuentemente", "Siempre"])

        st.markdown("#### 🏃 Sección 3: Rendimiento Deportivo")
        col5, col6 = st.columns(2)
        with col5:
            deporte_practicado = st.selectbox("1. Deporte practicado *", [
                "Seleccionar", "Atletismo", "Básquet damas", "Básquet varones", "Escalada", "Fútbol damas",
                "Fútbol varones", "Futsal damas", "Futsal varones", "Judo", "Karate",
                "Levantamiento de pesas", "Lucha olímpica", "Natación", "Rugby damas", "Rugby varones",
                "Taekwondo", "Tenis de mesa", "Tiro deportivo", "Vóley damas", "Vóley varones", "Wushu"
            ])
            anos_experiencia = st.selectbox("2. Años de experiencia *", 
                ["Seleccionar", "Menos de 1 año", "1 a 3 años", "4 a 6 años", "Más de 6 años"])
            ranking_posicion = st.selectbox("3. Ranking o posición *", 
                ["Seleccionar", "Local", "Regional", "Nacional", "Internacional", "No aplica"])
        with col6:
            competiciones_ano = st.selectbox("4. Número de competiciones *", 
                ["Seleccionar", "Ninguna", "1 a 5", "Más de 5"])
            frecuencia_lesiones = st.selectbox("5. Frecuencia de lesiones *", 
                ["Seleccionar", "Ninguna", "1 a 2 lesiones", "Más de 2 lesiones"])

        st.markdown("#### 🧠 Sección 4: Factores Psicológicos y Sociales")
        col7, col8 = st.columns(2)
        with col7:
            estres_deporte = st.selectbox("1. Nivel de estrés *", ["Seleccionar", "1", "2", "3", "4", "5"])
            motivacion_competir = st.selectbox("2. Motivación para competir *", ["Seleccionar", "1", "2", "3", "4", "5"])
            apoyo_familia = st.selectbox("3. Apoyo emocional de tu familia *", ["Seleccionar", "1", "2", "3", "4", "5"])
        with col8:
            apoyo_entrenador = st.selectbox("4. Apoyo del entrenador *", ["Seleccionar", "1", "2", "3", "4", "5"])
            apoyo_companeros = st.selectbox("5. Apoyo de compañeros/as *", ["Seleccionar", "1", "2", "3", "4", "5"])
            integracion_equipo = st.selectbox("6. Integración en el equipo *", ["Seleccionar", "1", "2", "3", "4", "5"])

        st.markdown("#### 🏋️ Sección 5: Carga de Entrenamiento")
        col9, col10 = st.columns(2)
        with col9:
            horas_entrenamiento = st.selectbox("1. Horas de entrenamiento *", 
                ["Seleccionar", "1 a 5 horas", "6 a 10 horas", "Más de 10 horas"])
            intensidad_entrenamiento = st.selectbox("2. Intensidad del entrenamiento *", 
                ["Seleccionar", "1", "2", "3", "4", "5"])
        with col10:
            priorizar_entrenamientos = st.radio("3. ¿Priorizas entrenamientos sobre clases? *", ["Sí", "No"])
            considerar_dejar_deporte = st.radio("4. ¿Has considerado dejar el deporte? *", ["Sí", "No"])

        comentarios_adicionales = st.text_area("Comentarios o Información Adicional", height=100)

        st.markdown("---")
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])

        with col_btn1:
            if st.form_submit_button("💾 Guardar", use_container_width=True):
                required_fields = [
                    (edad and edad.isdigit(), "Edad"),
                    (genero != "Seleccionar", "Género"),
                    (facultad != "Seleccionar", "Facultad Universitaria"),
                    (ciclo_actual != "Seleccionar", "Ciclo Actual"),
                    (nivel_socioeconomico != "Seleccionar", "Nivel Socioeconómico"),
                    (apoyo_economico_deporte != "Seleccionar", "Apoyo Económico"),
                    (promedio_academico and promedio_academico.replace('.', '').isdigit(), "Promedio Académico"),
                    (afectan_ausencias != "Seleccionar", "Ausencias"),
                    (carga_academica != "Seleccionar", "Carga Académica"),
                    (estudios_afectan_deporte != "Seleccionar", "Estudios vs Deporte"),
                    (deporte_practicado != "Seleccionar", "Deporte Practicado"),
                    (anos_experiencia != "Seleccionar", "Experiencia"),
                    (ranking_posicion != "Seleccionar", "Ranking"),
                    (competiciones_ano != "Seleccionar", "Competiciones"),
                    (frecuencia_lesiones != "Seleccionar", "Lesiones"),
                    (estres_deporte != "Seleccionar", "Estrés"),
                    (motivacion_competir != "Seleccionar", "Motivación"),
                    (apoyo_familia != "Seleccionar", "Apoyo Familiar"),
                    (apoyo_entrenador != "Seleccionar", "Apoyo Entrenador"),
                    (apoyo_companeros != "Seleccionar", "Apoyo Compañeros"),
                    (integracion_equipo != "Seleccionar", "Integración Equipo"),
                    (horas_entrenamiento != "Seleccionar", "Horas Entrenamiento"),
                    (intensidad_entrenamiento != "Seleccionar", "Intensidad"),
                    (priorizar_entrenamientos in ["Sí", "No"], "Priorizar Entrenamiento"),
                    (considerar_dejar_deporte in ["Sí", "No"], "Considerar Dejar")
                ]
                missing_fields = [f for v, f in required_fields if not v]
                if missing_fields:
                    st.error(f"❌ Faltan completar: {', '.join(missing_fields)}")
                else:
                    try:
                        promedio_val = float(promedio_academico)
                        if not (0 <= promedio_val <= 20):
                            st.error("❌ El promedio debe estar entre 0 y 20")
                            return
                    except ValueError:
                        st.error("❌ El promedio debe ser numérico")
                        return

                    st.session_state["formulation_data"] = {
                        "edad": int(edad),
                        "genero": genero,
                        "facultad": facultad,
                        "ciclo_actual": ciclo_actual,
                        "nivel_socioeconomico": nivel_socioeconomico,
                        "apoyo_economico_deporte": apoyo_economico_deporte,
                        "promedio_academico": float(promedio_academico),
                        "afectan_ausencias": afectan_ausencias,
                        "carga_academica": carga_academica,
                        "estudios_afectan_deporte": estudios_afectan_deporte,
                        "deporte_practicado": deporte_practicado,
                        "anos_experiencia": anos_experiencia,
                        "ranking_posicion": ranking_posicion,
                        "competiciones_ano": competiciones_ano,
                        "frecuencia_lesiones": frecuencia_lesiones,
                        "estres_deporte": estres_deporte,
                        "motivacion_competir": motivacion_competir,
                        "apoyo_familia": apoyo_familia,
                        "apoyo_entrenador": apoyo_entrenador,
                        "apoyo_companeros": apoyo_companeros,
                        "integracion_equipo": integracion_equipo,
                        "horas_entrenamiento": horas_entrenamiento,
                        "intensidad_entrenamiento": intensidad_entrenamiento,
                        "priorizar_entrenamientos": priorizar_entrenamientos,
                        "considerar_dejar_deporte": considerar_dejar_deporte,
                        "comentarios_adicionales": comentarios_adicionales
                    }
                    st.session_state["formulation_completed"] = True
                    st.success("✅ Formulario guardado correctamente")

        with col_btn3:
            if st.form_submit_button("➡️ Siguiente", use_container_width=True, type="primary"):
                if st.session_state.get("formulation_completed", False):
                    st.session_state["workflow_step"] = "prediction"
                    st.session_state["current_page"] = "Prediction"
                    st.rerun()
                else:
                    st.error("❌ Debe guardar los datos antes de continuar")
