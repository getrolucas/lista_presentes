import streamlit as st
import pandas as pd
import csv
import time
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()


st.write(df)

# Interface do Streamlit
st.title(":sun_with_face: :hibiscus: :gray[Chá da Luísa] :sunflower: :blossom:")

'''
# Seleção dos valores para as duas colunas
st.subheader("Escreva seu nome")
nome = st.text_input('',None, placeholder="Obrigatório")

st.subheader("Selecione um presentinho")
selec_presentes = st.selectbox('', presentes, placeholder="Escolha uma opção")

# Função para escrever no arquivo CSV
def salvar_dados(nome, presente):
    with open("selecionados.csv", "a", newline="") as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow([nome, presente])

# Botão para salvar
if st.button("Enviar"):
    if nome:
        salvar_dados(nome, selec_presentes)
        st.success(f"{nome}, suas opção {selec_presentes} foi enviada para os papais")
        lista.loc[selec_presentes, "quantidade"] = lista.loc[selec_presentes, "quantidade"] - 1
        lista.to_csv("lista.csv")
        
        time.sleep(3)
        st.rerun()
        
    else:
        st.warning("Insira seu nome", icon="⚠️")

'''