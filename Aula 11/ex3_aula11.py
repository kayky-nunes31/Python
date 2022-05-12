lista_placas = []
lista_multas = []
soma = 0
qtd_carros = 0

for i in range(15):
    placa = input("Digite a placa do carro: ")
    multa = int(input("Digite o valor da multa: "))

    if placa > 0:
        lista_placas.append(placa)
    elif multa > 0:
        lista_multas.append(multa)

for mult in lista_multas:
    soma += mult
    if multa >= 300:
        qtd_carros = qtd_carros + 1

media = soma/15
print(f"Essa é a média das multas digitadas: {media}")
print(f"Essa é a quantidade de carros com multa maior ou igual a R$300.00: {qtd_carros}")