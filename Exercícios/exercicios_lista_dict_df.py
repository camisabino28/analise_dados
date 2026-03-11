"""
Aula - Exercicios de Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados.

Requisito:
- Instalar pandas: pip install pandas

Regra da aula:
- Pense no DataFrame como uma planilha.
- Resolva um exercicio por vez.
"""
# -------------------------------------------------
# BLOCO 1: criar DataFrame e inspecionar estrutura
# -------------------------------------------------
import pandas as pd
dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}

# Exercicio 1:
# a) Crie o DataFrame df_vendas usando dados_vendas
df_vendas = pd.DataFrame(dados_vendas)

# b) Mostre as 5 primeiras linhas
df_vendas.head()

# c) Mostre o formato (linhas, colunas)
df_vendas.shape

# d) Mostre os tipos de dados das colunas
df_vendas.dtypes


# -------------------------------------------------
# BLOCO 2: selecionar colunas e linhas
# -------------------------------------------------

# Exercicio 2:
# a) Mostre apenas as colunas "mes" e "vendas"
df_vendas.loc[:, ["mes", "vendas"]]

# b) Mostre somente a primeira linha
df_vendas.head(1)
df_vendas.loc[0:0,]
# c) Mostre as linhas de indice 2 ate 4
df_vendas.loc[2:4,]

# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 3: filtros com condicoes de negocio
# -------------------------------------------------

# Exercicio 3:
# a) Filtre vendas acima de 12000
df_vendas.loc[df_vendas["vendas"] > 12000,]

# b) Filtre apenas a filial "Centro"
df_vendas.loc[df_vendas["filial"] == "Centro"]

# c) Filtre vendas acima de 11000 na filial "Norte"
df_vendas.loc[(df_vendas["vendas"] >= 11000) & (df_vendas["filial"] == "Norte")]
# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 4: novas colunas e metricas
# -------------------------------------------------

# Exercicio 4:
# a) Crie a coluna "ticket_medio" = vendas / clientes
df_vendas["ticket_medio"] = round(df_vendas["vendas"]/df_vendas["clientes"],2)

# b) Crie a coluna "meta_batida" com True para vendas >= 13000
df_vendas["meta_batida"] = df_vendas["vendas"] >= 13000
# c) Mostre apenas "filial", "mes", "ticket_medio", "meta_batida"
df_vendas.loc[:, ["filial", "mes", "ticket_medio", "meta_batida"]]


# -------------------------------------------------
# BLOCO 5: agregacao com groupby
# -------------------------------------------------

# Exercicio 5:
# a) Calcule total de vendas por filial
df_vendas.groupby("filial")["vendas"].sum()

# b) Calcule media de clientes por mes
df_vendas.groupby("mes")["clientes"].mean()
# c) Descubra a filial com maior total de vendas
teste = df_vendas.groupby("filial")["vendas"]
teste.idxmax()

# -------------------------------------------------
# BLOCO 6: ordenacao e ranking
# -------------------------------------------------

# Exercicio 6:
# a) Ordene df_vendas por "vendas" em ordem decrescente
df_vendas.sort_values(by='vendas', ascending=True)
# b) Pegue os 3 maiores resultados de vendas
df_vendas.sort_values(by='vendas', ascending=True).tail(3)

# opção 2: ascending = False e .head(3)

# c) Mostre um ranking com "filial", "mes", "vendas"
ranking = df_vendas.sort_values(by='vendas', ascending=False)[['filial', 'mes', 'vendas']]
# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 7: desafio final de analise
# -------------------------------------------------

# Exercicio 7 (desafio):
# 1) Gere um resumo por filial com:
#    - total_vendas
#    - media_ticket_medio
#    - total_clientes
df_vendas['ticket_medio'] = df_vendas['vendas'] / df_vendas['clientes']
resumo_filial = df_vendas.groupby('filial').agg({
    'vendas': 'sum',           
    'ticket_medio': 'mean',    
    'clientes': 'sum'          
})
# 2) Ordene o resumo por total_vendas (desc)
resumo_filial.sort_values(by='vendas', ascending=True)

# 3) Exiba qual filial teve melhor desempenho geral
resumo_filial.loc[resumo_filial["vendas"] == resumo_filial["vendas"].max(), ["vendas", "ticket_medio", "clientes"]]
# RESOLUCAO: complete aqui


# ===========================================================
# PARTE 1 – Estrutura lista + dicionário
# ===========================================================
import pandas as pd
dados_list_dict = [{
    "Column A":[1, 2, 3],
    "Column B":[4, 5, 6],
    "Column C":[7, 8, 9]
}]


# -----------------------------------------------------------
# EXERCÍCIO 1 – Explorando a estrutura
# -----------------------------------------------------------

# 1. Qual é o tipo de dados_list_dict?
type(dados_list_dict)

# 2. Qual é o tipo do primeiro elemento?
dic = dados_list_dict[0]
type(dic)
# 3. Como acessar a lista da "Column A"?
dic["Column A"]

# 4. Como acessar o segundo elemento da "Column C"?
dic["Column C"]

# -----------------------------------------------------------
# EXERCÍCIO 2 – Convertendo para DataFrame
# -----------------------------------------------------------
# 1. Converta dados_list_dict[0] em um DataFrame chamado df1
df1 = pd.DataFrame(dados_list_dict[0])

# 2. Mostre:
#    - shape
df1.shape

#    - tipos das colunas
df1.dtypes

# 3. Calcule:
#    - soma de cada coluna
df1.sum()
#    - média de cada coluna
df1.mean()

# -----------------------------------------------------------
# EXERCÍCIO 3 – Criando novas colunas
# -----------------------------------------------------------

# No df1:
# 1. Crie coluna "Total" = soma das colunas
df1["Total"] = df1.sum(axis=1)
# 2. Crie coluna "Media" = média por linha
colunas = ["Column A", "Column B", "Column C"]
df1["Media"] = df1[colunas].mean(axis=1)
# 3. Filtre linhas onde Total > 10
filtro = df1["Total"] >= 10
df1.loc[filtro, :]

# RESOLVA AQUI:



# -----------------------------------------------------------
# EXERCÍCIO 4 – Conversões estruturais
# -----------------------------------------------------------

# 1. Converta df1 para:
#    - lista de dicionários [ {linha1}, {linha2}, {linha3} ]
#    - dicionário de listas { coluna1: [valores], coluna2: [valores] }
# Dica:
# orient="records":
#   Cada elemento representa uma linha.
#   Estrutura ideal para APIs e JSON.
df1.to_dict(orient="records")
# orient="list":
#   Cada chave representa uma coluna.
#   Estrutura colunar, útil para reconstruir DataFrame.
df1.to_dict(orient="list")

# RESOLVA AQUI:


# -----------------------------------------------------------
# EXERCÍCIO 5 – Trabalhando com lista
# -----------------------------------------------------------

# 1. Transforme a coluna "Column A" em uma lista chamada lista_a.
lista_a = df1["Column A"].to_list()

# 2. Multiplique cada elemento da lista por 10.
lista_a_multiplicada = []
for x in lista_a:
    lista_a_multiplicada.append(x * 10)
    
# outra opção: lista_a = (df1["Column A"] * 10).to_list()

# 3. Crie uma nova coluna chamada "Column A x10" com essa nova lista.
df1["Column A x10"] = lista_a_multiplicada

# Forma mais eficiente: df1["Column A x10"] = df1["Column A"] * 10
# RESOLVA AQUI:



# ===========================================================
# BASE DE DADOS
# ===========================================================
import pandas as pd
dados = [
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 5000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 3000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 4000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 6000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-03", "valor": 7000},
]


# ===========================================================
# PARTE 1 – EXPLORAÇÃO INICIAL
# ===========================================================

# Exercício 1
# 1. Qual o tipo da variável dados?
type(dados)
# 2. Quantos registros existem?
len(dados)
# 3. Quais são as chaves do primeiro dicionário?
dados[0].keys()
# 4. Liste todos os países existentes (sem repetição).
paises = []
for dict in dados:
    nome = dict["nome_pais"]
    if nome not in paises:
     paises.append(nome)
# RESOLVA AQUI:



# ===========================================================
# PARTE 2 – CONVERSÃO PARA DATAFRAME
# ===========================================================

# Exercício 2
# 1. Converta dados para DataFrame chamado df
df = pd.DataFrame(dados)
# 2. Mostre shape, tipos e primeiras linhas
df.shape
df.dtypes
df.head()
# 3. Converta a coluna periodo para datetime
df["periodo"] = pd.to_datetime(df["periodo"])
# RESOLVA AQUI:



# ===========================================================
# PARTE 3 – FILTROS E ORDENAÇÃO
# ===========================================================

# Exercício 3 – Filtros
# 1. Filtre apenas Brasil
df.loc[df["nome_pais"] == "Brasil", :]
# 2. Filtre apenas Produto A
df.loc[df["descricao"] == "Produto A", :]
# 3. Filtre valor > 4000
df.loc[df["valor"] > 4000, :]
# 4. Combine Brasil + Produto A
df.loc[(df["nome_pais"] == "Brasil") & (df["descricao"] == "Produto A"), :]
# RESOLVA AQUI:


# Exercício 4 – Ordenação
# 1. Ordene por valor crescente
df.sort_values(by='valor', ascending=True)
# 2. Ordene por valor decrescente
df.sort_values(by='valor', ascending=False)
# 3. Ordene por periodo e depois por valor
df.sort_values(by=['periodo', 'valor'])
# RESOLVA AQUI:



# ===========================================================
# PARTE 4 – AGREGAÇÕES
# ===========================================================

# Exercício 5 – GroupBy Simples
# 1. Total exportado por país
df.groupby("nome_pais")["valor"].sum()
# 2. Total exportado por produto
df.groupby("descricao")["valor"].sum()
# 3. Média por país
df.groupby("nome_pais")["valor"].mean()
# 4. Quantidade de operações por país
df.groupby("nome_pais")["tipo_operacao"].count()
# RESOLVA AQUI:


# Exercício 6 – GroupBy Múltiplo
# Agrupe por nome_pais e descricao
# Calcule soma, média e contagem
df.groupby(['nome_pais', 'descricao'])['valor'].agg(['sum', 'mean', 'count'])
# Explique em comentário o que essa tabela representa

# Essa  permite identificar qual produto é o carro chefe de cada país 
# RESOLVA AQUI:



# ===========================================================
# PARTE 5 – PIVOT TABLE
# ===========================================================

# Exercício 7 – Pivot por Produto
# Linhas: periodo
# Colunas: descricao
# Valores: soma de valor

# Responda:
# 1. Qual produto vendeu mais?
tabela_pivot = df.pivot_table(index='periodo', 
                              columns='descricao', 
                              values='valor', 
                              aggfunc='sum')

somas = tabela_pivot.sum()
somas.idxmax()

# 2. Qual mês teve maior valor total?
tabela_pivot.sum(axis = 1).idxmax()

# 3. Existe mês sem venda?
tabela_pivot.isna()

# Sim, em março o produto B nao vendeu
# RESOLVA AQUI:


# Exercício 8 – Pivot por País
# Linhas: periodo
# Colunas: nome_pais
# Valores: soma de valor

# Explique o que podemos interpretar dessa tabela

# RESOLVA AQUI:
tabela_pivot_2 = df.pivot_table(index='periodo', 
                              columns='nome_pais', 
                              values='valor', 
                              aggfunc='sum')

#A tabela revela uma alternância completa entre os fluxos, onde as exportações de um país ocorrem apenas nos meses de inatividade do outro.

# ===========================================================
# PARTE 6 – FEATURE ENGINEERING
# ===========================================================

# Exercício 9
# 1. Extraia ano e mês da coluna periodo
df["periodo"].dt.year
df["periodo"].dt.month
# 2. Crie coluna valor_mil (valor / 1000)
df["valor_mil"] = df["valor"] / 1000
# 3. Calcule crescimento percentual por produto mês a mês
tabela_crescimento = tabela_pivot.pct_change() * 100
# RESOLVA AQUI:



# ===========================================================
# PARTE 7 – QUALIDADE DE DADOS
# ===========================================================

# Exercício 10
# 1. Verifique valores nulos
df.isnull().sum()
# 2. Verifique valores negativos
df[df['valor'] < 0]
# 3. Verifique duplicatas
df.duplicated().sum()
# RESOLVA AQUI:








