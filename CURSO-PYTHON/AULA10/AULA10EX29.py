velo = float(input("Digite a velocidade do carro em km/h: "))

multa = velo - 80
if velo > 80:
    print("Você foi multado por estar andando acima do limite! O valor da multa é de R${:.2f}".format(multa * 7))