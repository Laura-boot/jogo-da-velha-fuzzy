## Isola a lógica do jogo (funções de verificação de vitória, jogadas da IA, etc.).

import random

# Função para iniciar um novo jogo
def iniciar_jogo():
    tabuleiro = [''] * 9
    turno = 'X'
    return tabuleiro, turno

# Função para fazer uma jogada
def fazer_jogada(tabuleiro, posicao, turno, modo):
    if tabuleiro[posicao] == '':
        tabuleiro[posicao] = turno

        # Verifica se a jogada atual resulta em vitória
        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            return posicao, vencedor

        # Se o modo for contra IA e o próximo turno for da IA
        if modo == 'ia' and turno == 'X':
            posicao_ia = ia_fuzzy(tabuleiro)
            tabuleiro[posicao_ia] = 'O'
            vencedor = verificar_vencedor(tabuleiro)
            return posicao_ia, vencedor

        return posicao, None
    return None, None

# Função para verificar o vencedor
def verificar_vencedor(tabuleiro):
    combinacoes_vitoria = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in combinacoes_vitoria:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] and tabuleiro[a] != '':
            return tabuleiro[a]
    return None

# Função da IA Fuzzy para tomar decisões
def ia_fuzzy(tabuleiro):
    # Priorizar vitória imediata
    for i in range(9):
        if tabuleiro[i] == '':
            tabuleiro[i] = 'O'
            if verificar_vencedor(tabuleiro) == 'O':
                return i
            tabuleiro[i] = ''  # Reverte a jogada

    # Bloquear vitória do adversário
    for i in range(9):
        if tabuleiro[i] == '':
            tabuleiro[i] = 'X'
            if verificar_vencedor(tabuleiro) == 'X':
                tabuleiro[i] = 'O'
                return i
            tabuleiro[i] = ''  # Reverte a jogada

    # Priorizar o centro
    if tabuleiro[4] == '':
        return 4

    # Ocupar cantos
    for i in [0, 2, 6, 8]:
        if tabuleiro[i] == '':
            return i

    # Ocupar laterais
    laterais = [i for i in [1, 3, 5, 7] if tabuleiro[i] == '']
    if laterais:
        return random.choice(laterais)

    return None
