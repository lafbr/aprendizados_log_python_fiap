import os
os.system ("cls")
nome = "Edson de Oliveira"
idade = 52
altura = 1.75
# Formatação 1 - Clássica: utilizando virgula   | exibe qualquer tipo de dado

print("Nome:", nome, "Idade:", idade, "Altura:", altura)

print("\nNome:", nome, "\nIdade:", idade, "\nAltura:", altura)

#Formtação 1 - concatenação + : concatena valores str()

print()
print("Nome: " + nome)
print("Nome: " + nome)
print("Nome: " + nome)


# Formatacao 3 - usando a funcao format()

print("{0}\nNome: {1} \nIdade: {2} \nAltura:" .format(nome, idade , altura))
print("{0}\nNome: {1} \nIdade: {2} \nAltura:" .format(nome, idade , altura))

#formatação 4 - f print


print(f"{0}\nNome: {1} \nIdade: {2} \nAltura:" .format(nome, idade , altura))

#plus - triple quotes ~~~~  ~~~~

print(f"""
      Nome: {nome}
      Idade:{idade}
    Altura: {altura}
      
      
      
      
      """)

#formatando os dados:


produto1 = "café"
produto2 = "Alface"
produto3 = "Carne de soja"

qtd1 = 23
qtd2 = 857
qtd3 = 4949

valor1 = 1.3452
valor2 = 231.442
valor3 =  23441.3

os.system( "cls")

