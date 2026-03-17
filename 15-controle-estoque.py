import os
os.system("cls")

qtd_produtos = int(input("Digite a quantidade de produtos em estoque: "))

if(qtd_produtos < 5):
    print("O estoque está baixo!")
else:
    print("O estoque está normal!")