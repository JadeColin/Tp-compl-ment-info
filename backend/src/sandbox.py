from datetime import datetime

from business_object.game import Game
from business_object.player import Player

p1 = Player("Jacky", 1000, "jacky@email.com")
p2 = Player("Jackie", 1000, "jackie@email.com")

g = Game(
    p1,
    p2,
    "coinflip",
    p2,
    "Jackie won the coin flip",
    datetime.now(),
)

print(g)