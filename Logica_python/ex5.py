mercadoria = int(input("Preço da mercadoria"))
desconto = int(input("desconto(%): "))
calculo = (desconto/100)*mercadoria
print(mercadoria - calculo)