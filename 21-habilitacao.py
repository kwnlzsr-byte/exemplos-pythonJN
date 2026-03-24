import os
os.system("cls")

nome = input("Qual o seu nome?: ")
idade = int(input("Qual a sua idade?: "))

if idade >= 18:
    print("Você tem a idade necessária, mas ainda não pode dirigir!")
    
    habilitacao = int(input("Você possui habilitação?\n 1- Sim 2- Não\n"))
    if habilitacao == 1:
        print("Parabéns!! Você pode dirigir!!")

    elif habilitacao == 2:
        print("Opa! Você não pode dirigir!")

    else:
        print("Digite um valor válido.")


elif idade < 18:
    print("Você ainda não tem a idade necessária. Volte mais tarde.")
    
