import streamlit as st
import time
from random import sample

#banco de perguntas (nicolas)
PERGUNTAS = {
    "Matemática": {
        "Fácil": [
            {"pergunta": "Quanto é 2 + 2?", "opcoes": ["3", "4", "5"], "resposta": "4"},
            {"pergunta": "Qual é a raiz quadrada de 9?", "opcoes": ["2", "3", "4"], "resposta": "3"},
            {"pergunta": "Quanto é 5 × 6?", "opcoes": ["25", "30", "35"], "resposta": "30"},
        ],
        "Médio": [
            {"pergunta": "Quanto é 7 × 8?", "opcoes": ["48", "56", "64"], "resposta": "56"},
            {"pergunta": "Qual é o valor de π (pi) arredondado?", "opcoes": ["3.14", "3.16", "3.18"], "resposta": "3.14"},
            {"pergunta": "Qual é a área de um quadrado com lado 5?", "opcoes": ["20", "25", "30"], "resposta": "25"},
        ],
        "Difícil": [
            {"pergunta": "Qual é a derivada de x²?", "opcoes": ["x", "2x", "x³"], "resposta": "2x"},
            {"pergunta": "Qual é o resultado de 15²?", "opcoes": ["200", "225", "250"], "resposta": "225"},
            {"pergunta": "Qual é a soma dos ângulos internos de um triângulo?", "opcoes": ["180°", "270°", "360°"], "resposta": "180°"},
        ],
    },
    "Português": {
        "Fácil": [
            {"pergunta": "Qual é o plural de 'cão'?", "opcoes": ["cãos", "cães", "cãezes"], "resposta": "cães"},
            {"pergunta": "Qual é o antônimo de 'feliz'?", "opcoes": ["alegre", "triste", "contente"], "resposta": "triste"},
            {"pergunta": "Qual é o feminino de 'leão'?", "opcoes": ["leoa", "leãoa", "leonina"], "resposta": "leoa"},
        ],
        "Médio": [
            {"pergunta": "Qual é o sujeito da frase: 'Choveu muito ontem'?", "opcoes": ["Chuva", "Ontem", "Indeterminado"], "resposta": "Indeterminado"},
            {"pergunta": "Qual é o tempo verbal de 'eu estudarei'?", "opcoes": ["Presente", "Futuro", "Pretérito"], "resposta": "Futuro"},
            {"pergunta": "Qual é a classe gramatical de 'rapidamente'?", "opcoes": ["Adjetivo", "Advérbio", "Substantivo"], "resposta": "Advérbio"},
        ],
        "Difícil": [
            {"pergunta": "Qual é a figura de linguagem em 'A vida é um palco'?", "opcoes": ["Metáfora", "Hipérbole", "Ironia"], "resposta": "Metáfora"},
            {"pergunta": "Qual é o plural de 'mal'?", "opcoes": ["males", "mais", "mals"], "resposta": "males"},
            {"pergunta": "Qual é o correto: 'Se eu ver' ou 'Se eu vir'?", "opcoes": ["Se eu ver", "Se eu vir", "Ambos"], "resposta": "Se eu vir"},
        ],
    },
    "Geografia": {
        "Fácil": [
            {"pergunta": "Qual é a capital do Brasil?", "opcoes": ["Rio de Janeiro", "São Paulo", "Brasília"], "resposta": "Brasília"},
            {"pergunta": "Qual é o maior planeta do sistema solar?", "opcoes": ["Terra", "Júpiter", "Saturno"], "resposta": "Júpiter"},
            {"pergunta": "Qual é o oceano que banha o Brasil?", "opcoes": ["Atlântico", "Pacífico", "Índico"], "resposta": "Atlântico"},
        ],
        "Médio": [
            {"pergunta": "Qual é o rio mais longo do mundo?", "opcoes": ["Amazonas", "Nilo", "Yangtzé"], "resposta": "Nilo"},
            {"pergunta": "Qual é o país com a maior população?", "opcoes": ["Índia", "China", "EUA"], "resposta": "Índia"},
            {"pergunta": "Qual é o maior deserto da Ásia?", "opcoes": ["Gobi", "Saara", "Kalahari"], "resposta": "Gobi"},
        ],
        "Difícil": [
            {"pergunta": "Qual é o ponto mais alto da Terra?", "opcoes": ["Monte Everest", "K2", "Kilimanjaro"], "resposta": "Monte Everest"},
            {"pergunta": "Qual é o maior deserto do mundo?", "opcoes": ["Saara", "Antártida", "Gobi"], "resposta": "Antártida"},
            {"pergunta": "Qual é o país com mais fusos horários?", "opcoes": ["Rússia", "França", "EUA"], "resposta": "França"},
        ],
    },
}

#exibe as funçoes com o tempo
def mostrar_pergunta(pergunta, index):
    st.subheader(f"Pergunta {index + 1}: {pergunta['pergunta']}")
    opcoes = pergunta["opcoes"]

    #define o tempo limite com base na dificuldade
    if st.session_state.dificuldade == "Fácil":
        tempo_limite = 15
    elif st.session_state.dificuldade == "Médio":
        tempo_limite = 20
    else:
        tempo_limite = 30

    timer_placeholder = st.empty()
    resposta_placeholder = st.empty()

    #a variavel começa sem valor para o usuario inserir/escolher um
    resposta = None
    #loop pra atualizar o timer
    for segundos_restantes in range(tempo_limite, 0, -1):
        timer_placeholder.write(f"Tempo restante: {segundos_restantes} segundos")

        #exibe as respostas disponiveis
        with resposta_placeholder.container():
            resposta = st.radio(
                "Escolha a resposta:",
                opcoes,
                key=f"pergunta_{index}_radio"
            )

        #caso o usuario responda, ele sai do loop
        if resposta:
            break
        time.sleep(1)

    
    if not resposta:
        timer_placeholder.error("Tempo esgotado!") #verifica se o tempo acabou
        resposta = None #se tiver acabado, a variavel (resposta) estara vazia, resultando no erro da questao

    return resposta
def quiz():
    #verifica se as variaveis estao definidas
    if "materia" not in st.session_state or "dificuldade" not in st.session_state:
        st.error("Matéria ou dificuldade não selecionadas. Redirecionando para o início...")
        time.sleep(2)
        st.switch_page("pages/01_Início.py")
        return
    if "perguntas" not in st.session_state:
        st.session_state.perguntas = sample(
            PERGUNTAS[st.session_state.materia][st.session_state.dificuldade],
            3
        )
        st.session_state.pontuacao = 0
        st.session_state.pergunta_atual = 0
    # faz o streamlit ver se ainda tem perguntas sobrandop
    if st.session_state.pergunta_atual >= len(st.session_state.perguntas):
        st.switch_page("pages/03_Resultado.py")
        return
    pergunta = st.session_state.perguntas[st.session_state.pergunta_atual]
    resposta = mostrar_pergunta(pergunta, st.session_state.pergunta_atual)
    if st.button("Próxima"):
        if resposta == pergunta["resposta"]:
            st.session_state.pontuacao += 1
            st.success("Correto!")
        else:
            st.error(f"Errado! A resposta correta era: {pergunta['resposta']}")

        st.session_state.pergunta_atual += 1

        if st.session_state.pergunta_atual >= len(st.session_state.perguntas):
            st.switch_page("pages/03_Resultado.py")
        else:
            st.rerun()
#abre/executa o quiz
if __name__ == "__main__":
    quiz()
