# 1: Criando um Dicionário
aluno = {"nome": "Camila",
    "idade": 22,
    "curso": "Economia"
}
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']}")
print(f"Curso: {aluno['curso']}")
# 2: Manipulação de Dicionário
produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10
}
# a. Adicione uma nova chave chamada 'marca' com um valor de sua escolha.
produto["marca"] = "Positivo"

# b. Atualize o preço do produto para R$ 320,00.
produto["preco"] = 320.00

# c. Reduza o estoque em 2 unidades.
produto["estoque"] = produto["estoque"] - 2

# d. Remova a chave 'marca' do dicionário.
del produto["marca"]

# e. Exiba o dicionário atualizado.
print(produto)

# 3: Iterando sobre um Dicionário
notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}
# a. Itere sobre o dicionário e exiba os nomes dos alunos e suas respectivas notas.
for nome, nota in notas.items(): 
    print(f"Aluno(a): {nome} - Nota: {nota}")
# b. Calcule a média das notas e exiba o resultado.
todas_as_notas = notas.values()
media = sum(todas_as_notas) / len(notas)
print(media)

# 4: Soma de Valores
numeros = {"a": 10, "b": 20, "c": 30}
num = numeros.values()
soma = sum(num)
print(soma)

# 5: Contagem de Itens Repetidos
lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
contagem = {}
for frutas in lista: 
    if frutas in contagem:
        contagem[frutas] += 1
    else:
        contagem[frutas] = 1

print(contagem)

# 6: Filtrando Dicionário
produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
filtro = {}

for nome,preco in produtos.items():
    if preco > 50:
        filtro[nome] = preco

print(filtro)

# 7: Tradutor Simples
# Crie um dicionário chamado 'tradutor' que contém algumas palavras em inglês como chaves e suas traduções para português como valores.
tradutor = {
    "key": "chave", 
    "annual": "anual",
    "percentual": "percentual",
    "rate": "taxa",
    "price": "preço",
    "notebook": "caderno",
    "bottle": "garrafa"
}

#Peça ao usuário para digitar uma palavra em inglês e exiba sua tradução, caso exista no dicionário. Se a palavra não estiver cadastrada, exiba "Palavra não encontrada".
palavra = input("Digite a palavra em inglês: ").lower().strip()
encontrado = False

for ingles,portugues in tradutor.items():
    if ingles == palavra:
        print(f"A tradução é: {portugues}")
        encontrado =True
        break
if not encontrado:
    print("Palavra não econtrada")  

# 8: Lista de Compras
lista_compras = {}

#Adicionar ou alterar itens da lista:
add_item = input("Digite o item que você quer adicionar a lista: ").lower().strip()
add_qtd = int(input(f"Qual a quantidade de {add_item}? "))
lista_compras[add_item] = add_qtd

#Remover itens da lista:
dele_item = input("Qual item você deseja remover?").lower().strip()
if dele_item in lista_compras:
    del lista_compras[dele_item]
    print(f"{dele_item} foi removido com sucesso!")
else:
    print("Produto não encontrado")
    
print(lista_compras)

# 9: Dicionário Aninhado
turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}

# a. Adicione um novo aluno ao dicionário.
cadastro = input("Digite o nome do aluno: ").lower().strip().title()
cad_idade = int(input("Digite a idade: "))
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
cad_notas = [nota1, nota2, nota3]

turma[cadastro] = {"idade": cad_idade,
                           "notas": cad_notas}
print(turma)

# b. Calcule a média de notas de cada aluno e exiba no formato:
medias = {}
for nomes, valores in turma.items():
    lista_notas = valores["notas"]
    media = sum(lista_notas)/len(lista_notas)
    medias[nomes] = media

for aluno, med in medias.items():
    print(f"{aluno}: Média  {med}")
    
# c. Encontre o aluno com a maior média e exiba o nome dele.
melhor_aluno = max(medias, key=medias.get)
maior_nota = medias[melhor_aluno]
print(f"O/A melhor aluno/a foi: {melhor_aluno}, com média {maior_nota}")
# 10: Cadastro de Funcionários
funcionarios = {}
cad_nome = input("Digite o nome do funcionário: ").lower().strip().title()
cad_cargo = input("Digite o cargo do funcionário: ").lower().strip().title()
cad_salario = float(input("Digite o salário do funcionário: "))

funcionarios[cad_nome] = {"Cargo": cad_cargo,
                          "Salário": cad_salario}

print(funcionarios)

busca = input("Digite o nome do funcionário que você deseja buscar: ").lower().strip().title()
if busca in funcionarios:
    info = funcionarios[busca]
    print(f"Informação sobre {busca}: {info}")
else:
    print("Funcionário não encontrado")


