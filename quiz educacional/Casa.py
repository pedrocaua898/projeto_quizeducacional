import streamlit as st
import os
import base64

# configuraçoes da pagina
st.set_page_config(
    page_title="Quiz educacional NEP",
    page_icon="🎓",
    layout="centered"
)

# funçao usada para carregar a logo da pagina
def get_image_base64(path):
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except FileNotFoundError:
        st.error(f"Arquivo '{path}' não encontrado! Verifique:")
        st.error("1. O arquivo está na mesma pasta do Casa.py?")
        st.error("2. O nome está correto (incluindo maiúsculas/minúsculas)?")
        st.stop()

# verificaçao da logo
logo_path = "logo.png"
if not os.path.exists(logo_path):
    st.error(f"Arquivo '{logo_path}' não encontrado!")
    st.info("Por favor, salve a logo como 'logo.png' na pasta raiz do projeto.")
    st.stop()

# estilo de botao em CSS
st.markdown(
    """
    <style>
        .header {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 2rem;
        }
        .header img {
            width: 80px;
            border-radius: 10px;
        }
        .header h1 {
            color: #1E3A8A;
            margin: 0;
        }
        .content {
            text-align: center;
            max-width: 600px;
            margin: 0 auto;
            padding: 1rem;
        }
        .start-button {
            background-color: #1E3A8A !important;
            color: white !important;
            font-size: 1.1rem !important;
            padding: 0.5rem 1rem !important;
            border-radius: 8px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# logo e titulo no estilo header
logo_base64 = get_image_base64(logo_path)
st.markdown(
    f"""
    <div class="header">
        <img src="data:image/png;base64,{logo_base64}">
        <h1>NEP Quiz Educacional</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# conteudo principal da pagina
st.markdown(
    """
    <div class="content">
        <p>Bem-vindo ao <strong>Quiz Educacional</strong>! Teste seus conhecimentos em:</p>
        <ul style="text-align: left; display: inline-block;">
            <li>Matemática</li>
            <li>Português</li>
            <li>Geografia</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# botao de iniciar o quiz, alternando de pagina
if st.button("Começar Quiz", key="start", use_container_width=True):
    st.switch_page("pages/01_Início.py")

st.write("Feito por Nicolas, Eduardo e Pedro Cauã (NEP)")