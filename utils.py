import settings as s


def generate_grid_line_points(start_point, end_point):
    """
    Generate a list of points (x, y) on a grid through which a line between two given points would pass.

    Uses Bresenham's line algorithm for rasterization of lines on a discrete grid.

    Args:
    start_point (tuple): The starting point (x, y) of the line.
    end_point (tuple): The ending point (x, y) of the line.

    Returns:
    list: A list of tuples representing points on the grid through which the line passes.
    """

    line_points = []
    start_x, start_y = start_point
    end_x, end_y = end_point

    # Calculate the differences and steps
    delta_x = abs(end_x - start_x)
    delta_y = -abs(end_y - start_y)
    step_x = 1 if start_x < end_x else -1
    step_y = 1 if start_y < end_y else -1
    error = delta_x + delta_y  # Initialize error value

    # Generating points using Bresenham's algorithm
    while True:
        line_points.append((start_x, start_y))
        if start_x == end_x and start_y == end_y:
            break
        error_double = 2 * error
        if error_double >= delta_y:
            error += delta_y
            start_x += step_x
        if error_double <= delta_x:
            error += delta_x
            start_y += step_y

    return line_points


def screen_to_grid(pos):
    grid_top_left_x, grid_top_left_y = s.get_grid_top_left_coordinates()
    block_size = s.get_block_size()
    grid_x = (pos[0] - grid_top_left_x) // block_size
    grid_y = (pos[1] - grid_top_left_y) // block_size
    return grid_x, grid_y
