vlrcasa = float(input("Digite o valor da casa: "))
salar = float(input("Digite o seu salário: "))
financ = float(input("Em quantos anos você pretende pagar: "))

meses = financ * 12
prestmen = vlrcasa/meses

verif = 0.30 * salar

print("Valor da prestação é de: R${:.2f}".format(prestmen))
print(verif)
if (prestmen > verif):
    print ("Empréstimo Negado!")
else:
    print ("Empréstimo Concedido!")