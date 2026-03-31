# %%

idades = []

while True:
    idade = input("Entre com a idade: ")

    if idade == "":
        break

    idades.append(int(idade))

print(idades)

media = sum(idades) / len(idades)
maximo = max(idades)
minimo = min(idades)
qtdeidade = len(idades)

print("A média das idades é: ", round(media,2))
print("A idade máxima é: ", maximo)
print("A idade mínima é: ", minimo)
print("A quantidade de idades é: ", qtdeidade)
