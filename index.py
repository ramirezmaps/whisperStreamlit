import streamlit as st
import whisper

st.title("App Whisper")
carga_audio = st.file_uploader("upload Audio",type=["mp3","wav"])

model = whisper.load_model("base")
st.text("Modelo Whisper Cargando")

if st.sidebar.button("Transcribe audio"):
    if carga_audio is not None:
        st.sidebar.success("Transcribiendo Audio")
        transcripcion = model.transcribe(carga_audio.name)
        st.sidebar.success("Transcripcion completa")
        st.markdown(transcripcion["text"])
    else:
        st.sidebar.error("Carga tu archivo de audio")
st.sidebar.header("Escuchar audio original")
st.sidebar.audio(carga_audio)

# app corriendo