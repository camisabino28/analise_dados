#Usar arquivo salary.xlsx

import pandas as pd
df = pd.read_excel(r"C:\Users\camis\OneDrive\Anexos de email\Área de Trabalho\FACULDADE\PROG. PARA ANALISE DE DADOS\analiseDados\Dados\salary.xlsx")

# 1.	Quantas linhas e quantas colunas tem o dataset?
df.shape

# 2.	Qual a média salarial? Qual é o maior salário? O menor salário?
media_salarial = df.loc[:, "salary"].mean()
df.loc[:, "salary"].max()
df.loc[:, "salary"].min()

# 3.	Crie um df com apenas as colunas job_title, salary, company_location, company_size, remote_ratio?
df2 = df.loc[:, ("job_title", "salary", "company_location", "company_size", "remote_ratio")]
print(df2)

# 4.	Qual é o maior e menor salário de um “Data Scientist”? Onde fica essas empresas
data_scientist = df.loc[df["job_title"] == "Data Scientist", ["job_title","salary","company_location"]]
data_scientist.max()
data_scientist.min()

# 5.	Qual a profissão com a maior média salarial? E a menor?
media_salarial_prof = df.groupby("job_title")["salary"].mean().sort_values()
media_salarial_prof .idxmax()
media_salarial_prof .idxmin()

# 6.	Quais as profissões com a média salarial maior que a média geral?
profissoes_ricas = media_salarial_prof[media_salarial_prof > media_salarial]
print(profissoes_ricas)
# 7.	Qual a localização com maior média salarial?
media_salarial_local= df.groupby("company_location")["salary"].mean()
media_salarial_local.idxmax()

# 8.	Quais as profissões que existem no Brasil (BR)?
prof_brasil = df.loc[df["company_location"] == "BR", ["job_title", "company_location","salary"]]

# 9.	Qual a média salarial no Brasil?
media_sal_brasil = prof_brasil["salary"].mean()

# 10.	Quantas profissões existem no Brasil?
profissões = prof_brasil["job_title"].unique()
len(profissões)

# 11.	Qual a profissão que mais ganha no Brasil?
indice = prof_brasil["salary"].idxmax()
maior_sal_brasil = prof_brasil.loc[indice, "job_title"]
print(maior_sal_brasil)

# 12.	Quantas profissões tem nos US e que trabalham em empresas grandes (L)?
tamanho_usa = df.loc[(df["company_location"] == "US") & (df["company_size"] == "L"), ["job_title", "salary","company_size"]]
prof_us_l = tamanho_usa["job_title"]
len(prof_us_l)

# 13.	Qual é a média salarial das empresas médias (M) na Canada (CA)?
media_canada_m = df.loc[(df["company_location"] == "CA") & (df["company_size"] == "M"), ["job_title", "salary"]]
media_canada_m["salary"].mean()

# 14.	Qual é o país com mais profissões? E qual é o mais com menos?
agrup_prof = df.groupby("company_location")["job_title"].nunique()
agrup_prof.idxmax()
agrup_prof.idxmin()

# 15.	Quem ganha mais que trabalha remoto, presencial ou híbrido?
agrup_remoto = df.groupby("remote_ratio")["salary"].mean()
agrup_remoto.idxmax()

# 16.	Qual o país com maior numero de profissões trabalhando 100% remoto?
remoto = df.loc[df["remote_ratio"] == 100, ["company_location", "job_title"]]
agrup_remoto = remoto.groupby("company_location")["job_title"].nunique().sort_values()
agrup_remoto.idxmax()


