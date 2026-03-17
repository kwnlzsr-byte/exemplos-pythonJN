import os
os.system("cls")

vl_carro = float(input("Qual foi a velocidade atingida?: "))

if(vl_carro > 80):
    print("Você ultrapassou o limite de velocidade estabelecido! Você está Multado!!")
else:
    print("Tudo certo! Você está no limite de velocidade!")