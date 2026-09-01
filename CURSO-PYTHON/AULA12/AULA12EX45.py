import random

escolhaPC= random.randint(1,3)

print("----------------MENU--DO--JOKENPO---------------------")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

opc = int(input("Digite uma opção: "))

if escolhaPC == 1:
        escolhaPC = "Pedra"
        print("PC escolheu {}".format(escolhaPC))

if escolhaPC == 2:
        escolhaPC = "Papel"
        print("PC escolheu {}".format(escolhaPC))

if escolhaPC == 3:
        escolhaPC = "Tesoura"
        print("PC escolheu {}".format(escolhaPC))

if opc == 1:
        opc = "Pedra"
        print("Sua escolha: {}".format(opc))

if opc == 2:
        opc = "Papel"
        print("Sua escolha: {}".format(opc))

if opc == 3:
        opc = "Tesoura"
        print("Sua escolha: {}".format(opc))

if escolhaPC == "Pedra" and opc == "Pedra":
    print("EMPATE")

elif escolhaPC == "Papel" and opc == "Pedra":
    print("COMPUTADOR GANHOU")

elif escolhaPC == "Tesoura" and opc == "Pedra":
    print("VOCÊ GANHOU!")

if escolhaPC == "Pedra" and opc == "Papel":
    print("VOCÊ GANHOU")

elif escolhaPC == "Papel" and opc == "Papel":
    print("EMPATE")

elif escolhaPC == "Tesoura" and opc == "Papel":
    print("COMPUTADOR GANHOU")

if escolhaPC == "Pedra" and opc == "Tesoura":
    print("COMPUTADOR GANHOU")

elif escolhaPC == "Papel" and opc == "Tesoura":
    print("VOCÊ GANHOU")

elif escolhaPC == "Tesoura" and opc == "Tesoura":
    print("EMPATE")


