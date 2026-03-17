
#1 passo - variaveis e entradas
print("Seja bem vindo ao Boletim Virtual do aluno KEWIN")

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
nota03 = float(input("Digite a terceira nota: "))

media = (nota01 + nota02 + nota03) / 3

print("Sua média foi: ", media)

if(media>=7):
        print("Você foi aprovado! Parabéns!!")
elif(media>=4 and media<=6):
        print("Você foi reprovado")
else:
        print("Você foi reprovado")