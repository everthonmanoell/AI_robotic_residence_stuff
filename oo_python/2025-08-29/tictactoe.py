# -*- coding: utf-8 -*-
from random import choice

# --- Constantes do Jogo ---
BOARD_MAP = {
    1: (2, 0),
    2: (2, 1),
    3: (2, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (0, 0),
    8: (0, 1),
    9: (0, 2),
}

WINNING_COMBINATIONS = [
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
]

SAMPLE_BOARD = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
]

MARKS = [" ", "X", "O"]

# --- Variáveis globais ---
board = None
player_moves = None
available_moves = None
round_count = None
current_player = None


# --- Inicializa jogo ---
def initialize_game():
    global board, player_moves, available_moves, round_count, current_player

    board = [[" " for _ in range(3)] for _ in range(3)]
    player_moves = {1: [], 2: []}
    available_moves = BOARD_MAP.copy()
    round_count = 1
    current_player = 1  # Jogador 1 começa

    while True:
        robot_color_input = int(
            input("Qual a cor das peças que o robô jogará? [0] vermelho, [1] verde: ")
        )
        if robot_color_input == 0:
            robot_color = "red"
            break
        elif robot_color_input == 1:
            robot_color = "green"
            break
        else:
            print("Entrada inválida! Digite 0 ou 1.")

    return robot_color, board


# --- Imprime tabuleiro ---
def print_board(current_board):
    print(
        " {} | {} | {} ".format(
            current_board[0][0], current_board[0][1], current_board[0][2]
        )
    )
    print("---+---+---")
    print(
        " {} | {} | {} ".format(
            current_board[1][0], current_board[1][1], current_board[1][2]
        )
    )
    print("---+---+---")
    print(
        " {} | {} | {} ".format(
            current_board[2][0], current_board[2][1], current_board[2][2]
        )
    )


# --- Alterna jogador ---
def next_player():
    global round_count, current_player
    round_count += 1
    current_player = 2 if current_player == 1 else 1


# --- Mapeia coordenadas para chave ---
def get_move_key(move_coords):
    for key, value in BOARD_MAP.items():
        if value == move_coords:
            return key
    return None


# --- Registra jogada ---
def register_play(move_coords):
    global player_moves, available_moves
    player_moves[current_player].append(move_coords)
    key = get_move_key(move_coords)
    if key in available_moves:
        available_moves.pop(key)


# --- Jogada do jogador ---
def get_player_move(board):
    player_mark = MARKS[current_player]
    new_board = [row[:] for row in board]
    try:
        play = int(input("Digite sua jogada (1-9): "))
        if play not in BOARD_MAP:
            raise ValueError
        i, j = BOARD_MAP[play]
        if new_board[i][j] != " ":
            print("Posição já ocupada!")
            return (False, board, None)
        new_board[i][j] = player_mark
        return (True, new_board, (i, j))
    except (ValueError, KeyError):
        print("Jogada inválida. Digite um número de 1 a 9.")
        return (False, board, None)


# --- Verifica vencedor ---
def check_for_winner():
    last_player = 1 if current_player == 1 else 2
    for combination in WINNING_COMBINATIONS:
        if all(pos in player_moves[last_player] for pos in combination):
            return last_player
    return 0


# --- Minimax para robô invencível ---
def check_for_winner_state(moves_state):

    """
    moves_state: um dicionário com as jogadas de cada jogador
    Retorna:
        1 se o jogador humano venceu
        2 se o robô venceu
        0 se ninguém venceu ainda
    """

    # Verifica cada jogador
    for player in [1, 2]:
        # Verifica cada combinação possível de vitória
        for combo in WINNING_COMBINATIONS:
            # Se todas as posições da combinação estão nas jogadas do jogador
            if all(pos in moves_state[player] for pos in combo):
                return player  # Retorna o vencedor
    return 0  # Ninguém venceu


def minimax(board_state, moves_state, avail_moves_state, depth, is_maximizing):

    """
    board_state: o tabuleiro atual
    moves_state: lista de jogadas de cada jogador
    avail_moves_state: jogadas ainda disponíveis
    depth: quantas jogadas à frente estamos simulando
    is_maximizing: True se for a vez do robô (quer maximizar pontuação)
                   False se for a vez do jogador (quer minimizar pontuação do robô)
    """

    # Verifica se alguém já venceu neste cenário
    winner = check_for_winner_state(moves_state)
    if winner == 2:  # Robô venceu
        return 10 - depth  # Quanto mais cedo vencer, melhor (score alto)
    elif winner == 1:  # player venceu
        return depth - 10  # Quanto mais cedo perder, pior (score baixo)
    elif not avail_moves_state:  # Não tem mais jogadas (empate)
        return 0  # Empate = score neutro

    # Se o jogo ainda não terminou, simulamos jogadas futuras
    if is_maximizing:  # Vez do robô
        best_score = -float("inf")  # Começamos com o pior score possível
        # Testa todas as jogadas disponíveis
        for key, (i, j) in list(avail_moves_state.items()):
            # Marca temporariamente a jogada do robô
            board_state[i][j] = MARKS[2]
            moves_state[2].append((i, j))
            removed = avail_moves_state.pop(key)

            # agora é a vez vez do usuario
            score = minimax(board_state, moves_state, avail_moves_state, depth + 1, False)

            # Desfaz a jogada para testar outra possibilidade 
            board_state[i][j] = " "
            moves_state[2].remove((i, j))
            avail_moves_state[key] = removed
             # Mantém o maior score do robo
            best_score = max(best_score, score)
        return best_score
    else: # vez do usuario
        best_score = float("inf") # Começamos com o pior score para o jogador
        for key, (i, j) in list(avail_moves_state.items()):
            # Marca temporariamente a jogada do jogador
            board_state[i][j] = MARKS[1]
            moves_state[1].append((i, j))
            removed = avail_moves_state.pop(key)
            #agora é a vez do robô
            score = minimax(
                board_state, moves_state, avail_moves_state, depth + 1, True
            )

            # Desfaz a jogada para testar outra possibilidade
            board_state[i][j] = " "
            moves_state[1].remove((i, j))
            avail_moves_state[key] = removed
            # Assume que o jogador vai escolher a jogada que piora o score do robô
            best_score = min(best_score, score)
        return best_score


# --- Função que escolhe a melhor jogada do robô usando Minimax ---
def get_robot_move(board):

    """
    board: tabuleiro atual
    Retorna:
        True/False (se conseguiu jogar)
        novo tabuleiro após a jogada do robô
        coordenadas da jogada feita pelo robô
    """

    best_score = -float("inf") # Melhor pontuação inicial
    best_move = None
        # Cria cópias para simular sem alterar o tabuleiro real
    new_board = [row[:] for row in board]
    moves_state = {1: player_moves[1][:], 2: player_moves[2][:]}
    avail_moves_state = available_moves.copy()

    # Testa todas as jogadas possíveis
    for key, (i, j) in list(avail_moves_state.items()):
        new_board[i][j] = MARKS[2] # Faz jogada temporária do robô
        moves_state[2].append((i, j))
        removed = avail_moves_state.pop(key)

        # Calcula o score da jogada usando Minimax
        score = minimax(new_board, moves_state, avail_moves_state, 0, False)
         # Desfaz a jogada temporária
        new_board[i][j] = " "
        moves_state[2].remove((i, j))
        avail_moves_state[key] = removed
        # Guarda a jogada que deu o melhor score
        if score > best_score:
            best_score = score
            best_move = (i, j, key)

    # Executa a melhor jogada no tabuleiro real
    if best_move:
        i, j, _ = best_move
        final_board = [row[:] for row in board]
        final_board[i][j] = MARKS[2]
        return (True, final_board, (i, j))

    # fallback 2
    return (False, board, None)
