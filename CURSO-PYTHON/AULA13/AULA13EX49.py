n = int(input("DIGITE UM NÚMERO: "))
Stoped = int(input("DIGITE UM NÚMERO PARA PARAR A TABOADA: "))

for i in range (0, Stoped + 1):
    print("a taboada do numero {} multiplicado até o {} é: {} x {} = {}".format(n, Stoped, n, i, n * i))