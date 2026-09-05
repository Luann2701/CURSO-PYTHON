n = int(input("DIGITE O 1° NÚMERO DE UMA P.A: "))
raz = int(input("DIGITE A RAZÃO DESTA P.A: "))

for i in range(0, 10):
    termo = n + (i * raz)
    print(termo)