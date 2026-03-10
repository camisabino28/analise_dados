"""
Aula - Exercicios de Filtros Regex com Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados com print.

Requisito:
- Instalar pandas: pip install pandas

Regra da aula:
- Regex ajuda a filtrar texto com padroes.
- Resolva um exercicio por vez.
"""

import pandas as pd
df = pd.read_excel(r"C:\Users\camis\OneDrive\Anexos de email\Área de Trabalho\FACULDADE\PROG. PARA ANALISE DE DADOS\analiseDados\Dados\cadastro_alunos.xlsx")
# ---------------------------------------------
# EXERCICIO 1
# ---------------------------------------------
"""
Filtre nomes que começam com a letra A
"""
# RESOLUCAO
filtro = df["nome_aluno"].str.contains("^A")
df.loc[filtro, :]

# ---------------------------------------------
# EXERCICIO 2
# ---------------------------------------------
"""
Filtre nomes que terminam com "Silva"
"""
# RESOLUCAO
filtro2 = df["nome_aluno"].str.contains("Silva$", case= False)
df.loc[filtro2, :]

# ---------------------------------------------
# EXERCICIO 3
# ---------------------------------------------
"""
Filtre nomes que começam com M
"""
# RESOLUCAO
filtro3 = df["nome_aluno"].str.contains("^M")
df.loc[filtro3, :]

# ---------------------------------------------
# EXERCICIO 4
# ---------------------------------------------
"""
Filtre nomes que começam com:
A ou B ou C
"""
# Dica regex
# r"^[ABC]"
# RESOLUCAO
filtro4 = df["nome_aluno"].str.contains(r"^[ABC]")
df.loc[filtro4, :]


# ---------------------------------------------
# EXERCICIO 5
# ---------------------------------------------
"""
Filtre nomes que começam com:
Ana OU Maria
"""
# Dica
# r"^(Ana|Maria)"
# RESOLUCAO
filtro5 = df["nome_aluno"].str.contains(r"^(Ana|Maria)", case=False)
df.loc[filtro5, :]

# ---------------------------------------------
# EXERCICIO 6
# ---------------------------------------------
"""
Filtre nomes que possuem a palavra "Paulo"
em qualquer posição
"""
# RESOLUCAO
filtro6 = df["nome_aluno"].str.contains("paulo", case=False)
df.loc[filtro6, :]


# ---------------------------------------------
# EXERCICIO 7
# ---------------------------------------------
"""
Filtre nomes com exatamente dois nomes
Exemplo:
Ana Souza
Bruno Lima
"""
# Dica
# r"^[A-Za-z]+ [A-Za-z]+$"
# RESOLUCAO
filtro7 = df["nome_aluno"].str.contains(r"^[A-Z]+ [A-Z]+$", case=False)
df.loc[filtro7, :]

# ---------------------------------------------
# EXERCICIO 8
# ---------------------------------------------
"""
Filtre nomes com três palavras
"""
# RESOLUCAO
filtro8 = df["nome_aluno"].str.contains(r"^[A-Z]+ [A-Z]+ [A-Z]+$", case=False)
df.loc[filtro8, :]

# ---------------------------------------------
# EXERCICIO 9
# ---------------------------------------------
"""
Filtre nomes que tenham Santos OU Silva
"""
# RESOLUCAO
filtro9 = df["nome_aluno"].str.contains(r"(Santos|Silva)", case=False)
df.loc[filtro9, :]

# ---------------------------------------------
# EXERCICIO 10
# ---------------------------------------------
"""
Filtre nomes que terminam com:
Costa ou Alves
"""
# RESOLUCAO
filtro10 = df["nome_aluno"].str.contains(r"(Costa|Alves)$", case=False)
df.loc[filtro10, :]

# ---------------------------------------------
# EXERCICIO 11
# ---------------------------------------------
"""
Filtre nomes que possuem apenas letras e espaços
(remover empresas)
"""
# Dica
# r"^[A-Za-z ]+$"
# RESOLUCAO
filtro11 = df["nome_aluno"].str.contains(r"[A-Z]+$", case=False)
df.loc[filtro11, :]

# ---------------------------------------------
# EXERCICIO 12
# ---------------------------------------------
"""
Filtre nomes que começam com letra maiuscula
"""
# Dica
# r"^[A-Z]"
# RESOLUCAO
filtro12 = df["nome_aluno"].str.contains(r"^[A-Z]")
df.loc[filtro12, :]

# ---------------------------------------------
# EXERCICIO 13
# ---------------------------------------------
"""
Filtre nomes que possuem "Maria" ignorando maiúsculas/minúsculas
"""
# Dica
# case=False
# RESOLUCAO
filtro13 = df["nome_aluno"].str.contains("Maria", case=False)
df.loc[filtro13, :]

# ---------------------------------------------
# EXERCICIO 14
# ---------------------------------------------

"""
Filtre nomes que possuem duas palavras
e terminam com Souza ou Lima ou Rocha
"""
# RESOLUCAO
filtro10 = df["nome_aluno"].str.contains(r"^[A-Z]+ [A-Z]+ (Souza|Lima|Rocha)$", case=False)
df.loc[filtro10, :]




dados_clientes = {
    "cliente": [
        "Ana Souza",
        "Bruno Lima",
        "Carla Mendes",
        "Daniel Rocha",
        "Empresa XPTO Ltda",
        "Mercado Bom Preco",
    ],
    "email": [
        "ana.souza@gmail.com",
        "bruno_lima@empresa.com.br",
        "carla.mendes@yahoo.com",
        "daniel@outlook.com",
        "contato@xpto.com.br",
        "vendas@bompreco.com.br",
    ],
    "cidade": ["Sao Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Sao Paulo", "Curitiba"],
    "codigo_cliente": ["CLI-001", "CLI-002", "VIP-101", "CLI-003", "EMP-501", "VIP-102"],
}
df_clientes = pd.DataFrame(dados_clientes)

# Exercicio 15:
# Filtre os registros onde:
# a) email termina com ".com.br"
# b) cliente contem a palavra "Mercado"
# c) codigo_cliente comeca com "VIP"
#
# Dica:
# Use str.contains com padroes regex:
# - r"\.com\.br$"
# - r"Mercado"
# - r"^VIP"

# RESOLUCAO: complete aqui
filtro15 = df_clientes["email"].str.contains(r"\.com\.br$", case=False)
df_clientes.loc[filtro15, :]

filtro15_B = df_clientes["cliente"].str.contains(r"Mercado", case=False)
df_clientes.loc[filtro15_B, :]

filtro15_C = df_clientes["codigo_cliente"].str.contains(r"^VIP", case=False)
df_clientes.loc[filtro15_C, :]

# Exercicio 16:
# Filtre os clientes cujo codigo esteja no formato:
# 3 letras maiusculas + "-" + 3 digitos
# Exemplo valido: CLI-001
#
# Dica de regex:
# r"^[A-Z]{3}-\d{3}$"

# RESOLUCAO: complete aqui
filtro16 = df_clientes["codigo_cliente"].str.contains(r"^[A-Z]{3}-\d{3}$")
df_clientes.loc[filtro16, :]


# Exercicio 17:
# Encontre emails que sejam de:
# - gmail.com OU outlook.com
#
# Dica de regex:
# r"@(gmail|outlook)\.com$"

# RESOLUCAO: complete aqui
filtro17 = df_clientes["email"].str.contains(r"@(gmail|outlook)\.com$")
df_clientes.loc[filtro17, :]



# Inclui valores com caixa diferente e um valor ausente.
df_leads = pd.DataFrame(
    {
        "origem": ["Instagram", "instagram", "LinkedIn", "EMAIL", None, "Google Ads"],
        "campanha": ["Promo Verao", "promo verao", "B2B_Q1", "BLACK_FRIDAY", "Teste", "Leads_2026"],
    }
)

# Exercicio 18:
# a) Filtre origem contendo "instagram" sem diferenciar maiusculas/minusculas
# b) Filtre campanhas que tenham apenas letras, espacos e underscore
# c) Garanta que valores nulos nao quebrem o filtro
#
# Dicas:
# - case=False
# - na=False
# - regex sugerida para (b): r"^[A-Za-z_ ]+$"

# RESOLUCAO: complete aqui
filtro18_a = df_leads["origem"].str.contains("Instagram", case=False)
df_leads.loc[filtro18_a, :]

filtro18_b = df_leads["campanha"].str.contains( r"^[A-Za-z_ ]+$", case=False)
df_leads.loc[filtro18_b, :]

filtro18_c = df_leads["campanha"].str.contains( r"^[A-Za-z_ ]+$", na=False)
df_leads.loc[filtro18_b, :]