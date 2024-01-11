from node import Node_State
import settings as s
from queue import PriorityQueue


def breadth_first_search(grid, start_node):
    if not start_node:
        return []

    # Initialize frontier with start_node, frontier uses a FIFO queue
    frontier = [start_node]
    # explored uses a Set for efficiency
    explored = set()

    all_algorithm_steps = []

    def mark_path(node):
        while node.parent is not None:
            if node.state != Node_State.GOAL:
                node.state = Node_State.ON_PATH
                all_algorithm_steps.append(
                    [node.row, node.column, Node_State.ON_PATH])
            node = node.parent
        return

    # while frontier is not empty
    while frontier:
        node = frontier.pop(0)
        explored.add(node)
        node.state = Node_State.EXPLORED
        all_algorithm_steps.append(
            [node.row, node.column, Node_State.EXPLORED])

        # Bounds check if the children of node can be accessed
        above_valid = node.row - 1 >= 0 and node.row - \
            1 < s.get_columns() and not grid[node.row -
                                             1][node.column].state == Node_State.OBSTACLE
        right_valid = node.column + 1 >= 0 and node.column + \
            1 < s.get_columns() and not grid[node.row][node.column +
                                                       1].state == Node_State.OBSTACLE
        below_valid = node.row + 1 >= 0 and node.row + \
            1 < s.get_columns() and not grid[node.row +
                                             1][node.column].state == Node_State.OBSTACLE
        left_valid = node.column - 1 >= 0 and node.column - \
            1 < s.get_columns() and not grid[node.row][node.column -
                                                       1].state == Node_State.OBSTACLE

        # Check if children of node are on the frontier or explored
        if above_valid:
            above = grid[node.row - 1][node.column]
            if above not in frontier and above not in explored:
                above.parent = node
                if above.state == Node_State.GOAL:
                    mark_path(above)
                    return all_algorithm_steps
                else:
                    frontier.append(above)
                    above.state = Node_State.ON_FRONTIER
                    all_algorithm_steps.append(
                        [above.row, above.column, Node_State.ON_FRONTIER])
        if right_valid:
            right = grid[node.row][node.column + 1]
            if right not in frontier and right not in explored:
                right.parent = node
                if right.state == Node_State.GOAL:
                    mark_path(right)
                    return all_algorithm_steps
                else:
                    frontier.append(right)
                    right.state = Node_State.ON_FRONTIER
                    all_algorithm_steps.append(
                        [right.row, right.column, Node_State.ON_FRONTIER])
        if below_valid:
            below = grid[node.row + 1][node.column]
            if below not in frontier and below not in explored:
                below.parent = node
                if below.state == Node_State.GOAL:
                    mark_path(below)
                    return all_algorithm_steps
                else:
                    frontier.append(below)
                    below.state = Node_State.ON_FRONTIER
                    all_algorithm_steps.append(
                        [below.row, below.column, Node_State.ON_FRONTIER])
        if left_valid:
            left = grid[node.row][node.column - 1]
            if left not in frontier and left not in explored:
                left.parent = node
                if left.state == Node_State.GOAL:
                    mark_path(left)
                    return all_algorithm_steps
                else:
                    frontier.append(left)
                    left.state = Node_State.ON_FRONTIER
                    all_algorithm_steps.append(
                        [left.row, left.column, Node_State.ON_FRONTIER])
    return all_algorithm_steps


def depth_first_search(grid, start_node):
    if not start_node:
        return []

    # Initialize frontier with start_node, frontier uses a LIFO stack for DFS
    frontier = [start_node]
    # explored uses a Set for efficiency
    explored = set()

    all_algorithm_steps = []

    def mark_path(node):
        while node.parent is not None:
            if node.state != Node_State.GOAL:
                node.state = Node_State.ON_PATH
                all_algorithm_steps.append(
                    [node.row, node.column, Node_State.ON_PATH])
            node = node.parent
        return

    # while frontier is not empty
    while frontier:
        node = frontier.pop()  # .pop and not .pop(0)
        explored.add(node)

        # Bounds check if the children of node can be accessed
        above_valid = node.row - 1 >= 0 and node.row - \
            1 < s.get_columns() and not grid[node.row -
                                             1][node.column].state == Node_State.OBSTACLE
        right_valid = node.column + 1 >= 0 and node.column + \
            1 < s.get_columns() and not grid[node.row][node.column +
                                                       1].state == Node_State.OBSTACLE
        below_valid = node.row + 1 >= 0 and node.row + \
            1 < s.get_columns() and not grid[node.row +
                                             1][node.column].state == Node_State.OBSTACLE
        left_valid = node.column - 1 >= 0 and node.column - \
            1 < s.get_columns() and not grid[node.row][node.column -
                                                       1].state == Node_State.OBSTACLE

        # Check if children of node are on the frontier or explored
        if above_valid:
            above = grid[node.row - 1][node.column]
            if above not in frontier and above not in explored:
                above.parent = node
                if above.state == Node_State.GOAL:
                    mark_path(above)
                    return all_algorithm_steps
                else:
                    frontier.append(above)
                    above.state = Node_State.ON_FRONTIER
                    all_algorithm_steps.append(
                        [above.row, above.column, Node_State.ON_FRONTIER])
        if right_valid:
            right = grid[node.row][node.column + 1]
            if right not in frontier and right not in explored:
                right.parent = node
                if right.state == Node_State.GOAL:
                    mark_path(right)
                    return all_algorithm_steps
                else:
                    frontier.append(right)
                    right.state = Node_State.ON_FRONTIER
                    all_algorithm_steps.append(
                        [right.row, right.column, Node_State.ON_FRONTIER])
        if below_valid:
            below = grid[node.row + 1][node.column]
            if below not in frontier and below not in explored:
                below.parent = node
                if below.state == Node_State.GOAL:
                    mark_path(below)
                    return all_algorithm_steps
                else:
                    frontier.append(below)
                    below.state = Node_State.ON_FRONTIER
                    all_algorithm_steps.append(
                        [below.row, below.column, Node_State.ON_FRONTIER])
        if left_valid:
            left = grid[node.row][node.column - 1]
            if left not in frontier and left not in explored:
                left.parent = node
                if left.state == Node_State.GOAL:
                    mark_path(left)
                    return all_algorithm_steps
                else:
                    frontier.append(left)
                    left.state = Node_State.ON_FRONTIER
                    all_algorithm_steps.append(
                        [left.row, left.column, Node_State.ON_FRONTIER])
        node.state = Node_State.EXPLORED
        all_algorithm_steps.append(
            [node.row, node.column, Node_State.EXPLORED])
    return all_algorithm_steps


class Grid_Square():
    def __init__(self, row, column):
        self.is_start = False
        self.is_goal = False
        self.is_obstacle = False
        self.color = s.get_empty_square_color()
        self.adjacent = []
        self.row = row
        self.col = column
        self.row_total = s.get_columns()

    def get_pos(self):
        return self.row, self.col

    def is_explored(self):
        return self.color == s.get_explored_color()

    def is_exploring(self):
        return self.color == s.get_frontier_color()

    def is_path(self):
        return self.color == s.get_path_color()

    def set_explored(self):
        self.color = s.get_explored_color()

    def set_exploring(self):
        self.color = s.get_frontier_color()

    def set_path(self):
        self.color = s.get_path_color()

    def update_adjacent(self, grid):
        self.adjacent = []
        if self.row < self.row_total - 1 and not grid[self.row + 1][self.col].is_obstacle: # Checks to see if adjacent isn't end row or obstacle when going down
            self.adjacent.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_obstacle: # Checks to see if adjacent isn't end row or obstacle when going up
            self.adjacent.append(grid[self.row - 1][self.col])

        if self.col < self.row_total - 1 and not grid[self.row][self.col + 1].is_obstacle: # Checks to see if adjacent isn't end col or obstacle when going right
            self.adjacent.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_obstacle: # Checks to see if adjacent isn't end col or obstacle when going left
            self.adjacent.append(grid[self.row][self.col - 1])

# Euclidean distance, not ideal for a 2D grid without diagonal moves
# def heuristic(point1, point2):
#     return math.sqrt((point1[0] - point2[0])**2 + abs(point1[1] - point2[1])**2)

# Here is Manhatten distance instead
def heuristic(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def convert_node_grid_to_grid_square_grid(node_grid):

    grid_height = len(node_grid)
    grid_width = len(node_grid[0])
    
    grid_square_grid =[[Grid_Square(i, j) for j in range(grid_width)]
            for i in range(grid_height)]
    
    for i in range(grid_height):
        for j in range(grid_width):
            match node_grid[i][j].state:
                case Node_State.START:
                    grid_square_grid[i][j].is_start = True
                    start = grid_square_grid[i][j]
                case Node_State.GOAL:
                    grid_square_grid[i][j].is_goal = True
                    end = grid_square_grid[i][j]
                case Node_State.ON_PATH:
                    grid_square_grid[i][j].set_path()
                case Node_State.OBSTACLE:
                    grid_square_grid[i][j].is_obstacle = True
                case Node_State.ON_FRONTIER:
                    grid_square_grid[i][j].set_exploring()
                case Node_State.EXPLORED:
                    grid_square_grid[i][j].is_explored()
                case Node_State.EMPTY:
                    grid_square_grid[i][j].color = s.get_empty_square_color

    for i in range(grid_height):
        for j in range(grid_width):
            grid_square_grid[i][j].update_adjacent(grid_square_grid)
                    
    return grid_square_grid, start, end

def print_grid_square(grid_square):
    print(f"is_start = {grid_square.is_start}")
    print(f"is_goal = {grid_square.is_goal}")
    print(f"is_obstacle = {grid_square.is_obstacle}")
    print(f"color = {grid_square.color}")
    print(f"adjacent = {grid_square.adjacent}")
    print(f"row = {grid_square.row}")
    print(f"col = {grid_square.col}")
    print(f"row_total = {grid_square.row_total}")


def dijkstra(grid, start, end):

    all_algorithm_steps = []

    def create_path(previous_node, current):
        while current in previous_node:
            current = previous_node[current]
            current.set_path()
            all_algorithm_steps.append([current.row, current.col, Node_State.ON_PATH])

    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    previous_node = {}
    g_score = {square: float("inf") for row in grid for square in row}
    g_score[start] = 0
    f_score = {square: float("inf") for row in grid for square in row}
    # set heuristic to zero for Dijkstra's
    f_score[start] = 0 # heuristic(start.get_pos(), end.get_pos())

    open_set_dict = {start}

    while not open_set.empty():

        current = open_set.get()[2]
        open_set_dict.remove(current)

        if current == end:
            create_path(previous_node, end)
            end.is_goal = True
            return all_algorithm_steps

        for adjacent in current.adjacent:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[adjacent]:
                previous_node[adjacent] = current
                g_score[adjacent] = temp_g_score
                # set heuristic to zero for Dijkstra's
                f_score[adjacent] = temp_g_score # + heuristic(adjacent.get_pos(), end.get_pos())
                if adjacent not in open_set_dict:
                    count += 1
                    open_set.put((f_score[adjacent], count, adjacent))
                    open_set_dict.add(adjacent)
                    adjacent.set_exploring()
                    all_algorithm_steps.append([adjacent.row, adjacent.col, Node_State.ON_FRONTIER])
        if current != start:
            current.set_explored()
            all_algorithm_steps.append([current.row, current.col, Node_State.EXPLORED])
    return all_algorithm_steps

def astar(grid, start, end):
    if not start:
        return []

    all_algorithm_steps = []

    def create_path(previous_node, current):
        while current in previous_node:
            current = previous_node[current]
            current.set_path()
            all_algorithm_steps.append([current.row, current.col, Node_State.ON_PATH])

    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    previous_node = {}
    g_score = {square: float("inf") for row in grid for square in row}
    g_score[start] = 0
    f_score = {square: float("inf") for row in grid for square in row}
    f_score[start] = heuristic(start.get_pos(), end.get_pos())

    open_set_dict = {start}

    while not open_set.empty():

        current = open_set.get()[2]
        open_set_dict.remove(current)

        if current == end:
            create_path(previous_node, end)
            end.is_goal = True
            return all_algorithm_steps

        for adjacent in current.adjacent:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[adjacent]:
                previous_node[adjacent] = current
                g_score[adjacent] = temp_g_score
                f_score[adjacent] = temp_g_score + heuristic(adjacent.get_pos(), end.get_pos())
                if adjacent not in open_set_dict:
                    count += 1
                    open_set.put((f_score[adjacent], count, adjacent))
                    open_set_dict.add(adjacent)
                    adjacent.set_exploring()
                    all_algorithm_steps.append([adjacent.row, adjacent.col, Node_State.ON_FRONTIER])
        if current != start:
            current.set_explored()
            all_algorithm_steps.append([current.row, current.col, Node_State.EXPLORED])
    return all_algorithm_steps

