

# 24. Crie uma lista numeros contendo os números de 1 a 20. Utilize um loop for para imprimir apenas os números pares. - list_loop
numeros = range(1,20)
for n in numeros:
    if n % 2 == 0:
        print(n)