import random

# Função para jogar novamente
def play_again():
    return input("\nDeseja jogar novamente? (s/n): ").lower() == 's'

# Função para exibir suposições dos jogadores
def display_guesses(player, guesses):
    print(f"Suposições do Jogador, {player}: {guesses}")

# Função para exibir a vez do jogador humano
def player_turn():
    print(f"\n====== {player_name}, é a sua vez! ======")
    return int(input("Digite um número entre 1 e 100: "))

# Função para exibir a vez do computador
def computer_turn():
    print(f"\n====== Vez do Computador! ======")
    computer_guess = random.randint(1, 100)
    print(f"O computador palpita: {computer_guess}")
    return computer_guess
    
# Função para verificar o vencedor do jogo
def check_winner(player_name, secret_number, guess, guesses):
    if guess == secret_number:
        print(f"\nParabéns, {player_name}! Você acertou! O número era: {secret_number}\n")
        return True
    elif guess < secret_number:
        print(f"{player_name}, o seu palpite é menor. Tente novamente!")
    else:
        print(f"{player_name}, o seu palpite é maior. Tente novamente!")
    guesses.append(guess)
    return False

# Saudação e entrada do nome do jogador
print("************************************************************")
player_name = input("Olá! Bem-vindo(a) ao Guess the Number!\nPor favor, digite seu nome: ")
print(f"Olá, {player_name}! Vamos testar sua habilidade em adivinhar números!")
print("************************************************************")

while True:
    secret_number = random.randint(1, 100)
    print(secret_number)
    
    player_guesses = []
    computer_guesses = []

    while True:
        human_guess = player_turn()
        if check_winner(player_name, secret_number, human_guess, player_guesses):
            break

        computer_guess = computer_turn()
        if check_winner("Computador", secret_number, computer_guess, computer_guesses):
            break
    # Exibir suposições dos jogadores
    display_guesses(player_name, player_guesses)
    display_guesses("Computador", computer_guesses)

    # Finalizar jogo
    if not play_again():
      print("\n╔════════════════════════════════════════════════════════════╗")
      print(f"║ Obrigado por jogar, {player_name}! Esperamos que tenha se divertido. ║")
      print("║ Até a próxima! 🕹️  🎲                                       ║")
      print("╚════════════════════════════════════════════════════════════╝")
      break
