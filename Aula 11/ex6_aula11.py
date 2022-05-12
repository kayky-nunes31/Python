lista_num = []

soma = 0

while True:
    num = int(input("Digite números inteiros: "))
    continuar = input("Deseja continuar? ")
    lista_num.append(num)

    if continuar in "Nn":
        break

for i in lista_num:
    soma += i

media = soma / len(lista_num)
qtd_num = len(lista_num)
print(f"Essa é a média dos números digitados: {media}")
print(f"Essa é a quantidades de números armazenados: {qtd_num}")