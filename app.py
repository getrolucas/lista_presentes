import streamlit as st
import pandas as pd
import time
from streamlit_gsheets import GSheetsConnection

st.cache_data.clear()

# criando conexão ao "banco"
conn = st.connection("gsheets", type=GSheetsConnection)

# query
sql = '''
SELECT 
    "nome", 
    "item" 
FROM
    dados
WHERE
   "item" IS NOT NULL
'''

# lendo dados do "banco"
df_selecionados = conn.query(sql=sql)

# dados estaticos
df_lista = pd.read_csv("lista.csv")

# quantidade atual de cada item selecionado
atual = df_selecionados["item"].value_counts()

# função para limpar itens já selecionados
def ajustar_quantidades(i):
    if i['item'] in atual:
        return i['quantidade'] - atual[i['item']]
    else:
        return i['quantidade']

# Aplicando a função ao primeiro DataFrame
df_lista['quantidade'] = df_lista.apply(ajustar_quantidades, axis=1)

# dados para selectbox
presentes = df_lista[df_lista["quantidade"] > 0]["item"].to_list()

# interface do Streamlit
text = "&#127774 &#127802 Chá da Luísa &#127799 &#127803"

st.markdown(
    f"<h1 style='text-align: center; color: red;'>{text}</h1>", 
    unsafe_allow_html=True
)

# seleção dos valores para as duas colunas
st.subheader("Escreva seu nome")
nome = st.text_input('',None, placeholder="Obrigatório")

st.subheader("Selecione um presentinho")
item_selecionado = st.selectbox('', presentes, placeholder="Escolha uma opção")

# Botão para salvar
if st.button("Enviar"):
    if nome:
        dados = pd.DataFrame({"nome":[nome], "item":[item_selecionado]})
        data_update = pd.concat((df_selecionados, dados), ignore_index=True)
        conn.update(data=data_update)

        st.success(
            f"{nome}, sua opção {item_selecionado} foi enviada para os papais. \n Aguardamos você!")
    
        time.sleep(5)
        st.cache_data.clear()
        st.rerun()
        
    else:
        st.warning("Insira seu nome", icon="⚠️")