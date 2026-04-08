# Calculo de IMC
# IMC = peso / (altura * altura)

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)
print(f"{nome} tem {peso} kg e {altura} m de altura.")
print(f"Seu IMC é {imc:.2f}.")