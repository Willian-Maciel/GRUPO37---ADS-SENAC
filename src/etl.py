import pandas as pd

# 1. Carregar os dados originais
df = pd.read_csv('../data/pagamentos_brasil.csv')

# 2. Dicionário de Tradução (Limpeza e Padronização)
# Vamos trocar os nomes técnicos por nomes claros em português
traducao_colunas = {
    'YearMonth': 'ano_mes',
    'quantityPix': 'qtd_pix',
    'valuePix': 'valor_pix',
    'quantityTED': 'qtd_ted',
    'valueTED': 'valor_ted',
    'quantityTEC': 'qtd_tec',
    'valueTEC': 'valor_tec',
    'quantityBankCheck': 'qtd_cheque',
    'valueBankCheck': 'valor_cheque',
    'quantityBrazilianBoletoPayment': 'qtd_boleto',
    'valueBrazilianBoletoPayment': 'valor_boleto'
}

# Aplicando a renomeação
df.rename(columns=traducao_colunas, inplace=True)

# 3. Tratamento Extra: Converter 'ano_mes' para data real
# O formato original é 202405 (YYYYMM)
df['data'] = pd.to_datetime(df['ano_mes'].astype(str), format='%Y%m')

# 4. Salvar a base limpa e traduzida
df.to_csv('../data/base_tratada.csv', index=False)

print("Limpeza e Tradução concluídas! Arquivo 'base_tratada.csv' gerado.")
