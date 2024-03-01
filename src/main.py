import random

numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)

while True:
    palpite_humano = int(input("Digite um número entre 1 e 100: "))

    if palpite_humano == numero_aleatorio:
        print("Parabéns!! Você acertou o número!")
        break
    elif palpite_humano < numero_aleatorio:
        print("O número é maior, tente novamente!")
    else:
        print("O número é menor, tente novamente!")