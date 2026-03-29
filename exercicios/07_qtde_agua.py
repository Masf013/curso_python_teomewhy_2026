# Altere o programa anterior para considerar a quantidade de garrafas de água

texto = """
Escolha a sua água para comprar
(1) Água mineral natural - R$ 1,50
(2) Água mineral com gás - R$ 2,50 """

opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.50
elif opcao == "2":
    valor_item = 2.50
if valor_item == 0:
    print("Entre com a porra da opção correta, não seja idiota.")

else:
    qtde = input("Quantas garrafas? ")
    qtde = int(qtde)
    valor_total = valor_item * qtde
    print("O valor da sua conta é: R$", valor_total)