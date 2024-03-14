from main import computer_turn, player_turn, play_again, display_guesses, check_winner

#Testa se a função jogar novamente retorna True quando o usuário insere 's'
def test_play_again_yes():
  assert play_again("s") == True
#Testa se a função jogar novamente retorna False quando o usuário insere 'n'
def test_play_again_no():
  assert play_again("n") == False

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

#Teste para a função check_winner
def test_check_winner():
#Testa se a função retorna True quando o palpite é igual ao número secreto
  assert check_winner("Jogador1", 42, 42, [1, 2, 3]) == True
#Testa se a função retorna False quando o palpite não é igual ao número secreto
  assert check_winner("Jogador1", 42, 41, [1, 2, 3]) == False



# Passos para criar testes em py
# Preparação para o teste, ação (função, click...) e afirmação da expectativa (resposta esperada)
