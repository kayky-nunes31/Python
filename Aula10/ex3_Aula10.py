palavra = input("Digite uma palavra: ")

#letra_palavra1 = input("Digite uma letra que deseja: ")
letra1 = palavra.count(input("Digite uma letra para saber a quantidade: "))

#letra_palavra2 = input("Digite uma letra que deseja: ")
letra2 = palavra.count(input("Digite uma letra para saber a quantidade: "))

#letra_palavra3 = input("Digite uma letra que deseja: ")
letra3 = palavra.count(input("Digite uma letra para saber a quantidade: "))

print(f"O caractere {palavra[1]} aparece {letra1} vezes")
print(f"O caractere {palavra[2]} aparece {letra2} vezes")
print(f"O caractere {palavra[4]} aparece {letra3} vezes")


#for i in range(3):
#    letra_palavra = input("Digite uma letra que deseja: ")
#    letra = palavra.count(input("Digite uma letra para saber a quantidade: "))
#print(f"O caractere {palavra[1]} aparece {letra} vezes")
#print(f"O caractere {palavra[2]} aparece {letra} vezes")
#print(f"O caractere {palavra[4]} aparece {letra} vezes")