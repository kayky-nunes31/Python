

qtd_m = 0
qtd_f = 0

alturaM = 0
alturaF = 0

while True:
    sexo = input("Digite seu sexo m/f (0 para sair): ")
    if sexo in "mM":
        print("Olá Sr! Qual a sua Altura?")
        qtd_m = qtd_m + 1
    else :
        print ("Olá Sra! Qual a sua Altura?")
        qtd_f = qtd_f + 1

    altura = float(input("Digite sua altura (0 para sair): "))
    if sexo in "mM" and altura > 0:
        alturaM = alturaM + altura 
    elif altura == 0:
        break
    else :
        alturaF = alturaF + altura

#    divisaoM = alturaM / qtd_m
#    divisaoF = alturaF / qtd_f

    print(f"A soma das alturas dos homens é: {alturaM}")
    print(f"Quantidade de homens {qtd_m}")
    print(f"Quantidade de mulheres {qtd_f}")


    input("conferindo")