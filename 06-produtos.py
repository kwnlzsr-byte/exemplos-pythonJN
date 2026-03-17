import os
os.system ("cls")

print("Bem-Vindo ao Walmart!!")

produto = input("Nome do produto: ")
quantidade = int(input("Digite a quantidade desejada: "))
preco = float(input("E qual o preço do produto?: "))

total = preco * quantidade
print("O total a pagar é: ", total)

if(quantidade <= 5):
    desconto = total * 0.02
elif(quantidade > 5 and quantidade <= 10):
    desconto = total * 0.03
elif(quantidade > 10):
    desconto = total * 0.05

total_desconto = (total - desconto)

print("============================")
print(f"total:{total} \ndesconto:{desconto:.2f} \ntotal_desconto:{total_desconto:.2f}")
print("Obrigado por comprar!")