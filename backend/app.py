## Contém a lógica principal do servidor Flask e as rotas RESTful.

from flask import Flask, jsonify, request
from game_logic import iniciar_jogo, fazer_jogada, verificar_vencedor

app = Flask(__name__)

# Estado do jogo
estado_jogo = {
    "tabuleiro": [],
    "turno": "X",
    "placar": {"X": 0, "O": 0}
}

@app.route('/iniciar_jogo', methods=['POST'])
def iniciar_jogo_route():
    global estado_jogo
    estado_jogo["tabuleiro"], estado_jogo["turno"] = iniciar_jogo()
    return jsonify(estado_jogo)

@app.route('/fazer_jogada', methods=['POST'])
def fazer_jogada_route():
    dados = request.get_json()
    posicao = dados['posicao']
    modo = dados.get('modo', 'pvp')  # modo pode ser 'pvp' ou 'ia'

    # Executa a jogada e atualiza o estado do tabuleiro
    nova_posicao, vencedor = fazer_jogada(estado_jogo["tabuleiro"], posicao, estado_jogo["turno"], modo)
    estado_jogo["turno"] = "O" if estado_jogo["turno"] == "X" else "X"

    # Atualiza o placar se houver um vencedor
    if vencedor:
        estado_jogo["placar"][vencedor] += 1

    return jsonify({
        "tabuleiro": estado_jogo["tabuleiro"],
        "turno": estado_jogo["turno"],
        "vencedor": vencedor,
        "placar": estado_jogo["placar"]
    })

@app.route('/verificar_vencedor', methods=['GET'])
def verificar_vencedor_route():
    vencedor = verificar_vencedor(estado_jogo["tabuleiro"])
    return jsonify({"vencedor": vencedor})

if __name__ == '__main__':
    app.run(debug=True)
