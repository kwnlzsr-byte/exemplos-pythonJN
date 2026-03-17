import os
os.system("cls")

ano = float(input("Digite um número:"))

resto = ano % 4

if resto == 0:
    print("O ano é bissexto!")

else:
    print("O ano NÃO é bissexto!")