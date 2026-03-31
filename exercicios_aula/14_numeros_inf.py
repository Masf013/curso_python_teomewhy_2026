# 2. Peça números indefinidamente ao 
# usuário e pare quando ele digitar 0, 
# mostrando a soma de todos.

#%%
soma = 0

while True:
    numero = input("Digite um número: ")
    if numero == "0":
        break
    soma += float(numero)
print("A soma total é:", soma)