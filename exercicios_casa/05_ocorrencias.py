# **Contando ocorrências**  
# Crie uma lista fixa: `[5, 2, 9, 1, 5, 8, 5, 3, 5]`. 
# Peça ao usuário um número inteiro e informe quantas vezes esse número aparece na lista.
# %%
lista = [5, 2, 9, 1, 5, 8, 5, 3, 5]

numero = int(input("Digite um número: "))

count = 0
for i in lista:
    if i == numero:
        count += 1
print("Quantas vezes o",numero,"aparece é:",count)