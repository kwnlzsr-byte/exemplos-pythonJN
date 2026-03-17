import os
os.system("cls")

idade = float(input("Escreva sua idade: "))
nascimento = float(input("Digite sua data de nascimento: "))

idade = 2026 - nascimento
idade_futura = 2035 - nascimento

print("Sua idade é: ", idade)
print("Sua idade em 2035 será: ", idade_futura)