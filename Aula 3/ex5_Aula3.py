import math

#Faça uma programa em Python que peça do usuário um valor em graus para
#um ângulo. Converta-o para radianos e, usando funções da biblioteca math,
#imprima o seno, cosseno e tangente deste ângulo.

valor_graus = float(input("Digite um valor em graus: "))
radiano = math.radians(valor_graus)

#Imprimindo Seno, Cosseno e Tangente
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f"Esse é o valor do radiano em Seno: {seno}; Em Cosseno: {cosseno}; Em Tangente: {tangente}")

input("Conferindo")