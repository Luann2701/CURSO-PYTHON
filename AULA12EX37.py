num = int(input("Digite um numero qualquer: "))

print("----------------------------MENU---------------------------")
print("Digite uma opção:")
print("1 - Converter para BINÁRIO")
print("2 - Converter para OCTAL")
print("3 - Converter para HEXADECIMAL")

opc = int(input("Sua opção: "))

if opc == 1:
    print(f"{num} em binário é {bin(num)[2:]}")
elif opc == 2:
    print(f"{num} em octal é {oct(num)[2:]}")
elif opc == 3:
    print(f"{num} em hexadecimal é {hex(num)[2:]}")
else:
    print("Opção inválida. Tente novamente.")