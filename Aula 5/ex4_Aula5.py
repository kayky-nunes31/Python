num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Indique qual operação deseja fazer: ")

if operacao == "+":
    conta = num1 + num2
    print(f"Esse foi o valor da operação escolhida - Soma: {conta}")
if operacao == "/":
    conta = num1 / num2
    print(f"Esse foi o valor da operação escolhida - Divisão: {conta}")
if operacao == "-":
    conta = num1 - num2
    print(f"Esse foi o valor da operação escolhida - Subtração: {conta}")
if operacao == "*":
    conta = num1 * num2
    print(f"Esse foi o valor da operação escolhida - Multiplicação: {conta}")
else:
    print("Operação inválida")


input("Conferindo!!!")