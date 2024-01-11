from enum import Enum, auto


class Node_State(Enum):
    EMPTY = auto()
    START = auto()
    GOAL = auto()
    OBSTACLE = auto()
    ON_FRONTIER = auto()
    ON_PATH = auto()
    EXPLORED = auto()


class Node:
    def __init__(self, row=-1, column=-1):
        self.parent = None
        self.row = row
        self.column = column
        self.state = Node_State.EMPTY
