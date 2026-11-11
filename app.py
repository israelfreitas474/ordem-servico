import streamlit as st
from datetime import date, time

st.set_page_config(page_title="Ordem de Serviço", page_icon="🧾")
st.title("🧾 Minha Ordem de Serviço")

# --- CLIENTE ---
nome = st.text_input("Nome do Cliente")
telefone = st.text_input("Telefone / WhatsApp")

# --- ENDEREÇO ---
st.markdown("### 📍 Endereço")
tipo_residencia = st.selectbox("Tipo de Residência", ["Casa", "Apartamento", "Comércio", "Outro"])

col_end1, col_end2 = st.columns([3, 1])
with col_end1:
    endereco = st.text_input("Endereço / Rua", placeholder="Ex: Rua das Flores")
with col_end2:
    numero = st.text_input("Número", placeholder="Ex: 123")

col_end3, col_end4 = st.columns(2)
with col_end3:
    bairro = st.text_input("Bairro", placeholder="Ex: Centro")
with col_end4:
    complemento = st.text_input("Complemento / Bloco / Apto", placeholder="Ex: Bloco B, Apto 201")

# --- SERVIÇO ---
st.markdown("### 🛠️ Serviço")
tipo = st.selectbox("Tipo de Serviço", ["Limpeza", "Instalação", "Manutenção", "Conserto", "Orçamento"])
aparelho = st.selectbox("Aparelho", ["Split 9000 BTU", "Split 12000 BTU", "Split 18000 BTU", "Split 24000 BTU", "Janela", "Outro"])

# --- QUANTIDADE (NOVO!) ---
quantidade = st.number_input("Quantidade de Equipamentos", min_value=1, value=1, step=1)
st.caption(f"Você vai limpar {quantidade} equipamento(s)")

# --- DATA E VALOR ---
col1, col2 = st.columns(2)
with col1:
    data_servico = st.date_input("Data do Serviço", value=date.today(), format="DD/MM/YYYY")
with col2:
    hora = st.time_input("Hora", value=time(11, 0))

col3, col4 = st.columns(2)
with col3:
    valor_unitario = st.number_input("Valor por Equipamento R$", min_value=0.0, value=0.0, step=10.0, format="%.2f")
with col4:
    pagamento = st.selectbox("Forma de Pagamento", ["Pix", "Dinheiro", "Cartão Crédito", "Cartão Débito", "A Pagar"])

# Calcula total sozinho
valor_total = valor_unitario * quantidade

observacoes = st.text_area("Observações")

# --- GERAR ---
if st.button("Gerar Ordem de Serviço", type="primary"):
    if not nome:
        st.warning("Preencha o nome do cliente!")
    else:
        st.success("OS Gerada com sucesso!")
        data_formatada = data_servico.strftime("%d/%m/%Y")
        hora_formatada = hora.strftime("%H:%M")
        valor_unit_fmt = f"R$ {valor_unitario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        valor_total_fmt = f"R$ {valor_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        st.markdown("---")
        st.markdown(f"### 🧾 Ordem de Serviço")
        st.markdown(f"**Cliente:** {nome}")
        st.markdown(f"**Telefone:** {telefone}")
        st.markdown(f"**Endereço:** {tipo_residencia} - {endereco}, Nº {numero} - {bairro}")
        if complemento:
            st.markdown(f"**Complemento:** {complemento}")
        st.markdown(f"**Serviço:** {tipo} - {aparelho}")
        st.markdown(f"**Quantidade:** {quantidade} equipamento(s)")
        st.markdown(f"**Data:** {data_formatada} às {hora_formatada}")
        st.markdown(f"**Valor por equipamento:** {valor_unit_fmt}")
        st.markdown(f"**Valor Total:** {valor_total_fmt}")
        st.markdown(f"**Pagamento:** {pagamento}")
        st.markdown(f"**Observações:** {observacoes}")
        st.markdown("---")
