import secrets

from business_object.game import Game
from business_object.game_mode.game_mode import GameMode


class CoinFlipMode(GameMode):

    def play(self, p1, p2, choice):
        result = secrets.choice(["heads", "tails"])

        winner = p1 if result == choice else p2

        description = f"Coin flip result: {result}"

        return Game(
            p1,
            p2,
            "coinflip",
            winner,
            description,
            None,
        )
