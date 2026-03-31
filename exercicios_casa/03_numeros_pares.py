# **Lista de números pares** Crie uma lista 
# chamada `pares` que contenha todos os números 
# pares entre 10 e 50 (inclusive). Exiba a lista, 
# a quantidade de elementos e a soma de todos os valores.

#%%
pares = []

for i in range(10,51):
    if i % 2 ==0:
        pares.append(i)

print("Lista:",pares)
print(len(pares))
print(sum(pares))