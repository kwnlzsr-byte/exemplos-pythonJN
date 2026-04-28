import os
os.system("cls")

def somar(n1,n2):
    resultado = n1 + n2
    return resultado 

def subtrair(n1,n2):
    resultado = n1 - n2
    return resultado 

def multiplicar(n1,n2):
    resultado = n1 * n2
    return resultado 

def dividir(n1,n2):
    resultado = n1 / n2
    return resultado 

def saida():
    print("Operação inváloda")
    input("Pressione enter para encerrar ")
    exit()

print("Bem Vindo a Calculadora 1.14.5")
print("==============================")

n1 = int(input("Informe o Primeiro Número: "))
n2 = int(input("Informe o Segundo Número: "))

print("Escolha uma das opções abaixo:\n [1] - Somar\n [2] - Subtrair\n [3] - Multiplicar\n [4] - Dividir")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    print(f"O resultado da Soma é: {somar(n1,n2)}")
elif opcao == 2:
    print(f"O resultado da Subtração é: {subtrair(n1,n2)}")
elif opcao == 3:
    print(f"O resultado da Multiplicação é: {multiplicar(n1,n2)}")
elif opcao == 4:
    print(f"O resultado da Divisão é: {dividir(n1,n2)}")
else:
    saida()
