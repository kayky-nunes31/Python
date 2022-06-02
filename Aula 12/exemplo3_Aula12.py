def calculadora(a, b):
    return a+b, a-b, a*b, a/b, a**b

def adeus():
    print("Até logo... volte sempre")

a = int(input("Digite um número"))
b = int(input("Digite outro número"))

c = calculadora(a, b)
print(f"soma = {c[0]}")
print(f"subtração = {c[1]}")
adeus()