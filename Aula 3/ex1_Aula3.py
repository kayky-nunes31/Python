#valores da altura do tronco da pirâmide (h)
#o valor da base menor (Bmenor)
#base maior (Bmaior)

h = float(input("Indique o valor da Altura do Tronco da Pirâmide: "))
Bmenor = float(input("Indique o valor da Base Menor: "))
Bmaior = float(input("Indique o valor da Base Maior: "))

volume = h/3 * (Bmaior ** 2 + Bmenor ** 2 + (Bmaior ** 2 * Bmenor ** 2) ** 0.5)

print(f"Esse é o volume do Tronco da Pirâmide: {volume}")

input("Conferindo")