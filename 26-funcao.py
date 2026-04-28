import os
os.system("cls")

#Função
def escreva():
    print("Natsuki <3")

escreva()

#Função com parâmetros
def exibir_dados(nome, idade, email):
    print(f"seu nome é: {nome}")
    print(f"você tem {idade} anos")
    print(f"Seu email é: {email}")
    print("=" * 50)

exibir_dados("Natsuki", 16, "suki@gmail.com")
exibir_dados("Kewin", 16, "kwnlzsr@gmail.com")

#Função com retorno
def somar(num1, num2):
    resultado = num1 + num2
    return resultado

total = somar(10,20)
print(f"O total será: {somar(10,20)}")
