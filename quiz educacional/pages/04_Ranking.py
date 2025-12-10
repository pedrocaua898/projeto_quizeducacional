import streamlit as st
import json
import os

#funçao para carregar o rank
def carregar_ranking():
    if os.path.exists("ranking.json"):
        with open("ranking.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

#mostra o título
st.title("Ranking Geral")
ranking = carregar_ranking()

if ranking:
    #ordena de forma decrescente
    ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

    #mostra na tabela o usuario, posiçao, materia, dificuldade
    st.markdown(
        """
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                text-align: left;
                padding: 8px;
                border-bottom: 1px solid #ddd;
            }
            th {
                background-color: #1E3A8A;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <table>
            <tr>
                <th>Posição</th>
                <th>Usuário (Matéria, Dificuldade)</th>
                <th>Pontuação</th>
            </tr>
            {"".join([f"<tr><td>{i+1}</td><td>{usuario}</td><td>{pontuacao}</td></tr>" for i, (usuario, pontuacao) in enumerate(ranking_ordenado)])}
        </table>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("Nenhum usuário no ranking ainda!")

#botao para voltar
if st.button("Voltar ao Início"):
    st.switch_page("pages/01_Início.py")
