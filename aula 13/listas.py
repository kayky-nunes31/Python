nomes = []
salario = []

while True:
    nome = input("Digite um nome <ENTER> para sair: ")
    if nome == '': break
    #nomes += [nome]
    nomes.append(nome)
    money = float(input(f"Digite o salário do {nome}: R$"))
    salario.append(money)

pesq = input("\nDigite o nome do eliminado: ")
if pesq in nomes:
    i = nomes.index(pesq)
    print(f"O funcionário {nomes} recebe R$ {salario[i]}!")
else: print("Nome não encontrado!!!!!!!!!")

#pop sem nada sempre elimina o ultimo da lista
#mas lembrando que a contagem sempre começa pelo 0