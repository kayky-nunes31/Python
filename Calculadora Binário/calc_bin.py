lista_bin = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

numero_binario = input("Digite um número binário: ")

soma = 0

try:
    for i in range(len(numero_binario)):
        if numero_binario[i] not in '01':
            raise ValueError("Entrada inválida")
        if numero_binario[i] == '1':
            soma += lista_bin[len(numero_binario) - 1 - i]

    print(f"A soma dos valores correspondentes é: {soma}")

except ValueError as e:
    print(e)