import random

# Função para jogar novamente
def jogar_novamente():
    resposta = input("Deseja jogar novamente? (s/n): ")
    return resposta.lower() == 's'

# Saudação e entrada do nome do jogador
print("************************************************************")
nome_jogador = input(" Olá! Bem-vindo(a) ao Guess the Number!\n Por favor, digite seu nome: ")
print(f" Olá, {nome_jogador}! Vamos testar sua habilidade em adivinhar números!")
print("************************************************************")

while True:
  numero_aleatorio = random.randint(1, 100)
  print(numero_aleatorio)

  suposicoes_jogador = []
  suposicoes_computador = []

  while True:
    # Vez do jogador
    print(f"\n====== {nome_jogador}, é a sua vez! ======")
    palpite_humano = int(input("Digite um número entre 1 e 100: "))
    suposicoes_jogador.append(palpite_humano)

    if palpite_humano == numero_aleatorio:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f" Parabéns, {nome_jogador}!! Você acertou!")
        print(f" O número secreto era: {numero_aleatorio}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        break
    elif palpite_humano < numero_aleatorio:
        print(f"{nome_jogador}, o seu palpite é menor. Tente novamente!")
    else:
        print(f"{nome_jogador}, o seu palpite é maior. Tente novamente!")
    
    # Vez do computador
    print(f"\n====== Vez do Computador! ======")
    palpite_computador = random.randint(1, 100)
    suposicoes_computador.append(palpite_computador)
   
    print(f"O computador palpita: {palpite_computador}")

    if palpite_computador == numero_aleatorio:
      print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print(f" O computador acertou o número!")
      print(f" O número secreto era: {numero_aleatorio}")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      break
    elif palpite_computador < numero_aleatorio:
      print("O palpite do computador é menor.")
    else:
      print("O palpite do computador é maior.")
    
  print("\nSuposições do jogador:", suposicoes_jogador)
  print("Suposições do computador:", suposicoes_computador)

  if not jogar_novamente():
    print("\n╔═══════════════════════════════════╗")
    print(f"║ Obrigado por jogar, {nome_jogador}!          ║") 
    print("║ Esperamos que tenha se divertido. ║")
    print("║ Até a próxima! 🕹️  🎲              ║")
    print("╚═══════════════════════════════════╝")
    break

 