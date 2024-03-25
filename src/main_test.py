"""
Este módulo contém testes para as funções do seu programa principal.
"""
from unittest.mock import patch
from main_module import computer_turn, player_turn, play_again, display_guesses, check_winner

# Testes para função play_again
def test_play_again_yes():
    """
    Testa se a função play_again retorna True quando o usuário insere 's'.
    """
    with patch('builtins.input', return_value='s'): # Simula entrada válida 's'
        assert play_again() is True

def test_play_again_no():
    """
    Testa se a função play_again retorna False quando o usuário insere 'n'.
    """
    with patch('builtins.input', return_value='n'): # Simula entrada válida 'n'
        assert play_again() is False

def test_play_again_invalid_input_then_yes():
    """
    Testa se a função play_again solicita uma entrada válida novamente ao receber um valor inválido
    e retorna True quando o usuário insere 's' após a entrada inválida.
    """
    with patch('builtins.input', side_effect=['x', 's']):
    # Simula entrada inválida 'x' e então entrada válida 's'
        assert play_again() is True

#Teste para função computer_turn
def test_computer_turn():
    """
    Testa a função computer_turn para garantir que o palpite do computador
    esteja dentro do intervalo fornecido.
    """
    low, high = 1, 100
    guess = computer_turn(low, high)
    assert low <= guess <= high

# Teste para função player_turn
def test_player_turn(monkeypatch):
    """
    Testa se a função player_turn retorna um número válido dentro do intervalo
    após simular a entrada do usuário.
    """
    monkeypatch.setattr('builtins.input', lambda _: '42') # Simula a entrada do usuário
    result = player_turn("NomeDoJogador")
    assert 1 <= result <= 100

# Teste para função display_guesses
def test_display_guesses():
    """
    Testa a função display_guesses para verificar se a saída contém o nome do jogador
    e seus palpites.
    """
    player_guesses = [1, 2, 3]
    computer_guesses = [10, 20, 30]
    player_name = "Jogador1"

    assert display_guesses(player_name, player_guesses) == (
        f"Suposições do Jogador, {player_name}: {player_guesses}"
        )
    assert display_guesses("Computador", computer_guesses) == (
        f"Suposições do Jogador, Computador: {computer_guesses}"
        )

# Teste para a função check_winner
def test_check_winner():
    """
    Testa a função check_winner para verificar se retorna True quando o palpite é igual 
    ao número secreto, e False quando o palpite é menor ou maior que o número secreto.
    """
    assert check_winner(player_name="NomeDoJogador", secret_number=42,
                        guess=42, guesses=[10, 28, 42], attempts=3) is True
    assert check_winner(player_name="NomeDoJogador", secret_number=42,
                        guess=30, guesses=[20, 25, 30], attempts=3) is False
    assert check_winner(player_name="NomeDoJogador", secret_number=42,
                        guess=50, guesses=[45, 48, 50], attempts=3) is False



# Passos para criar testes em py
# Preparação para o teste, ação (função, click...) e afirmação da expectativa (resposta esperada)
