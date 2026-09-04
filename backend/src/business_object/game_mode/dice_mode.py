import secrets

from business_object.game import Game
from business_object.game_mode.game_mode import GameMode


class DiceMode(GameMode):

    def play(self, p1, p2):
        d1 = secrets.choice(range(1, 7))
        d2 = secrets.choice(range(1, 7))

        if d1 > d2:
            winner = p1
        elif d1 < d2:
            winner = p2
        else:
            winner = None

        description = f"{p1.username} rolled {d1}, {p2.username} rolled {d2}"

        return Game(
            p1,
            p2,
            "dice",
            winner,
            description,
            None,
        )
