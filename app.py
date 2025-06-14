import streamlit as st
import requests

st.set_page_config(page_title="Clasificador de Mensajes", layout="centered")
st.title("Clasificador de Mensajes")
st.write("Clasifica mensajes en: Urgente, Moderado o Normal usando IA.")

mensaje = st.text_area("Escribe tu mensaje:", height=150)

if st.button("Clasificar"):
    if mensaje.strip() == "":
        st.warning("Por favor, escribe un mensaje.")
    else:
        try:
            response = requests.post("http://localhost:8000/clasificar", json={"texto": mensaje})
            st.write("Código de respuesta:", response.status_code)
            st.write("Respuesta JSON:", response.json())
            if response.status_code == 200:
                resultado = response.json()
                # Revisa si la clave existe antes de mostrar
                if "clasificacion" in resultado:
                    st.success(f" Clasificación: {resultado['clasificacion']} (Confianza: {resultado['confianza']:.2f})")
                else:
                    st.error(" La respuesta no contiene la clave 'clasificacion'.")


            else:
                st.error(" Error al clasificar el mensaje.")
        except Exception as e:
            st.error(f" No se pudo conectar al servidor FastAPI.\n\n{e}")