# Questão 1: Carregar o DataFrame
# LER arquivo titanic.csv em um DataFrame pandas chamado df?
import pandas as pd
df = pd.read_csv(r"C:\Users\camis\OneDrive\Anexos de email\Área de Trabalho\FACULDADE\PROG. PARA ANALISE DE DADOS\analiseDados\Dados\titanic.csv")
#

# Questão 2: Filtrar passageiros do sexo feminino
# Filtrar o DataFrame para mostrar apenas as Mulheres?
# (Dica: Filtar onde a coluna "Sex" é igual a "female")

mulheres = df.loc[df["Sex"] == "female", :]
print(mulheres)

# Questão 3: Contar sobreviventes
# Quantos passageiros Sobreviveram?
# (Dica: Sobreviventes têm o valor 1 na coluna "Survived")
sobreviventes = df.loc[df["Survived"] == 1, ["Survived"]].sum()
print(sobreviventes)

# Resposta: 152
# Questão 4: Calcular a média da idade
# Quantos Homens Sobreviveram?
homens_sobreviventes = df.loc[(df["Survived"] == 1) & (df["Sex"] == "male"), ["Survived"]].sum()
print(homens_sobreviventes)

# Resposta: 0
# Questão 5: Calcular Nome "John"
# Calcular quantos passageiros tem o nome "John"?
# (Dica: Usar a coluna "Name")
filtro = df["Name"].str.contains(r"John", case=False)
john = df.loc[filtro, :]
len(john)

# Resposta: 30
