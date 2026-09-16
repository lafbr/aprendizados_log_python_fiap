import os
os.system ("cls")

# Atribuir salario fixo
sal_fixo = 1600

# Ler a venda

venda = float(input("Venda: R$:"))

#se vendeu mais de 100 mil

if venda > 1000000:

# calcular comissão de 6%
comissao = venda * 0.06

# Caso contrario
else:

# Calcular a comissão de 4%


comissao = venda * 0.04


print

