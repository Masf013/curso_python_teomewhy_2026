# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

texto = """
Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás """

opcao = input(texto)

conta = 0
if opcao == "1":
    conta = 1.50
elif opcao == "2":
    conta = 2.50
if conta == 0:    
    print("Entre com a porra da opção correta, não seja idiota.")
else:
    print("O valor da sua conta é:", conta)

