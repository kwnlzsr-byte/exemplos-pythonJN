import os
os.system("cls")

nm_usuário = str(input("Digite o nome de usuário: "))
senha = int(input("Digite a senha: "))

if(nm_usuário == "admin" and senha == 123):
    print("Você logou na sua conta com sucesso!!")
else:
    print("Usuario ou senha incorretos, recarregue e tente novamente.")