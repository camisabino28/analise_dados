x = 4
idade = 4
objeto = "palhaco"

list = [objeto, idade, x]
list[2]

lista_mista = ["cavalo", "pato", 16, 17]
animal = []
numero = []

for item in lista_mista:
    if type(item) == str:
        animal.append(item)
    elif type(item) == int:
        numero.append(item)

lista_mista2 = [20,30,50,10,"cavalo", "pato", 16, 17]
i = 0
while i < len(lista_mista2):
    if isinstance(lista_mista2[i],str):
        print(f"Pare! encontrei a string: {lista_mista2[i]}")
        break
    i += 1 
        
dict_mista = {"animal" : "cavalo",
              11 : "pato",
              12 : 16,
              13 : 17
}