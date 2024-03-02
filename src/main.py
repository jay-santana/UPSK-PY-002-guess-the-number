import random

# Função para jogar novamente
def jogar_novamente():
    resposta = input("Deseja jogar novamente? (s/n): ")
    return resposta.lower() == 's'

while True:
  numero_aleatorio = random.randint(1, 100)
  print(numero_aleatorio)

  suposicoes_jogador = []
  suposicoes_computador = []

  while True:
    # Vez do jogador
    palpite_humano = int(input("Digite um número entre 1 e 100: "))
    suposicoes_jogador.append(palpite_humano)

    if palpite_humano == numero_aleatorio:
        print(f"Parabéns!! Você acertou o número! O número secreto era: {numero_aleatorio}")
        break
    elif palpite_humano < numero_aleatorio:
        print("O número é maior, tente novamente!")
    else:
        print("O número é menor, tente novamente!")
    
    # Vez do computador
    palpite_computador = random.randint(1, 100)
    suposicoes_computador.append(palpite_computador)
   
    print(f"O computador palpita: {palpite_computador}")

    if palpite_computador == numero_aleatorio:
      print(f"O computador acertou o número! O número secreto era: {numero_aleatorio}")
      break
    elif palpite_computador < numero_aleatorio:
      print("O palpite do computador é menor.")
    else:
      print("O palpite do computador é maior.")
    
  print("\nSuposições do jogador:", suposicoes_jogador)
  print("Suposições do computador:", suposicoes_computador)

  if not jogar_novamente():
    print(f"\nObrigado por jogar! Esperamos que tenha se divertido. Até a próxima!")
    break

 