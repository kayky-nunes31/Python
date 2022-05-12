lista_salarios = []
soma = 0
qtd_menor = 0

for i in range(10):
    salario = float(input("Digite o salário: "))
    lista_salarios.append(salario)
    if salario < 850:
        qtd_menor = qtd_menor + 1

for s in lista_salarios:
    soma += s

media = soma / len(lista_salarios)
print(f"Essa é a média dos salários: {media}")
print(f"Esse é o maior salário da empresa: ")
print(f"Essa é a quantidade de salários menores que R$850,00: {qtd_menor}")
print(f"Esse são todos os salários: {lista_salarios}")