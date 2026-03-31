# **Análise de notas**  Solicite ao usuário que 
# digite 4 notas (valores float). Armazene‑as em 
# uma lista. Depois: Exiba a maior nota, a menor 
# nota e a média. Verifique se a média é maior ou 
# igual a 7.0 e exiba uma mensagem “Aprovado” ou “Reprovado”.

#%%
notas = []
qtde_notas = 4

while qtde_notas > 0:
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    qtde_notas -= 1

maximo = max(notas)
minimo = min(notas)
media = sum(notas)/len(notas)

print("A nota máxima é:",maximo)
print("A nota mínima é:",minimo)
print("A média das notas é:",media)