cont = 0

for i in range (0, 7):
    year = int(input("Digite seu ano de nascimento: "))
    if 2026 - year >= 18:
        cont += 1
print(f"A quantidade de pessoas que são maiores de idade são: {cont} pessoas.")