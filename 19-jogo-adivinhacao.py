import os
import random
os.system("cls")

print("Bem vindo ao jogo da adivinhação!!")

n_secreto = random.randint(1,10)
palpite = int(input("Digite um número: "))

if(palpite == n_secreto):
    print("Você acertou o número secreto! Parabéns!")
elif(palpite > n_secreto):
    print("O palpite é maior que o número secreto.")
elif(palpite < n_secreto):
    print("O seu palpite é menor que o número secreto.")

print(f"O número secreto foi: {n_secreto}")