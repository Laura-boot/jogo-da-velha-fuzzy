import React from 'react';

function Scoreboard({ score }) {
    return (
        <div className="scoreboard">
        <div>X: {score.X}</div>
        <div>O: {score.O}</div>
        </div>
    );
}

export default Scoreboard;
