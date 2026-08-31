nt1 = float(input("Digite a primeira nota do aluno: "))
nt2 = float(input("Digite a segunda nota do aluno: "))

media = (nt1+nt2)/2

if media < 5.0:
    print("ALUNO REPROVADO!")

elif media >= 5.0 and media <= 6.9:
    print("ALUNO ESTÁ DE RECUPERAÇÃO!")

else:
    print("ALUNO APROVADO!")