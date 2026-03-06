import pandas as pd

# 1. Carregar os dados (Ajustado para o nome que está no seu GitHub)
df = pd.read_csv('../data/pagamentos_brasil.csv')

# 2. Limpeza e Transformação
# Padroniza nomes das colunas (Ex: valuePix -> value_pix)
df.columns = [col.replace('value', 'valor_').replace('quantity', 'qtd_').lower() for col in df.columns]

# Converte YearMonth para data real
df['data'] = pd.to_datetime(df['yearmonth'].astype(str), format='%Y%m')

# 3. Salvar a base tratada para o Dashboard usar
df.to_csv('../data/base_tratada.csv', index=False)

print("Limpeza concluída! Arquivo base_tratada.csv gerado na pasta data.")
