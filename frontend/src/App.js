// Componente principal para gerenciar o estado do jogo, placar e integração com o backend.

// import logo from './logo.svg';

import React, { useState, useEffect } from 'react';
import Board from './components/Board';
import Scoreboard from './components/Scoreboard';
import axios from 'axios';
import './App.css';

function App() {
  const [squares, setSquares] = useState(Array(9).fill(''));
  const [turn, setTurn] = useState('X');
  const [score, setScore] = useState({ X: 0, O: 0 });
  const [winner, setWinner] = useState(null);

  // Iniciar o jogo ao carregar
  useEffect(() => {
    iniciarJogo();
  }, []);

  const iniciarJogo = async () => {
    const response = await axios.post('http://localhost:5000/iniciar_jogo');
    setSquares(response.data.tabuleiro);
    setTurn(response.data.turno);
    setScore(response.data.placar);
    setWinner(null);
  };

  const handleSquareClick = async (index) => {
    if (squares[index] !== '' || winner) return;

    const response = await axios.post('http://localhost:5000/fazer_jogada', {
      posicao: index,
      modo: 'pvp', // ou 'ia' dependendo do modo de jogo selecionado
    });

    setSquares(response.data.tabuleiro);
    setTurn(response.data.turno);
    setWinner(response.data.vencedor);
    setScore(response.data.placar);
  };

  return (
    <div className="app">
      <div className="header">
        <button onClick={iniciarJogo}>Reiniciar Jogo</button>
      </div>
      <Scoreboard score={score} />
      <Board squares={squares} onSquareClick={handleSquareClick} />
      {winner && <div className="winner">{winner} venceu!</div>}
    </div>
  );
}

export default App;
