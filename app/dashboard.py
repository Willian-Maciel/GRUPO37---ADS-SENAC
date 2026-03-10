import streamlit as st
import pandas as pd
import os

# 1. Título da aba do navegador e layout
st.set_page_config(page_title="ADS - Dashboard Financeiro", layout="wide")

# 2. Lógica de caminhos (Garante que o Git encontre a pasta data)
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
pasta_projeto = os.path.dirname(diretorio_atual)
caminho_csv = os.path.join(pasta_projeto, 'data', 'base_tratada.csv')

# Título do Dashboard
st.title("Análise de Pagamentos - Brasil")
st.markdown("Este dashboard apresenta a evolução dos meios de pagamento processados pelo script de ETL.")

# 3. Carregar e mostrar os dados
if os.path.exists(caminho_csv):
    df = pd.read_csv(caminho_csv)
    df['data'] = pd.to_datetime(df['data']) # Converte para data real

    # Gráfico principal
    st.subheader("Evolução Mensal (Valor Total)")
    st.line_chart(data=df, x='data', y='valor_total')

    # Métricas rápidas (Para impressionar o professor)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Maior Valor Mensal", f"R$ {df['valor_total'].max():,.2f}")
    with col2:
        st.metric("Média de Movimentação", f"R$ {df['valor_total'].mean():,.2f}")

else:
    st.error(f"Arquivo não encontrado em: {caminho_csv}. Certifique-se de rodar o src/etl.py primeiro!")
