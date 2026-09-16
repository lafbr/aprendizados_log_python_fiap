import os
os.system ("cls")

# ler o valor da compra:

compra = float(input("Compra: R$"))


#se a compra for até 500:
if compra <= 500:

    # Calcular o desconto de 10%:
    compra = compra * 0.9

else:
    # Caso contrario, desconto de 20%
    compra = compra * 0.8



# Exibir o novo valor da compra
print("Compra: R$", compra)
