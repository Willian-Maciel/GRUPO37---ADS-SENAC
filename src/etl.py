import pandas as pd

# 1. Carregar os dados originais (o arquivo que você subiu no GitHub)
df = pd.read_csv('../data/pagamentos_brasil.csv')

# 2. Dicionário de Tradução
# Vamos mudar os nomes das colunas de inglês para português
traducao = {
    'YearMonth': 'ano_mes',
    'valuePix': 'valor_pix',
    'valueTED': 'valor_ted',
    'valueTEC': 'valor_tec',
    'valueBankCheck': 'valor_cheque',
    'valueBrazilianBoletoPayment': 'valor_boleto'
}
df.rename(columns=traducao, inplace=True)

# 3. Criar a coluna de Valor Total (Soma de todos os métodos)
# Aqui o Python soma linha por linha os valores de cada coluna
colunas_valor = ['valor_pix', 'valor_ted', 'valor_tec', 'valor_cheque', 'valor_boleto']
df['valor_total'] = df[colunas_valor].sum(axis=1)

# 4. Ajustar o formato da data (essencial para os gráficos futuros)
# Transforma '202405' em uma data que o computador entende
df['data'] = pd.to_datetime(df['ano_mes'].astype(str), format='%Y%m')

# 5. Salvar o resultado final na pasta data
df.to_csv('../data/base_tratada.csv', index=False)

print("Sucesso! Criamos o arquivo 'base_tratada.csv' com a soma total.")
