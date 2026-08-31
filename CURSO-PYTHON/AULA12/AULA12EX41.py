nasc = int(input("Digite o seu ano de nascimento: "))

age = 2026 - nasc

if age <= 9:
    print("CATEGORIA MIRIM")

elif age > 9 and age <= 14:
    print("CATEGORIA INFANTIL")

elif age > 14 and age <= 19:
    print("CATEGORIA JUNIOR")

elif age > 19 and age <= 20:
    print("CATEGORIA SÊNIOR")

else:
    print("CATEGORIA MASTER")
