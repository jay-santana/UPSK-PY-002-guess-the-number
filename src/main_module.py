"""
Este módulo contém o jogo Guess the Number, onde um jogador tenta adivinhar um número secreto.
"""
import random

# Função para jogar novamente
def play_again(user_input=None):
    """
    Pergunta ao usuário se deseja jogar novamente.

    Args:
        user_input (str, optional): A entrada do usuário. Defaults to None.

    Returns:
        bool: True se o usuário deseja jogar novamente, False caso contrário.
    """
    while True:
        if user_input is None:
            user_input = input("\nDeseja jogar novamente? (s/n): ").lower()
        if user_input == 's':
            return True
        if user_input == 'n':
            return False
        print("Por favor, insira apenas 's' para sim ou 'n' para não.")
        # Reset para solicitar novamente a entrada do usuário
        user_input = None

# Função para exibir suposições dos jogadores
def display_guesses(player, guesses):
    """
    Exibe as suposições de um jogador.

    Args:
        player (str): Nome do jogador.
        guesses (list): Lista de suposições.
    """
    output = f"Suposições do Jogador, {player}: {guesses}"
    print(output)
    return output

# Função para exibir a vez do jogador humano
def player_turn(player_name):
    """
    Solicita a suposição de um jogador humano.

    Args:
        player_name (str): Nome do jogador.

    Returns:
        int: A suposição do jogador.
    """
    while True:
        try:
            guess = int(input(f"\n====== {player_name}, é a sua vez! ======\nDigite um número entre 1 e 100: "))
            if 1 <= guess <= 100:
                return guess
            # Caso o usuário insira um valor fora do intervalo determinado
            print("Por favor, insira um número dentro do intervalo de 1 a 100.")
        # Caso o usuário insira um valor que não pode ser convertido para um número inteiro
        except ValueError:
            print("Por favor, insira um número válido.")

# Função para exibir a vez do computador
def computer_turn(low, high):
    """
    Realiza a suposição do computador.

    Args:
        low (int): Limite inferior do intervalo.
        high (int): Limite superior do intervalo.

    Returns:
        int: O palpite do computador.
    """
    print("\n====== Vez do Computador! ======")
    computer_guess = (low + high) // 2
    print(f"O computador palpita: {computer_guess}")
    return computer_guess

# Função para verificar o vencedor do jogo
def check_winner(player_name, secret_number, guess, guesses, attempts):
    """
    Verifica se o jogador venceu o jogo.

    Args:
        player_name (str): Nome do jogador.
        secret_number (int): O número secreto.
        guess (int): A suposição do jogador.
        guesses (list): Lista de suposições.
        attempts (int): O número de tentativas.

    Returns:
        bool: True se o jogador venceu, False caso contrário.
    """
    if guess == secret_number:
        if attempts == 1:
            print(f"\nParabéns, {player_name}! Você acertou em 1 tentativa! O número secreto era: {secret_number}\n")
        else:
            print(f"\nParabéns, {player_name}! Você acertou em {attempts} tentativas! O número secreto era: {secret_number}\n")
        return True
    if guess < secret_number:
        print(f"{player_name}, o seu palpite é menor. Tente novamente!")
    else:
        print(f"{player_name}, o seu palpite é maior. Tente novamente!")
    guesses.append(guess)
    return False

if __name__ == "__main__":

    while True:
        # Saudação e entrada do nome do jogador
        print("************************************************************")
        player_name_input = input("Olá! Bem-vindo(a) ao Guess the Number!\nPor favor, digite seu nome: ")
        # Verifica se o nome não está vazio, contém apenas letras e tem pelo menos 2 caracteres
        if player_name_input.strip() and player_name_input.isalpha() and len(player_name_input) >= 2:
            print(f"Olá, {player_name_input}! Vamos testar sua habilidade em adivinhar números!")
            print("************************************************************")
            break
        # Caso o usuário não insira um nome
        print("Por favor, insira um nome válido com pelo menos 2 letras.")

    while True:
        SECRET_NUMBER = random.randint(1, 100)
        # print(secret_number)

        player_guesses = []
        computer_guesses = []
        COMPUTER_LOW, COMPUTER_HIGH = 1, 100 # Intervalo inicial do palpite do computador
        ATTEMPTS = 0 # Inicializa o contador de tentativas

        while True:
            ATTEMPTS += 1  # Incrementa o número de tentativas
            human_guess = player_turn(player_name_input)
            if check_winner(player_name_input, SECRET_NUMBER, human_guess, player_guesses, ATTEMPTS):
                break
            COMPUTER_GUESS = computer_turn(COMPUTER_LOW, COMPUTER_HIGH)
            if check_winner("Computador", SECRET_NUMBER, COMPUTER_GUESS, computer_guesses, ATTEMPTS):
                break
            # Ajuste do intervalo com base no palpite do computador
            if COMPUTER_GUESS < SECRET_NUMBER:
                COMPUTER_LOW = COMPUTER_GUESS + 1
            else:
                COMPUTER_HIGH = COMPUTER_GUESS - 1

        # Exibir suposições dos jogadores
        display_guesses(player_name_input, player_guesses)
        display_guesses("Computador", computer_guesses)

        # Perguntar se deseja jogar novamente e mensagem para finalizar o jogo
        if not play_again():
            print("\n╔═══════════════════════════════════════╗")
            print(f"  Obrigado por jogar, {player_name_input}!  ")
            print("  Esperamos que tenha se divertido.     ")
            print("  Até a próxima! 🕹️  🎲                  ")
            print("╚═══════════════════════════════════════╝")
            break
