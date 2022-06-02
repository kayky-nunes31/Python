palavra = input("Digite uma palavra: ").upper()
temp = ''
for letra in palavra:
    if letra in temp: continue
    n = palavra.count(letra)
    temp += letra
    print(f"{letra} - {n}")