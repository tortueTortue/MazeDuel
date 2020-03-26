from .maze_producer import Maze

class Match:
    """
    A match represent one duel in one particular maze between
    two shooters which ends either a win of one of the shooters
    or a tie.
    """

    def __init__(self, maze: Maze, players: tuple):
        self.maze = maze
        self.players = players
        self.bullets = None

    def unavailable_move(self, position: Position) -> bool:
        """
        Verify whether a move is legal according to the
        frame of the game and the maze's walls

        params:
            position(Position): position to verify if move
            would be legal or not.

        return:
            bool: whether position is legal or not
        """
        return self.maze.touches(position)