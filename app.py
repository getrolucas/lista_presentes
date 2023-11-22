import streamlit as st
import pandas as pd
import csv
import time

# lendo dados armazenados
lista = pd.read_csv("lista.csv", index_col="item", encoding="ANSI").query("quantidade > 0")

selecionados = pd.read_csv("selecionados.csv", encoding="ANSI")

# lista de valores para check_box
presentes = lista.index.to_list()

# Interface do Streamlit
st.title(":sun_with_face: :hibiscus: :gray[Chá da Luísa] :sunflower: :blossom:")

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

