# Faça um programa em Python que solicite um número inteiro de três
# algarismos e imprima a soma desse número com seu inverso. Exemplo:
# Digite um número inteiro com três algarismos: 123
# O inverso do número é: 321
# A soma é: 123 + 321 = 444

num = input("Digite um número inteiro: ")
inverso = " "
for x in num:
    inverso = x + inverso
    numero = int(num)
    numero1 = int(inverso)

    soma = numero + numero1
print(inverso)
print(soma)