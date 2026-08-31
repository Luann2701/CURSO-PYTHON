weight = float(input("Digite seu peso em Kg: "))
height = float(input("Digite sua altura em CMs: "))

imc = weight / pow((height / 100), 2)

if imc < 18.5:
    print("ABAIXO DO PESO IDEAL")
elif 18.5 <= imc < 25:
    print("PESO IDEAL")
elif 25 <= imc < 30:
    print("VOCÊ ESTÁ COM SOBREPESO")
elif 30 <= imc < 40:
    print("VOCÊ ESTÁ OBESO")
else:
    print("OBESIDADE MÓRBITA")