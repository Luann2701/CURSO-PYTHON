num = int(input("Digite um número: "))
total_divisoes = 0

for i in range(1, num + 1):
    if num % i == 0:
        print("\033[34m", end="")
        total_divisoes += 1
    else:
        print("\033[m", end="")
    print(f"{i} ", end="")

print("\033[m")  # Limpa a formatação de cor no final

print(f"\nO número {num} foi dividido {total_divisoes} vezes.")

if total_divisoes == 2:
    print(f"O número {num} É primo!")
else:
    print(f"O número {num} NÃO é primo!")