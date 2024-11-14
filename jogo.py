import random

# Tabela do jogo
tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Função para imprimir o tabuleiro
def imprimir_tabuleiro():
    print(f'{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
    print('---------')
    print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
    print('---------')
    print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}')

# Função para verificar vitória
def verificar_vitoria(jogador):
    vitória = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for combo in vitória:
        if tabuleiro[combo[0]] == tabuleiro[combo[1]] == tabuleiro[combo[2]] == jogador:
            return True
    return False

# IA Fuzzy aprimorada
def ia_fuzzy():
    # 1. Priorizar vitória imediata
    for i in range(9):
        if tabuleiro[i] not in ['X', 'O']:
            tabuleiro[i] = 'O'
            if verificar_vitoria('O'):
                return i
            tabuleiro[i] = str(i+1)  # Reverte a jogada

    # 2. Bloquear vitória do adversário
    for i in range(9):
        if tabuleiro[i] not in ['X', 'O']:
            tabuleiro[i] = 'X'
            if verificar_vitoria('X'):
                tabuleiro[i] = 'O'
                return i
            tabuleiro[i] = str(i+1)  # Reverte a jogada

    # 3. Priorizar o centro se estiver disponível
    if tabuleiro[4] == '5':
        return 4

    # 4. Ocupar cantos se disponíveis
    for i in [0, 2, 6, 8]:
        if tabuleiro[i] not in ['X', 'O']:
            return i

    # 5. Ocupar laterais aleatoriamente
    laterais = [i for i in [1, 3, 5, 7] if tabuleiro[i] not in ['X', 'O']]
    if laterais:
        return random.choice(laterais)
    
    # Se nenhuma jogada for possível, retorna None
    return None

# Escolha do modo de jogo
modo = input("Escolha o modo de jogo (1 - Contra IA, 2 - Contra outro jogador): ")

# Jogabilidade
jogador_atual = 'X'
while True:
    imprimir_tabuleiro()
    
    if modo == '1':  # Modo contra IA
        if jogador_atual == 'X':
            jogada = input("Sua jogada (1-9): ")
            tabuleiro[int(jogada) - 1] = 'X'
            if verificar_vitoria('X'):
                imprimir_tabuleiro()
                print("Você ganhou!")
                break
            jogador_atual = 'O'
        else:
            jogada_ia = ia_fuzzy()
            if jogada_ia is None:
                imprimir_tabuleiro()
                print("O jogo deu velha!")
                break
            tabuleiro[jogada_ia] = 'O'
            if verificar_vitoria('O'):
                imprimir_tabuleiro()
                print("IA ganhou!")
                break
            jogador_atual = 'X'
    
    elif modo == '2':  # Modo contra outro jogador
        jogada = input(f"Jogador {jogador_atual}, sua jogada (1-9): ")
        tabuleiro[int(jogada) - 1] = jogador_atual
        if verificar_vitoria(jogador_atual):
            imprimir_tabuleiro()
            print(f"Jogador {jogador_atual} ganhou!")
            break
        # Alterna entre 'X' e 'O'
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

    # Verifica se deu velha (tabuleiro cheio sem vitória)
    if all(spot in ['X', 'O'] for spot in tabuleiro):
        imprimir_tabuleiro()
        print("O jogo deu velha!")
        break
