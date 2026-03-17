import os
os.system("cls")

hr_estudadas = int(input("Quantas horas por dia você estuda?: "))

if(hr_estudadas <= 2):
    print("Você estuda pouco! Se esforce mais!")
elif(hr_estudadas > 2 and hr_estudadas <= 4):
    print("Você estuda o necessario. Parabens!")
elif(hr_estudadas > 4):
    print("Você estuda MUITO! Talvez devesse descansar um pouco?")