import os
os.system("cls")

print("Seja Bem Vindo ao App Minha Conta!")
print("==================================")

def dividir(conta,pessoas):
    resultado = conta / pessoas
    return resultado

def saida():
    input("Encerrando programa, aperte enter para continuar")
    exit()

conta = float(input("Informe o valor da conta: ").replace(",", "."))
pessoas = int(input("Informe a quantidade de pessoas: "))

print(f"O valor que cada pessoa deverá pagar é: {dividir(conta,pessoas)}")
print("Obrigado por usar o app Minha Conta")

saida()