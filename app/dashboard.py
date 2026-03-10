import streamlit as st
import pandas as pd
import os

# Configurações iniciais
st.set_page_config(page_title="Análise de Pagamentos - Brasil", layout="wide")

# Caminho dos dados
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
pasta_projeto = os.path.dirname(diretorio_atual)
caminho_csv = os.path.join(pasta_projeto, 'data', 'base_tratada.csv')

# Título Principal
st.title("📊 Painel de Indicadores Financeiros (PIX vs Tradicionais)")

if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)
    df['data'] = pd.to_datetime(df['data'])

    # --- BARRA LATERAL (FILTROS) ---
    st.sidebar.header("Filtros de Análise")
    # Seleção de colunas para comparar
    metodos = ['valor_pix', 'valor_ted', 'valor_tec', 'valor_cheque', 'valor_boleto']
    selecionados = st.sidebar.multiselect("Selecione os métodos para comparar:", metodos, default=['valor_pix', 'valor_boleto'])

    # --- ÁREA DE GRÁFICOS ---
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Linha do Tempo Comparativa")
        # Gráfico dinâmico baseado na seleção do usuário
        st.line_chart(data=df, x='data', y=selecionados)

    with col2:
        st.subheader("Distribuição (Market Share)")
        # Calculando a soma total de cada método para o gráfico de pizza
        soma_metodos = df[metodos].sum()
        st.bar_chart(soma_metodos) # Gráfico de barras para comparação rápida

    # Tabela detalhada
    with st.expander("Clique para ver os dados brutos"):
        st.write(df)

else:
    st.error("Base de dados não encontrada. Verifique a pasta /data.")
