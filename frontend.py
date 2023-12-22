import streamlit as st
from b_test import responder_pregunta_usuario

def main():
    
    st.title("GPT legal personalizado")


    st.session_state.user = getattr(st.session_state, 'user', '')
    st.session_state.respuesta = getattr(st.session_state, 'respuesta', '')

    nombre_documento = st.file_uploader("Selecciona un archivo PDF", type="pdf")
    pregunta = st.text_input("¿En qué te puedo ayudar?", value=st.session_state.user)

    if nombre_documento is not None:
        st.success("Documento subido correctamente: {}".format(nombre_documento.name))

    if st.button("Consultar"):
        if pregunta and nombre_documento:
            st.session_state.respuesta = responder_pregunta_usuario(pregunta, nombre_documento)
            st.session_state.user = ''
        else:
            st.warning("Por favor, ingresa la pregunta y selecciona un archivo PDF.")

    if st.session_state.respuesta:
        st.subheader("Respuesta:")
        st.write(st.session_state.respuesta)

if __name__ == "__main__":
    main()

