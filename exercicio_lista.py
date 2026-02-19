# 21. Crie uma lista nomes contendo os nomes: "Ana", "Pedro", "Maria", "João".
nomes = ["Ana", "Pedro", "Maria", "João"]

#22. Utilize um loop for para imprimir cada nome da lista.
for nome in nomes: 
    print(nome)

# 23. Crie uma nova lista nomes_maiusculos contendo os nomes da lista nomes em letras maiúsculas. Utilize um loop for para isso.
nomes_maiusculos = []
for item in nomes:
    if item.istitle():
        nomes_maiusculos.append(item)

print(nomes_maiusculos)

# 24. Crie uma lista numeros contendo os números de 1 a 20. Utilize um loop for para imprimir apenas os números pares. - list_loop
numeros = range(1,20)
for n in numeros:
    if n % 2 == 0:
        print(n)
        
#25. Usando a lista numeros, utilize um loop for para criar uma nova lista quadrados contendo o quadrado de cada número.
quadrados = []
for n in numeros:
    operacao = n**2
    quadrados.append(operacao)

print(quadrados)

#26. Crie uma lista palavras contendo: "python", "java", "c", "javascript". Utilize um loop for para imprimir o tamanho (número de letras) de cada palavra.
palavras = ["python", "java", "c", "javascript"]
for palavra in palavras:
    tamanho = len(palavra)
    print(tamanho)

#27. Crie uma lista idades contendo [12, 18, 25, 40, 60]. Utilize um loop for para imprimir "maior de idade" se a idade for >= 18 ou "menor de idade" se for < 18.
idades = [12, 18, 25, 40, 60]

for idade in idades:
    if idade >= 18:
        print(f"A idade é {idade}, portanto é maior de idade")
    else:
        print(f"A idade é {idade}, portanto é menor de idade")


#28. Crie uma lista notas contendo [5.5, 7.0, 8.3, 4.9, 6.2]. Utilize um loop for para contar quantos alunos estão aprovados (nota >= 7) e quantos estão reprovados (nota < 7).
notas = [5.5, 7.0, 8.3, 4.9, 6.2]
aprovados = 0
reprovados = 0

for nota in notas:
    if nota >= 7:
        aprovados += 1
        print(f"Alunos aprovados: {aprovados}")
    else:
        reprovados += 1
        print(f"Alunos reprovados: {reprovados}")   

#29. Crie uma lista compras com ["arroz", "feijão", "batata", "carne"]. Utilize um loop for para imprimir cada item precedido da frase "Preciso comprar: ".
compras =["arroz", "feijão", "batata", "carne"]
for item in compras:
    print(f"Preciso comprar: {item}")
