import os
os.system("cls")

def exibir_menu():
    print("==== Conversor de moedas ====")
    print("[1] - Converter DOLAR -> REAL")
    print("[2] - Converter REAL -> DOLAR")
    print("[3] - Sair\n")

def limpar_tela():
    os.system("cls")

#Dolar para real
def dolar_pra_real(quantia_dolar, cotacao):
    total_reais = quantia_dolar * cotacao
    return total_reais

#Real para dolar  
def real_pra_dolar(quantia_real, cotacao):
    total_dolares = quantia_real / cotacao
    return total_dolares

def sair():
    exit()

#Função main
def main():
    limpar_tela()
    
    exibir_menu()
    opcao = int(input("Escolha uma opção: [1]  [2]  [3]\n"))

    if(opcao == 1):
        quantia_dolar = float(input("Informe a quantia de dolares: ").replace(",", "."))
        cotacao = float(input("Informe a cotação: ").replace(",", "."))
        resultado = dolar_pra_real(quantia_dolar, cotacao)
        print(f"A quantidade de dolares em reais é: R${resultado}")

    elif(opcao == 2):
        quantia_real = float(input("Informe a quantia de reais: ").replace(",", "."))
        cotacao = float(input("Informe a cotação:").replace(",", "."))
        resultado = real_pra_dolar(quantia_real, cotacao)
        print(f"A quantidade de reais em dolares é: ${resultado}")

    elif(opcao == 3):
        print("Ok! Finalizando...")
        sair()

main()