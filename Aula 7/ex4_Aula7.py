#Escreva um algoritmo que leia um grupo de valores reais e determine quantos
#valores são positivos e quantos são negativos. Determine, também, qual é o
#menor desses valores. Utilize o comando de repetição que desejar.
import math

qtd_positivo = 0
qtd_negativo = 0

qte = 0
while True:
    num = int(input("Digite um valor inteiro (0 para sair)"))
    if num > 0:
       qtd_positivo = qtd_positivo + 1
    elif num < 0:
        qtd_negativo = qtd_negativo + 1 
    elif num == 0:
        break
    qte = qte + 1
    menor = math.ceil(num)

print(f"O total de números é {qte}, a quantidade de números positivos {qtd_positivo} e a quantidade de números negativos {qtd_negativo}")
print(f"Esse é o menor número {menor}")