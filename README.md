# GRUPO 37 - ADS SENAC

# Projeto Integrador: Desenvolvimento Low Code em Ciência de Dados

**Curso:** Análise e Desenvolvimento de Sistemas (SENAC)

**Grupo:** 37

**Integrante:** Willian da Silva Maciel

---

## 1. Tema do Projeto

Análise da evolução dos métodos de pagamento no Brasil, com foco na transição tecnológica para o PIX e a redução do uso de modalidades tradicionais.

## 2. Definição da Base de Dados

* **Fonte:** [Brazilian Payment Methods - Kaggle](https://www.kaggle.com/datasets/clovisdalmolinvieira/brazilian-payment-methods).
* **Contexto:** Registros mensais do volume financeiro transacionado via PIX, Boletos, TED, DOC e Cheques.
* **Objetivo da Análise:** Identificar padrões de comportamento do consumidor brasileiro e a velocidade de adoção de novas tecnologias financeiras.

## 3. Estrutura do Repositório

* **/app**: Interface visual desenvolvida com Streamlit (`dashboard.py`).
* **/data**: Base de dados original (`pagamentos_brasil.csv`) e base tratada (`base_tratada.csv`).
* **/src**: Script de automação ETL (`etl.py`).
* **requirements.txt**: Lista de dependências para configuração do ambiente de execução.

## 4. Instruções para Execução

### 1. Instalação de Dependências

No terminal, na raiz do projeto, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt

```

### 2. Processamento de Dados (ETL)

Para executar a limpeza, tradução e normalização das séries temporais:

```bash
python src/etl.py

```

### 3. Visualização do Dashboard

Para iniciar a interface interativa no navegador:

```bash
streamlit run app/dashboard.py

```

## 5. Status do Planejamento

* [x] Criação e estruturação do repositório no GitHub.
* [x] Download e upload da base de dados (.csv).
* [x] Limpeza de dados e tratamento de séries temporais com Python.
* [x] Estruturação da pasta app e dashboard inicial.

## 6. Visualizações e Métricas

O dashboard apresenta uma linha do tempo comparativa, permitindo visualizar o volume total transacionado e a evolução das modalidades de pagamento ao longo dos meses. O foco principal é a métrica de valor total acumulado por período.
