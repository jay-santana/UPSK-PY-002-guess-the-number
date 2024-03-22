from main_module import computer_turn, player_turn, play_again, display_guesses, check_winner
from unittest.mock import patch

# Testes para função jogar novamente
# Verifica se a função retorna True quando o usuário insere 's'
def test_play_again_yes():
    # Simula entrada válida 's'
    with patch('builtins.input', return_value='s'):
        assert play_again() == True

# Verifica se a função retorna False quando o usuário insere 'n'
def test_play_again_no():
    # Simula entrada válida 'n'
    with patch('builtins.input', return_value='n'):
        assert play_again() == False

# Verifica se a função solicita uma entrada válida novamente ao receber um valor inválido
def test_play_again_invalid_input_then_yes():
    # Simula entrada inválida 'x' e então entrada válida 's'
    with patch('builtins.input', side_effect=['x', 's']): 
        assert play_again() == True

#Teste para função computer_turn
def test_computer_turn():
    # verifique se o palpite do computador está dentro do intervalo fornecido
    low, high = 1, 100
    guess = computer_turn(low, high)
    assert low <= guess <= high

# Testa se a função player_turn retorna um número válido dentro do intervalo
def test_player_turn(monkeypatch):
    # Simula a entrada do usuário
    monkeypatch.setattr('builtins.input', lambda _: '42')  
    result = player_turn("NomeDoJogador")
    assert 1 <= result <= 100

# Teste para a função de exibir suposições dos jogadores
def test_display_guesses():
    # Define os palpites dos jogadores
    player_guesses = [1, 2, 3]
    computer_guesses = [10, 20, 30]
    player_name = "Jogador1"

    # Verifica se a saída contém o nome do jogador e seus palpites
    assert display_guesses(player_name, player_guesses) == f"Suposições do Jogador, {player_name}: {player_guesses}"
    assert display_guesses("Computador", computer_guesses) == f"Suposições do Jogador, Computador: {computer_guesses}"

# Teste para a função check_winner
def test_check_winner():
    # Verifica se a função retorna True quando o palpite é igual ao número secreto
    assert check_winner("NomeDoJogador", 42, 42, [10, 28, 42], 3) == True

    # Verifica se a função retorna False quando o palpite é menor que o número secreto
    assert check_winner("NomeDoJogador", 42, 30, [20, 25, 30], 3) == False

    # Verifica se a função retorna False quando o palpite é maior que o número secreto
    assert check_winner("NomeDoJogador", 42, 50, [45, 48, 50], 5) == False



# Passos para criar testes em py
# Preparação para o teste, ação (função, click...) e afirmação da expectativa (resposta esperada)
