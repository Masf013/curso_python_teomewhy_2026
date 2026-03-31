# 1. Faça um programa que receba 4 
# notas usando um laço e calcule a média.


notas = 0
qtde_notas = 4

for i in range(qtde_notas):
    nota = float(input("Digite uma nota: "))
    notas += nota

media = notas / qtde_notas
print("Média:",round(media,2))
