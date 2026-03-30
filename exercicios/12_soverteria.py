# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

texto1 = """
Que tipo de soverte você deseja?
(1) Casquinha
(2) Cascão
(3) Cestinha
"""

soverte = int(input(texto1))

texto2 = """
Que tipo de sabor você deseja?
(1) Morango
(2) Creme
(3) Chocolate
"""

sabor = int(input(texto2))

texto3 = """
Que tipo de cobertura você deseja?
(1) Caramelo
(2) Morango
(3) Chocolate
(4) Sem cobertura
"""

cobertura = int(input(texto3))

conta = 0
if soverte == 1:
    conta += 1.00
elif soverte == 2:
    conta += 2.50
elif soverte == 3:
    conta += 4.00
else:
    print("Opção de soverte inválida!")

if cobertura in(1,2,3):
    conta += 1.50
elif cobertura == 0:
    conta = 0.00
else:
    print("Opção de soverte inválida!")

  
if conta == 0:
    print("Não temos essa opção no cardápio!")
else:
    print("O valor da sua conta é:", conta)

