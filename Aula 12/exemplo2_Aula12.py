def soma(a, b):
    a = a + b
    return(a)

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(soma(a, b))
#print(a)

#variaveis dentro do método, só existem dentro do método
#após fechar o método, essas variavel "deixa de existir"

#podemos chamar de escopo de var