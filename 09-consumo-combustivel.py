import os
os.system("cls")

km_percorridos = float(input("Quantos quilômetros foram percorridos?: "))
combustivel_gasto = float(input("Quantos litros de combustível foram gastos?: "))

media = km_percorridos / combustivel_gasto

print("A média de gasto do seu veiculo foi: ", media)