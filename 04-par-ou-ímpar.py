import os
os.system("cls")

n1 = float(input("Digite um número:"))

resto = n1 % 2

if resto == 0:
    print("o número é par!")

else:
    print("O número é impar!")