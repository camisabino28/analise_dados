# LISTA DE EXERCÍCIOS – ANÁLISE DE DADOS COM PANDAS Dataset: Ranking
# Mundial de Universidades (notas.csv)
import pandas as pd
df = pd.read_csv(r"C:\Users\camis\OneDrive\Anexos de email\Área de Trabalho\FACULDADE\PROG. PARA ANALISE DE DADOS\analiseDados\Dados\notas.csv")
df.shape
df.columns
df.dtypes
df.isna().sum()
df.head()
df.tail()

# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================

# Exercício 1 – Conhecendo o Dataset 
# 1. Quantas linhas e colunas existem?
df.shape
# Tem 2200 linhas e 14 colunas

# 2. Quais são os tipos de dados? 
df.dtypes

# 3. Existe coluna com valores ausentes?
df.isna().sum()
#Sim a coluna broad_impact tem 200 NAs

# 4. Qual é o período de anos disponível? 
anos =df[["year"]].drop_duplicates()
# 2012 - 2015

# 5. Quantos países diferentes existem?
paises =df[["country"]].drop_duplicates()
paises.shape
#59 países

# Exercício 2 – Estatísticas Gerais 
# 1. Média do score 
score = df[["score"]]
score.mean()

# 2. Maior score 
score.max()

# 3.Menor score 
score.min()

# 4. Média do score por ano 
agrupamento = df.groupby("year")["score"].mean()

# 5. Desvio padrão do score
score.std()

# ============================================================
# FILTROS E SELEÇÕES
# ============================================================

# Exercício 3 – Top Universidades 
# 1. Mostre as 10 melhores universidades do mundo (menor world_rank) 
top_10 = df[df["world_rank"] <= 10]
print(top_10)

# 2. Mostre as 5 melhores universidades do Brasil (se existirem) 
top_5_brasil = df[(df["country"] == "Brazil") & (df["national_rank"] <= 5)]
print(top_5_brasil)
# 3. Mostre universidades com score maior que 90 
nota_90 = df[df["score"] >= 90]
print(nota_90)

# 4. Mostre universidades dos EUA com score maior que 80
eua_score_80 = df[(df["country"] == "USA") & (df["score"] >= 80)]
print(eua_score_80)

# Exercício 4 – Seleção Avançada 
# 1. Mostre apenas as colunas: institution, country e score 
selecao_1 = df[["institution","country","score"]]
print(selecao_1)

# 2. Mostre universidades entre rank 50 e 100 
selecao_2 = df[(df["world_rank"] >= 50) & (df["world_rank"] <= 100)]
print(selecao_2)
# 3. Mostre universidades cujo país é “United Kingdom”
united_kingdom = df[df["country"] == "United Kingdom"]
print(united_kingdom)

# ============================================================ PARTE 3 –
# MISSING VALUES
# ============================================================

# Exercício 5 – Valores Ausentes 
# 1. Quantos valores nulos existem na coluna broad_impact? 
missing_1 = df[["broad_impact"]].isna().sum()
print(missing_1)

# 2. Qual percentual do dataset é nulo? 
total = df.size
total_nulos = df.isna().sum().sum()
percentual = (total_nulos/total)*100
print(percentual)

# 3. Remova linhas com broad_impact nulo
remocao = df.dropna()
remocao.isna().sum()  #verificação

# 4. Preencha valores nulos com a média 
media_bi = df[["broad_impact"]].mean()
preenchido = df.fillna(media_bi)

# 5. Compare a média antes e depois do preenchimento
media_preenchido = preenchido[["broad_impact"]].mean()
print(media_preenchido)
print(media_bi)

# Da igual 

# ============================================================ PARTE 4 –
# GROUPBY (ANÁLISE POR PAÍS E ANO)
# ============================================================

# Exercício 6 – Análise por País 
# 1. Média do score por país 
score_pais = df.groupby("country")["score"].mean()
print(score_pais)

# 2. País com maior média de score 
maior_media = score_pais.idxmax()  #idxmax chama o indice não o valor
print(maior_media)

# 3. Quantidade de universidades por país 
quant_uni = df.groupby("country")["institution"].nunique()
print(quant_uni)

# 4. Top 10 países com mais universidades
quant_uni_top10 = quant_uni.nlargest(10)
print(quant_uni_top10)

# Exercício 7 – Análise por Ano 
# 1. Média do score por ano 
agrupamento = df.groupby("year")["score"].mean()
print(agrupamento)

# 2. Qual ano teve maior média? 
maior_media = agrupamento.nlargest(1)
print(maior_media)

# 3. Faça um gráfico da evolução do score médio ao longo do tempo
import matplotlib.pyplot as plt

evolucao_score = df.groupby("year")["score"].mean().reset_index()
plt.style.use('ggplot')
plt.figure(figsize=(8, 5))
plt.plot(evolucao_score['year'], evolucao_score['score'], marker='o', color='blue', linewidth=2)
plt.title('Evolução do Score Médio')
plt.xlabel('Ano')
plt.ylabel('Média do Score')
plt.xticks(evolucao_score['year']) 
plt.show()
