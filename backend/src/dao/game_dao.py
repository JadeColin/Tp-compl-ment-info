from business_object.game import Game
from dao.db_connection import DBConnection
from dao.player_dao import PlayerDao
from utils.log_utils import get_logger, log
from utils.singleton import Singleton

logger = get_logger(__name__)


class GameDao(metaclass=Singleton):
    """Class containing methods to access Games in the database."""

    @log
    def create(self, game: Game) -> bool:
        """Create a game in the database.

        Args:
            game (Game): Game to create
        Returns:
            bool: True if creation is successful, False otherwise
        """
        res = None

        # Récupération des IDs des joueurs ou du gagnant s'ils sont des objets Player
        id_player1 = game.player1.id_player if getattr(game, "player1", None) else getattr(game, "id_player1", None)
        id_player2 = game.player2.id_player if getattr(game, "player2", None) else getattr(game, "id_player2", None)
        id_winner = game.winner.id_player if getattr(game, "winner", None) else getattr(game, "id_winner", None)

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO game(id_player1, id_player2, game_mode, id_winner, detail) VALUES "
                        "(%(id_player1)s, %(id_player2)s, %(game_mode)s, %(id_winner)s, %(detail)s) "
                        "RETURNING id_game;",
                        {
                            "id_player1": id_player1,
                            "id_player2": id_player2,
                            "game_mode": game.game_mode,
                            "id_winner": id_winner,
                            "detail": game.detail,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        created = False
        if res:
            game.id_game = res["id_game"]
            created = True

        return created

    @log
    def find_by_id(self, id_game: int) -> Game:
        """Find a game by its id.

        Args:
            id_game (int): The ID of the game to find
        Returns:
            Game: Game matching the given id, or None
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * "
                        "  FROM game "
                        " WHERE id_game = %(id_game)s; ",
                        {"id_game": id_game},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        game = None
        if res:
            # Étape 1 : Convertir les IDs en vrais objets Player
            p1 = PlayerDao().find_by_id(res["id_player1"])
            p2 = PlayerDao().find_by_id(res["id_player2"])
            winner = PlayerDao().find_by_id(res["id_winner"]) if res["id_winner"] else None

            # Étape 2 : Instancier et retourner l'objet Game
            game = Game(
                id_game=res["id_game"],
                game_mode=res["game_mode"],
                player1=p1,
                player2=p2,
                winner=winner,
                detail=res["detail"],
            )

        return game

    @log
    def find_all_by_player(self, id_player: int) -> list[Game]:
        """Find all games involving a specific player (as player1 or player2).

        Args:
            id_player (int): The ID of the player to search games for
        Returns:
            list[Game]: List of games matching the given player ID
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * "
                        "  FROM game "
                        " WHERE id_player1 = %(id_player)s "
                        "    OR id_player2 = %(id_player)s; ",
                        {"id_player": id_player},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logger.error(e)
            raise

        games_list = []
        if res:
            for row in res:
                # Étape 1 : Convertir les IDs en objets Player
                p1 = PlayerDao().find_by_id(row["id_player1"])
                p2 = PlayerDao().find_by_id(row["id_player2"])
                winner = PlayerDao().find_by_id(row["id_winner"]) if row["id_winner"] else None

                # Étape 2 : Instancier l'objet Game et l'ajouter à la liste
                game = Game(
                    id_game=row["id_game"],
                    game_mode=row["game_mode"],
                    player1=p1,
                    player2=p2,
                    winner=winner,
                    detail=row["detail"],
                )
                games_list.append(game)

        return games_list