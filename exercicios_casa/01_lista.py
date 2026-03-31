# Escreva um programa que receba uma lista
# de números do usuário e conte quantas
# vezes um número específico aparece na
# lista. Solicite ao usuário um número
# e exiba a contagem.

lista = [1,2,4,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,7,8,9,6,3,5,4,1,1,6,6,9]

numero = int(input("Entre com um número: "))

count = 0
for i in lista:
    if i == numero:
        count += 1
print("A quantidade de",numero,":",count)
