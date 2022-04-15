#Faça um programa em Python que leia um valor n, inteiro e positivo, calcule e
#mostre a seguinte soma:
#S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n
soma = 0
qte = 0
while True:
    num = int(input("Digite um valor inteiro (0 para sair)"))
    if num > 0:
        soma = soma + num
    elif num < 0:
        break
    if num == 0:
        break
    qte = qte + 1

print(f"A soma dos números digitados é {soma}")