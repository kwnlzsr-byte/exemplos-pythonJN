import os
os.system("cls")

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura * altura)

if(imc < 16.9):
    print("Você está muito abaixo do peso!")
elif(imc >= 17 and imc <= 18.4):
    print("Você está abaixo do peso!")
elif(imc >= 18.5 and imc <=24.9):
    print("Seu peso está normal.")
elif(imc >= 25 and imc <= 29.9):
    print("Você está acima do peso.")
elif(imc >= 30 and imc <=34.9):
    print("Você está no nível Obesidade Grau I")
elif(imc >= 35 and imc <= 40):
    print("Você está nível Obesidade Grau II")
elif(imc > 40 and imc <= 65):
    print("Você está no nível Obesidade Grau III")
elif(imc > 65):
    print("Primeiro, como você está vivo? segundo, VA AO MÉDICO!!!")