import streamlit as st
import pandas as pd
import os

# Configurações iniciais
st.set_page_config(page_title="Análise de Pagamentos - Brasil", layout="wide")

# LÓGICA DE CAMINHO AJUSTADA PARA O GITHUB/STREAMLIT CLOUD
# Esta linha garante que ele ache a pasta 'data' na raiz do repositório
caminho_csv = os.path.join(os.getcwd(), 'data', 'base_tratada.csv')

# Título Principal
st.title("Painel de Indicadores Financeiros (PIX vs Tradicionais)")

if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)
    df['data'] = pd.to_datetime(df['data'])

    # --- BARRA LATERAL (FILTROS) ---
    st.sidebar.header("Filtros de Análise")
    metodos = ['valor_pix', 'valor_ted', 'valor_tec', 'valor_cheque', 'valor_boleto']
    selecionados = st.sidebar.multiselect("Selecione os métodos:", metodos, default=['valor_pix', 'valor_boleto'])

    # --- ÁREA DE GRÁFICOS ---
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Linha do Tempo Comparativa")
        st.line_chart(data=df, x='data', y=selecionados)

    with col2:
        st.subheader("Distribuição (Volume Acumulado)")
        soma_metodos = df[metodos].sum()
        st.bar_chart(soma_metodos)

    with st.expander("Clique para ver os dados brutos"):
        st.write(df)
else:
    # Mensagem de erro amigável com o caminho que ele tentou ler
    st.error(f"Erro: Não encontrei o arquivo em: {caminho_csv}")
    st.info("Verifique se o arquivo 'base_tratada.csv' está na pasta 'data' do seu GitHub.")
