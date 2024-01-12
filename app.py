import pandas as pd
import streamlit as st
import plotly.express as px


# Titulo
st.set_page_config(page_title="graficando", 
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Map-circle-blue.svg/1024px-Map-circle-blue.svg.png",
                   initial_sidebar_state="expanded", layout="wide"
                   )
st.title('Contagem de Segmentos de Empresas')



top_segmentos = pd.read_csv('./dataset/top-segmentos.csv', sep=';', encoding='ISO-8859-1')
top_segmentos = top_segmentos.sort_values(by='Contas', ascending=False)
top_rotatividade = pd.read_csv('./dataset/top-rotatividade.csv', sep=';', encoding='ISO-8859-1')
top_rotatividade = top_rotatividade.sort_values(by='Média Mensal', ascending=False)



# Center
table_top_segmentos, table_top_rotatividade = st.tabs(["Segmentos ", "Rotatividade"])


with table_top_segmentos:
    st.write("Contagem das contas abertas por segmento.")
    st.dataframe(top_segmentos, hide_index=True, width=1200)

with table_top_rotatividade:
    st.write("Média aritmédica da quantidade de contas abertas por cada segmento. Maior média indica maior rotatividade.")
    st.dataframe(top_rotatividade, hide_index=True, width=1200)



#python -m streamlit run app.py