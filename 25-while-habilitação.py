import os
os.system("cls")

resposta = "sim"

while (resposta == "sim"):
    nome = input("\nQual o seu nome?: ")
    idade = int(input("Qual a sua idade?: "))

    if idade >= 18:
        habilitacao = int(input("Você possui habilitação?\n 1- Sim 2- Não\n"))

        if habilitacao == 1:
            print("Você pode dirigir!\n")
        elif habilitacao == 2:
            print("Você não pode dirigir, pois não tem habilitação.\n")
    else:
        print("Você não tem idade suficiente para dirigir!")
    
    resposta = input("Você quer executar o programa novamente? (sim ou não)\n")
    if resposta == "não":
        print("Okay!")

print("Programa finalizado! Volte sempre!")