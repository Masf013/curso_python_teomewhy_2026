# **Fatiando uma frase** Dada a string
# `"Python é uma linguagem poderosa"`,
# transforme‑a em uma lista de palavras 
# usando o método `split()`. Depois:
# Exiba as três primeiras palavras.
# Exiba as duas últimas palavras.
# Exiba a lista invertida (da última para a primeira palavra).

# %%

frase = "Python é uma linguagem poderosa"
palavras = frase.split()

print("Lista de palavras:",palavras)

print("As 3 primeiras palavras:",palavras[:3])

print("As 2 últimas palavras:",palavras[-2:])

print("A Lista invertida:",palavras[::-1])