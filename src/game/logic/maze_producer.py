"""
"""

class Maze:
    """
    """
    def __init__(self, thickness: int):
        self.walls = ()
        self.thickness = thickness
        
    def touches(self, position: Position):
        """
        Verify whether the position touches the maze's walls
        or not

        params:
            position(Position): position to verify 

        return:
            bool: whether position is touches wall or not
        """
        for wall in self.walls:
            if wall == position:
                return True
        return False

def producer_maze() -> Maze:
    """
    """
    return None