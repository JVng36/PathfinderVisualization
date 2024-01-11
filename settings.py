
# Initial Settings

_window_width = 840
_window_height = 980
_grid_width = 800
_grid_height = 800
_columns = 20
_block_size = _grid_width // _columns

_grid_top_left_x = (_window_width - _grid_width) // 2
_grid_top_left_y = ((_window_height - _grid_height) // 2) - 20

# Node state colors

_grid_line_color = (0, 0, 0)
_empty_square_color = (255, 255, 255)
_start_color = (128, 255, 128)
_goal_color = (255, 128, 128)
_obstacle_color = (0, 76, 76)
_explored_color = (178, 216, 216)
_frontier_color = (102, 178, 178)
_path_color = (198, 173, 255)

# Setters and Getters


def set_window_size(width, height):
    global _window_width, _window_height
    _window_width = width
    _window_height = height


def get_window_size():
    return _window_width, _window_height


def set_grid_size(width, height):
    global _grid_width, _grid_height
    _grid_width = width
    _grid_height = height
    update_block_size()


def get_grid_size():
    return _grid_width, _grid_height


def set_columns(number_of_columns):
    global _columns
    _columns = number_of_columns
    update_block_size()


def get_columns():
    return _columns


def update_block_size():
    global _block_size
    _block_size = _grid_width // _columns


def get_block_size():
    return _block_size


def set_grid_line_color(color):
    global _grid_line_color
    _grid_line_color = color


def get_grid_line_color():
    return _grid_line_color


def set_empty_square_color(color):
    global _empty_square_color
    _empty_square_color = color


def get_empty_square_color():
    return _empty_square_color


def set_start_color(color):
    global _start_color
    _start_color = color


def get_start_color():
    return _start_color


def set_goal_color(color):
    global _goal_color
    _goal_color = color


def get_goal_color():
    return _goal_color


def set_obstacle_color(color):
    global _obstacle_color
    _obstacle_color = color


def get_obstacle_color():
    return _obstacle_color


def set_explored_color(color):
    global _explored_color
    _explored_color = color


def get_explored_color():
    return _explored_color


def set_frontier_color(color):
    global _frontier_color
    _frontier_color = color


def get_frontier_color():
    return _frontier_color


def set_path_color(color):
    global _path_color
    _path_color = color


def get_path_color():
    return _path_color


def update_grid_top_left_coordinates():
    global _grid_top_left_x, _grid_top_left_y
    _grid_top_left_x = (_window_width - _grid_width) // 2
    _grid_top_left_y = ((_window_height - _grid_height) // 2) - 20


def get_grid_top_left_coordinates():
    return _grid_top_left_x, _grid_top_left_y
