from service.game_service import GameService
from utils.env_variables import display_values, load_environment_variables
from utils.log_utils import initialize_logs

# Initialization
initialize_logs("Webservice")

load_environment_variables()
display_values()


g = GameService().play(3, 5, "coinflip", choice="tails")
print(g)

print(f"{g.player1.username} : new elo -> {g.player1.elo}")
print(f"{g.player2.username} : new elo -> {g.player2.elo}")

g2 = GameService().play(3, 5, "dice")
print(g2)

print(f"{g2.player1.username} : new elo -> {g2.player1.elo}")
print(f"{g2.player2.username} : new elo -> {g2.player2.elo}")


from dao.game_dao import GameDao
from dao.player_dao import PlayerDao
from utils.env_variables import load_environment_variables

load_environment_variables()

# 1. Test de find_by_id
game = GameDao().find_by_id(1)
print("Partie 1 :", game)

# 2. Test de find_all_by_player (pour le joueur avec id_player = 3 par exemple)
games_player3 = GameDao().find_all_by_player(3)
print(f"Nombre de parties pour le joueur 3 : {len(games_player3)}")
for g in games_player3:
    print(g)