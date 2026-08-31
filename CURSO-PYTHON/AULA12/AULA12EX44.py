vlrprod = float(input("Qual o valor do produto: "))

print("----------------------------MENU---------------------------")
print("Qual a forma de pagamento: ")
print("1 - Á vista/Cheque (10% de desconto)")
print("2 - Á vista no cartão (5% de desconto)")
print("3 - Em 2x no cartão (Preço normal)")
print("4 - Em 3x ou mais vezes no cartão 20% de juros)")

formpag = int(input("Sua opção: "))

if formpag == 1:
    print("O novo valor do produto a ser cobrado é: R${:.2f}".format(vlrprod -(vlrprod*0.10)))
elif formpag == 2:
    print("O novo valor do produto a ser cobrado é: R${:.2f}".format(vlrprod -(vlrprod*0.05)))
elif formpag == 3:
    print("O novo valor do produto a ser cobrado é: R${:.2f}".format(vlrprod))
elif formpag == 4:
    print("O novo valor do produto a ser cobrado é: R${:.2f}".format(vlrprod +(vlrprod*0.20)))