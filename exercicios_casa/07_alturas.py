# **Cadastro de alturas com loop**  
# Crie um programa que:
# Inicia com uma lista vazia.
# Pede ao usuário para digitar alturas (números reais) uma a uma.
# Para quando o usuário digitar um valor vazio (apenas Enter).
# Ao final, exiba a altura média, a maior altura e a menor altura 
# (se houver pelo menos uma altura informada).

lista = []

while True:
    altura = input("Digite uma altura: ")
    if altura == "":
        break
    lista.append(float(altura))

media = sum(lista) / len(lista)
maxima = max(lista)
minima = min(lista)

print("A média é:",media)
print("A máxima é:",maxima)
print("A mínima é:",minima)