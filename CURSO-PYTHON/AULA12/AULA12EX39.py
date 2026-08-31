age = int(input("Digite a sua idade: "))

passedtime = 18 - age

if age > 18:
    if passedtime < 0:
        passedtime = passedtime * (-1)
    
    print("Você está atrasado com seu alistamento em: {} anos!!!".format(passedtime))

elif age < 18:
    print("Você se alistará daqui {} anos.".format(passedtime))

else: 
    print("Está na hora de se alistar você ja tem {} anos.".format(age))