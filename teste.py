
import streamlit as st

st.set_page_config(page_title="Perfil - Douglas Alves", layout="centered")

st.markdown(
    """
    <a href="https://www.tesla.com/about" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e8/Tesla_logo.png" width="200">
    </a>
    """,
    unsafe_allow_html=True
)

st.title("Douglas Alves")

descricao = st.text_area(
    "Curiosidades sobre mim:",
    "Fale sobre seus interesses, objetivos e habilidades..."
)

st.subheader("Seu texto:")


col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "https://upload.wikimedia.org/wikipedia/en/d/d7/Harry_Potter_character_poster.jpg",
        width=200
    )

with col2:
    st.write(descricao)
