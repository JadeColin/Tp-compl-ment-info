from datetime import datetime

from business_object.player import Player


class Game:
    """
    Class representing a Game.
    Attributes:
        id_game (int): The unique identifier for the game.
        player1 (Player): The first player.
        player2 (Player): The second player.
        game_mode (str): The game mode.
        winner (Player): The winner of the game.
        description (str): A description of the game.
        timestamp (datetime): The date and time of the game.
    """

    def __init__(
        self,
        player1,
        player2,
        game_mode,
        winner,
        description,
        timestamp,
    ):
        """Constructor"""
        self.id_game = None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp

    def __str__(self):
        winner = self.winner.username if self.winner else "Draw"
        return (
            f"{self.game_mode} between {self.player1.username} "
        f"and {self.player2.username}. Winner: {winner}"
        )

