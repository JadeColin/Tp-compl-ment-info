-----------------------------------------------------
-- Player
-----------------------------------------------------
DROP TABLE IF EXISTS player CASCADE;
CREATE TABLE player (
    id_player    SERIAL PRIMARY KEY,
    username     VARCHAR(30) UNIQUE,
    password     VARCHAR(256),
    elo          INTEGER,
    email        VARCHAR(50),
    pokemon_fan  BOOLEAN,
    access_token VARCHAR(255)
);


DROP TABLE IF EXISTS project.game;

CREATE TABLE project.game (
    id_game      SERIAL PRIMARY KEY,
    id_player1   INTEGER REFERENCES player(id_player),
    id_player2   INTEGER REFERENCES player(id_player),
    game_mode    VARCHAR(20),
    id_winner    INTEGER REFERENCES player(id_player),
    detail       VARCHAR(100),
    timestamp    TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

INSERT INTO project.game(id_player1, id_player2, game_mode, id_winner, detail) VALUES
(1, 2, 'coinflip', 1, 'Gilbert chose heads, result was heads'),
(3, 4, 'dice',     3, 'Maurice rolled 5, Batricia rolled 2'),
(3, 4, 'dice',     null, 'Maurice rolled 4, Batricia rolled 4'),
(4, 3, 'dice',     4, 'Batricia rolled 2, Maurice rolled 1'),
(3, 4, 'coinflip', 4, 'Maurice chose heads, result was tails');