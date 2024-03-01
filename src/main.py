import random

numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)

while True:
    # Vez do jogador
    palpite_humano = int(input("Digite um número entre 1 e 100: "))

    if palpite_humano == numero_aleatorio:
        print(f"Parabéns!! Você acertou o número! O número secreto era: {numero_aleatorio}")
        break
    elif palpite_humano < numero_aleatorio:
        print("O número é maior, tente novamente!")
    else:
        print("O número é menor, tente novamente!")
    
    # Vez do computador
    palpite_computador = random.randint(1, 100)
   
    print(f"O computador palpita: {palpite_computador}")

    if palpite_computador == numero_aleatorio:
      print(f"O computador acertou o número! O número secreto era: {numero_aleatorio}")
      break
    elif palpite_computador < numero_aleatorio:
      print("O palpite do computador é menor.")
    else:
      print("O palpite do computador é maior.")