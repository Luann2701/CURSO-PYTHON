import random

escolhaPC= random.randint(0,5)
escolhaUsuario= int(input("Escolha um número de 0 a 5: "))

if escolhaUsuario == escolhaPC:
    print("Parabéns! Você acertou!")
else:
    print("Que pena! Você errou.")
print("O número escolhido pelo computador foi: {}".format(escolhaPC))