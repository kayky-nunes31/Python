agua = float(input("Digite o valor da sua conta de água: "))
luz = float(input("Digite o valor da sua conta de luz: "))
telefone = float(input("Digite o valor da sua conta de telefone: "))
salario = float(input("Digite o valor do seu salário: "))

contas = agua + luz + telefone

if salario > contas:
    restante = salario - contas
    print(f"Salário sufuciente, ainida sobrou a quantia de {restante}")
else:
    print("Salário insuficiente!")

input("Conferindo!")