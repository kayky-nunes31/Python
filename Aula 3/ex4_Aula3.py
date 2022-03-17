#Escreva um programa em Python para calcular o valor de uma prestação em
#atraso (prestacao). Para isso, obtenha o valor da prestação (valorPrestacao), a
#porcentagem de multa pelo atraso (multa) e a quantidade de dias de atraso
#(qtdeDias). Calcular e mostrar o valor da prestação atualizado, sabendo que:

#prestação = valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

valorPrestacao = float(input("Digite o valor da sua prestação em atraso aqui: "))
multa = float(input("Digite o valor da porcentagem: "))
qtdeDias = float(input("Digite a quantidade de dias: "))

prestacao = valorPrestacao + ( valorPrestacao * (multa/100) * qtdeDias)

print(f"Esse é o valor da prestação {prestacao}")

input("Conferindo")