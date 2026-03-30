# Faça um programa que conte quantas 
# vezes a letra “a” aparece em uma palavra

#%%
palavra = input("Escreva uma palavra: ")
resultado = 0

for i in palavra:
    if i == "a":
        resultado += 1

print("Essa palavra tem:",resultado,"letras a.")
