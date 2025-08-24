import random
import os
import time

class TicTacToe:
    def __init__(self):
        """
        Inicializa o jogo, criando um tabuleiro vazio e definindo o estado como não finalizado.
        """
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done = "" # "" = jogo a decorrer, "X" = X venceu, "O" = O venceu, "D" = Empate

    def print_board(self):
        """
        Limpa o ecrã e imprime o estado atual do tabuleiro de forma legível.
        """
        # Limpa o terminal. 'cls' para Windows, 'clear' para macOS/Linux.
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n--- JOGO DA VELHA ---")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])
        print("")

    def reset(self):
        """
        Reseta o tabuleiro e o estado do jogo para uma nova partida.
        """
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done = ""

    def check_win_or_draw(self):
        """
        Verifica se houve vitória ou empate.
        Esta função foi reescrita para corrigir a lógica.
        """
        for player in ["X", "O"]:
            # Combinações de vitória
            win_conditions = [
                # Horizontais
                self.board[0][0] == self.board[0][1] == self.board[0][2] == player,
                self.board[1][0] == self.board[1][1] == self.board[1][2] == player,
                self.board[2][0] == self.board[2][1] == self.board[2][2] == player,
                # Verticais
                self.board[0][0] == self.board[1][0] == self.board[2][0] == player,
                self.board[0][1] == self.board[1][1] == self.board[2][1] == player,
                self.board[0][2] == self.board[1][2] == self.board[2][2] == player,
                # Diagonais
                self.board[0][0] == self.board[1][1] == self.board[2][2] == player,
                self.board[0][2] == self.board[1][1] == self.board[2][0] == player,
            ]
            # Se qualquer uma das condições for verdadeira, o jogador venceu
            if any(win_conditions):
                self.done = player
                return

        # Verificação de empate (corrigida)
        # Se não houve vencedor e não há mais espaços vazios, é um empate.
        empty_spaces = sum(row.count(" ") for row in self.board)
        if empty_spaces == 0 and self.done == "":
            self.done = "D" # "D" para Draw (Empate)

    def get_player_move(self):
        """
        Obtém e valida a jogada do jogador.
        """
        while True:
            try:
                # Pede as coordenadas numa única linha para ser mais rápido
                move = input("Digite sua jogada (linha coluna, ex: 1 2): ")
                x, y = map(int, move.split())

                if 0 <= x <= 2 and 0 <= y <= 2:
                    if self.board[x][y] == " ":
                        self.board[x][y] = "X"
                        break # Sai do loop se a jogada for válida
                    else:
                        print("\nPosição já ocupada. Tente novamente.")
                else:
                    print("\nCoordenadas inválidas. Use números de 0 a 2. Tente novamente.")
            except ValueError:
                print("\nEntrada inválida. Por favor, digite dois números separados por um espaço.")
            except Exception as e:
                print(f"\nOcorreu um erro: {e}")

    def make_computer_move(self):
        """
        Gera uma jogada aleatória para o computador em uma posição vazia.
        """
        # Cria uma lista de todas as posições vazias
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    possible_moves.append((i, j))
        
        # Escolhe uma jogada aleatória se houver movimentos possíveis
        if possible_moves:
            x, y = random.choice(possible_moves)
            self.board[x][y] = "O"
            print(f"O computador jogou na posição ({x}, {y})")
            time.sleep(1) # Pequena pausa para o jogador ver a jogada do computador

# --- LOOP PRINCIPAL DO JOGO ---

# Cria uma instância do jogo
game = TicTacToe()
play_again = True

while play_again:
    # O jogo decorre enquanto o estado 'done' estiver vazio
    while game.done == "":
        game.print_board()
        
        # Vez do jogador
        game.get_player_move()
        
        # Verifica se o jogador ganhou ou se empatou
        game.check_win_or_draw()
        if game.done != "":
            break # Se o jogo terminou, sai do loop

        game.print_board()
        print("Vez do computador...")
        time.sleep(1)
        
        # Vez do computador
        game.make_computer_move()

        # Verifica se o computador ganhou ou se empatou
        game.check_win_or_draw()

    # Mostra o tabuleiro final e o resultado
    game.print_board()
    if game.done == "X":
        print("Parabéns, você venceu!")
    elif game.done == "O":
        print("O computador venceu!")
    elif game.done == "D":
        print("O jogo terminou em empate!")

    # Pergunta se quer jogar novamente
    while True:
        answer = input("\nDeseja jogar novamente? (s/n): ").lower()
        if answer in ["s", "n"]:
            if answer == "s":
                game.reset() # Reseta o jogo para uma nova partida
            else:
                play_again = False
            break
        else:
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

print("\nObrigado por jogar!")
