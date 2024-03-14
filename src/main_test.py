from main import computer_turn, player_turn

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


# Passos para criar testes em py
# Preparação para o teste, ação (função, click...) e afirmação da expectativa (resposta esperada)
