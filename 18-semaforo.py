import os
os.system("cls")

cor_semáforo = int(input("Qual a cor do semáforo? \nDigite 1 para vermelho, 2 para amarelo e 3 para verde: \n"))

if(cor_semáforo == 1):
    print("O sinal está vermelho, você deve parar!")
elif(cor_semáforo == 2):
    print("O sinal está amarelo, você deve desacelerar!")
elif(cor_semáforo == 3):
    print("O sinal está verde, você pode passar!")
else:
    print("Sinal indefinido, por precaução, pare.")