s = 0

for i in range (0, 6):
    n = int(input("DIGITE UM NÚMERO: "))
    if (n % 2) == 0:
        s += n
print("o somatório total de numeros pares foi de: {} ".format(s))