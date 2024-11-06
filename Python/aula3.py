#hariel = ['Daniel vai ser pai', 2, 5.7, 'Silvio Santos foi jogar no Vasco', 87, 93.0]
#print(hariel[0], hariel[2])

#vetor = [20,21,22,23,24,25]
#print(vetor[3])



lista1 = ['moto','jato','tanque']
#lista1.append('carro') - Adiciona um item no final do vetor.

#lista1.insert(2,'avião') - Adiciono um item na posição que eu desejo.

#lista1.remove('jato') - Remove o item que desejarmos

#del lista1[2] - Deleta o item da posição que desejarmos





print(lista1)
#remove - lista1.remove('carro')
#append - lista1.append('carro')
#insert - lista1.insert(1, 'carro')
#del - del lista1[3]

# Inicializa uma lista vazia
valores = []

# Loop while para inserção de valores
while True:
    # Solicita ao usuário para inserir um valor
    entrada = input("Digite um valor para adicionar à lista (ou 'sair' para terminar): ")
    
    # Condição para sair do loop
    if entrada.lower() == 'sair':
        break
    
    # Adiciona o valor à lista
    valores.append(entrada)

# Exibe a lista final
print("Valores na lista:", valores)