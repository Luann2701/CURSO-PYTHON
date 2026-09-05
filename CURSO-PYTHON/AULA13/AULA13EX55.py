maior = 0
menor = 100000000

for i in range (0, 5):
    peso = float(input("Digite seu peso corporal: "))
    
    if peso > maior:
        maior = peso
        
    if peso < menor:
        menor = peso

print(f"O maior peso foi de: {maior}kg")
print(f"O menor peso foi de: {menor}kg")