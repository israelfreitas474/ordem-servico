import streamlit as st
import datetime

st.set_page_config(page_title="Ordem de Serviço", page_icon="❄️")
st.title("❄️ Minha Ordem de Serviço")
st.write("Preencha os dados para gerar uma nova OS")

nome = st.text_input("Nome do Cliente")
telefone = st.text_input("Telefone")
endereco = st.text_input("Endereço")
tipo = st.selectbox("Tipo de Serviço", ["Manutenção", "Instalação", "Limpeza", "Suporte Técnico"])
aparelho = st.selectbox("Aparelho", ["Split 9000 BTU", "Split 12000 BTU", "Split 18000 BTU", "Janela", "Cassete"])
data = st.date_input("Data do Serviço", datetime.date.today())
obs = st.text_area("Observações")

if st.button("Gerar Ordem de Serviço"):
    if nome == "":
        st.error("Preencha o nome do cliente!")
    else:
        st.success("OS Gerada com sucesso!")
        st.markdown("---")
        st.subheader(f"OS - {nome}")
        st.write(f"**Cliente:** {nome}")
        st.write(f"**Telefone:** {telefone}")
        st.write(f"**Endereço:** {endereco}")
        st.write(f"**Serviço:** {tipo} - {aparelho}")
        st.write(f"**Data:** {data}")
        st.write(f"**Observações:** {obs}")
        st.balloons()