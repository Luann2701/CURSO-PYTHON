maior_idade = 0
nome_mais_velho = ""
soma_idade = 0

for i in range(0, 4):
    nome = str(input("Digite o seu nome: "))
    age = int(input("Digite sua idade: "))
    sxo = str(input("Digite seu sexo (Masc/Femi): "))

    soma_idade += age  
    
    if age > maior_idade:
        maior_idade = age
        nome_mais_velho = nome

med = soma_idade / 4

print(f"A pessoa mais velha é {nome_mais_velho}, com {maior_idade} anos.")
print(f"A média de idade dessas pessoas é de: {med:.1f} anos")