import streamlit as st
import json
import os
import time

#funçao para carregar o rank do banco de dados
def carregar_ranking():
    if os.path.exists("ranking.json"):
        with open("ranking.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

#funçao para salvar o rank atual
def salvar_ranking(ranking):
    with open("ranking.json", "w", encoding="utf-8") as f:
        json.dump(ranking, f, ensure_ascii=False, indent=4)

#verifica se ha informações na variável
if "pontuacao" not in st.session_state:
    st.error("Pontuação não encontrada. Redirecionando para o início...")
    time.sleep(2)
    st.switch_page("pages/01_Início.py")
else:
    #exibe o resultado
    st.title("🎉 Resultado do Quiz")
    pontuacao = st.session_state.pontuacao
    total_perguntas = len(st.session_state.perguntas)
    st.write(f"Você acertou {pontuacao} de {total_perguntas} perguntas!")

    #atualiza o rank com materia e dificuldade
    ranking = carregar_ranking()
    chave_usuario = f"{st.session_state.nome_usuario} ({st.session_state.materia}, {st.session_state.dificuldade})"
    ranking[chave_usuario] = pontuacao
    salvar_ranking(ranking)

    #botoes de navegaçao
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Voltar ao Início"):
            st.session_state.clear()
            st.switch_page("pages/01_Início.py")
    with col2:
        if st.button("Ver Ranking"):
            st.switch_page("pages/04_Ranking.py")
