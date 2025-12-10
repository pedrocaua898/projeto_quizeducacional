import streamlit as st

# verifica se o nome do usuario foi inserido
if "nome_usuario" not in st.session_state:
    st.session_state.nome_usuario = ""

# estilo css
st.markdown(
    """
    <style>
        .form-container {
            max-width: 500px;
            margin: 0 auto;
            padding: 2rem;
            background-color: #F9FAFB;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .form-title {
            text-align: center;
            color: #1E3A8A;
            margin-bottom: 1.5rem;
        }
        .stButton>button {
            width: 100%;
            background-color: #1E3A8A;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# formulação
st.markdown('<div class="form-container">', unsafe_allow_html=True)
st.markdown('<h2 class="form-title">Configurações do Quiz</h2>', unsafe_allow_html=True)

# campo de inserção do nome
nome = st.text_input("Digite seu nome:", value=st.session_state.nome_usuario)

# campo de seleçao de materia
materia = st.selectbox(
    "Escolha a matéria:",
    ["Matemática", "Português", "Geografia"]
)

#seleçao de dificuldade
dificuldade = st.selectbox(
    "Escolha a dificuldade:",
    ["Fácil", "Médio", "Difícil"]
)

#botao de iniciar quiz
if st.button("Iniciar Quiz"):
    if nome.strip() == "":
        st.error("Por favor, digite seu nome!")
    else:
        st.session_state.nome_usuario = nome
        st.session_state.materia = materia
        st.session_state.dificuldade = dificuldade
        st.switch_page("pages/02_Quiz.py")

st.markdown('</div>', unsafe_allow_html=True)