#lista1 = [52, 157, 44, 27, 97, 23, 13, 14, 364.5]

#sum_var = sum(lista1)
#max_var = max(lista1)
#min_var = min(lista1)
#len_var = len(lista1)

#print(sum_var)
#print(max_var)
#print(min_var)
#print(len_var)


#Criando uma lista com os números binários: 2, 4, 6, 8 à 1024.
numeros_binarios = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

#Função para somar elementos em índices específicos:
def soma_indices(lista, indices):
    soma = 0
    for index in indices:
        if 0 <= index < len(lista):
            soma += lista[index]
        else:
            print(f"Índice {index} fora do intervalo.")
    return soma

indice_para_soma = [0, 2, 7, 9]
resultado = soma_indices(numeros_binarios, indice_para_soma)

print(f"A soma dos elementos nos índices {indice_para_soma} é: {resultado}")