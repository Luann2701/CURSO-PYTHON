oldsal = float(input("Digite seu sálario: "))

if oldsal > 1250:
    print("O seu novo salário é de: R${}".format((oldsal*0.10)+oldsal))
else:
    print("O seu novo salário é de: R${}".format((oldsal*0.15)+oldsal))