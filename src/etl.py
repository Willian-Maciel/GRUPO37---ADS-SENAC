import pandas as pd

# 1. Carregar os dados originais da pasta data
df = pd.read_csv('../data/base_original.csv')

# 2. Tratamento Low Code / Python
# Convertendo nomes de colunas para minúsculo e removendo espaços
df.columns = [col.strip().lower() for col in df.columns]

# Criando uma coluna de 'Total' para facilitar o Dashboard
metodos = ['pix', 'boleto', 'ted', 'doc', 'cheque']
# Garantimos que apenas as colunas existentes sejam somadas
colunas_presentes = [c for c in metodos if c in df.columns]
df['total_mensal'] = df[colunas_presentes].sum(axis=1)

# 3. Salvar a base tratada na mesma pasta
df.to_csv('../data/base_tratada.csv', index=False)

print("Sucesso: base_tratada.csv gerada!")
