import pandas as pd
import os

# 1. Definir o caminho para garantir que ele encontre a pasta 'data'
# Independente de onde o comando seja disparado, ele busca a pasta correta
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
pasta_projeto = os.path.dirname(diretorio_atual)

caminho_entrada = os.path.join(pasta_projeto, 'data', 'pagamentos_brasil.csv')
caminho_saida = os.path.join(pasta_projeto, 'data', 'base_tratada.csv')

# 2. Carregar os dados originais
try:
    df = pd.read_csv(caminho_entrada)
    print("Sucesso: Arquivo original carregado do GitHub!")
except FileNotFoundError:
    print(f"Erro: Não encontrei o arquivo em {caminho_entrada}")
    exit()

# 3. Dicionário de Tradução (Limpeza para o Dashboard)
traducao = {
    'YearMonth': 'ano_mes',
    'valuePix': 'valor_pix',
    'quantityPix': 'qtd_pix',
    'valueTED': 'valor_ted',
    'quantityTED': 'qtd_ted',
    'valueTEC': 'valor_tec',
    'valueBankCheck': 'valor_cheque',
    'valueBrazilianBoletoPayment': 'valor_boleto'
}
}
df.rename(columns=traducao, inplace=True)

# 4. Criar a coluna de Valor Total 
colunas_valor = ['valor_pix', 'valor_ted', 'valor_tec', 'valor_cheque', 'valor_boleto']
df['valor_total'] = df[colunas_valor].sum(axis=1)

# 5. Ajustar o formato da data
df['data'] = pd.to_datetime(df['ano_mes'].astype(str), format='%Y%m')

# 6. Salvar o resultado final na pasta data do Git
df.to_csv(caminho_saida, index=False)

print("-" * 30)
print("ETL CONCLUÍDO COM SUCESSO!")
print(f"O arquivo 'base_tratada.csv' foi gerado em: {caminho_saida}")
print("-" * 30)
