import streamlit as st

st.set_page_config(page_title="Perfil - Douglas Alves", layout="centered")

st.image("https://upload.wikimedia.org/wikipedia/commons/e/e8/Tesla_logo.png", width=200)

st.title("Douglas Alves")

# Campo para texto descritivo
descricao = st.text_area(
    "Escreva um texto sobre você:",
    "Fale sobre seus interesses, objetivos e habilidades..."
)

# Mostrar o texto digitado
if descricao:
    st.subheader("Seu texto:")
    st.write(descricao)
st.image("harrypotter.jpg")
st.write("Site Douglas")
st.link_button("Acessar", "https://sites.google.com/academico.ifpb.edu.br/douglas-antonio-info/in%C3%ADcio")
