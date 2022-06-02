def area(base, alt):
    conta = (base * alt) / 2
    return conta

def despedida():
    print("Obrigado por usar este programa!")
    print("Até logo!")

base = float(input("Digite valor da base: "))
alt = float(input("Digite o valor da altura: "))

print(f"Área = {area(base, alt):.2f} cm")
despedida()