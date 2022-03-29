produto = input("Digite o nome do produto: ")
vlr_compra = float(input("Digite o valor da da compra: "))

if vlr_compra < 10.00:
    vlr_venda = vlr_compra * 0.7
    print(f"O produto {produto}, teve {vlr_venda} de lucro")
elif vlr_compra < 30.00:
    vlr_venda = vlr_compra * 0.5
    print(f"O produto {produto}, teve {vlr_venda} de lucro")
elif vlr_compra < 50.00:
    vlr_venda = vlr_compra * 0.4
    print(f"O produto {produto}, teve {vlr_venda} de lucro")
elif vlr_compra >= 50.00:
    vlr_venda = vlr_compra * 0.3
    print(f"O produto {produto}, teve {vlr_venda} de lucro")

input("Conferindo!!!")