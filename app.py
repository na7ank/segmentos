import pandas as pd
import streamlit as st
import plotly.express as px


# Titulo
st.set_page_config(page_title="tabelas", 
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Map-circle-blue.svg/1024px-Map-circle-blue.svg.png",
                   initial_sidebar_state="expanded", layout="wide"
                   )
st.title('Contagem de Segmentos de Empresas')
st.write('**2017-07-29    -    2023-09-20**')

hidden = """
            <style>
            .reportview-container .main footer {visibility: hidden;}
            #MainMenu {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            footer {display: none !important;}
            header {visibility: hidden !important;}
            </style>
            """
st.markdown(hidden, unsafe_allow_html=True)

top_segmentos = pd.read_csv('./dataset/top-segmentos.csv', sep=';', encoding='ISO-8859-1')
top_segmentos = top_segmentos.sort_values(by='Contas', ascending=False)
top_rotatividade = pd.read_csv('./dataset/top-rotatividade.csv', sep=';', encoding='ISO-8859-1')
top_rotatividade = top_rotatividade.sort_values(by='Média Mensal', ascending=False)



table_top_segmentos, table_top_rotatividade = st.tabs(["Segmentos ", "Rotatividade"])

with table_top_segmentos:
    st.write("**Total de Contas:** Contagem das contas abertas por segmento.")
    # Adiciona um gradiente de fundo à tabela com base nos valores da coluna 'Contas'
    st.dataframe(top_segmentos, width=1200, hide_index=True)

with table_top_rotatividade:
    st.write("**Médias:** Média aritmédica da quantidade de contas abertas por cada segmento de empresa. Maior média indica maior rotatividade.")

    # Adiciona um gradiente de fundo à tabela com base nos valores da coluna 'Média Mensal'
    st.dataframe(top_rotatividade, width=1200, hide_index=True)
#python -m streamlit run app.py