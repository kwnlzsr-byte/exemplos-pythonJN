import os
os.system("cls")

print("Qual o tipo de veiculo?:")

veiculo = int(input("1 - Carro\n2 - Moto\n3 - Caminhão\n\n"))

if(veiculo == 1):
    print("O veiculo é um carro! O valor do pedágio é: R$10")
elif(veiculo == 2):
    print("O veiculo é uma moto! O valor do pedágio é: R$5")
elif(veiculo == 3):
    print("O veiculo é um caminhão! O valor do pedágio é: R$20")
else:
    print("O tipo de veiculo é inválido")