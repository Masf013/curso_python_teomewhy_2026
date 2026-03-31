# %%

idades = [18,5,36,54,23,54,14]

print(idades)

#%%

persona = ["Misael", "Augusto", 28, True,000.00]
print(persona)

#%%
type(persona)

#%%

idades = [12,36,25,12,32,32,45,85,32]

print("A soma das idades é:",sum(idades))

print("A quantidade de idades é:",len(idades))

print("A média das idades é:", sum(idades)/len(idades))

print("A menor idade é:",min(idades))

print("A maior idade é:",max(idades))

#%%

teo = ["Teo Calvo", 32, 
       True, "casado",
       ["estagiario","ds jr.","ds pl", "head"],
       [1550,4000,6550,10000], 
       ["Ana", "Maria", "Claúdia"]]

print(len(teo))

print(teo[-2][0])
teo[-1][-2]

#%%
teo[0:4]

teo[4][2:4]

#%%
teo[4][-2:]

#%%
teo[-1:][-2:]

#%%
salarios = teo[5]
salarios[::-1]

# [ start : stop : step ]