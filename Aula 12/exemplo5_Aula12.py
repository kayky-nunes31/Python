def calculeimc(peso, alt):
    conta = peso / alt ** 2
    return(conta)

def despedida():
    print("Obrigado por usar este programa!")
    print("Até logo!")

peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura: "))

print("O IMC é", calculeimc(peso, alt), " Kg/m")
despedida()