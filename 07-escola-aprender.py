import os
os.system("cls")

nivel = int(input("Entre com o nível do professor: "))
qtd_aulas = int(input("Diga a quantidade de aulas: "))

if(nivel == 1):
    salario = qtd_aulas * 12
elif(nivel == 2):
    salario = qtd_aulas * 17
elif(nivel == 3):
    salario = qtd_aulas * 25
else:
    print("O nivel digitado é invalido!")

print(f"O salário do professor: R${salario:.3f}")