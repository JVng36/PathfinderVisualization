import pygame
from node import Node, Node_State
import settings as s


grid_line_color = s.get_grid_line_color()
empty_square_color = s.get_empty_square_color()
start_color = s.get_start_color()
goal_color = s.get_goal_color()
obstacle_color = s.get_obstacle_color()
explored_color = s.get_explored_color()
frontier_color = s.get_frontier_color()
path_color = s.get_path_color()


def create_grid():
    grid_width, grid_height = s.get_grid_size()
    block_size = s.get_block_size()
    grid = [[Node(i, j) for j in range(grid_width // block_size)]
            for i in range(grid_height // block_size)]
    return grid


def draw_grid_lines(surface, grid):
    grid_top_left_x, grid_top_left_y = s.get_grid_top_left_coordinates()
    grid_width, grid_height = s.get_grid_size()
    block_size = s.get_block_size()
    for i in range(len(grid) - 1):
        pygame.draw.line(surface, grid_line_color, (grid_top_left_x, grid_top_left_y +
                         (i+1)*block_size), (grid_top_left_x + grid_width, grid_top_left_y + (i+1)*block_size))
        for j in range(len(grid[i]) - 1):
            pygame.draw.line(surface, grid_line_color, (grid_top_left_x + (j+1) *
                             block_size, grid_top_left_y), (grid_top_left_x + (j+1)*block_size, grid_top_left_y + grid_height))

    pygame.draw.rect(surface, grid_line_color, (grid_top_left_x,
                     grid_top_left_y, grid_width + 1, grid_height + 1), 1)


def draw_window(surface, grid, start_node, goal_node):
    grid_top_left_x, grid_top_left_y = s.get_grid_top_left_coordinates()
    block_size = s.get_block_size()

    surface.fill((0, 0, 0))
    if start_node:
        start_node.state = Node_State.START
    if goal_node:
        goal_node.state = Node_State.GOAL

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            match grid[i][j].state:
                case Node_State.START:
                    pygame.draw.rect(surface, start_color, (grid_top_left_x + j * block_size,
                                     grid_top_left_y + i * block_size, block_size, block_size), 0)
                case Node_State.GOAL:
                    pygame.draw.rect(surface, goal_color, (grid_top_left_x + j * block_size,
                                     grid_top_left_y + i * block_size, block_size, block_size), 0)
                case Node_State.ON_PATH:
                    pygame.draw.rect(surface, path_color, (grid_top_left_x + j * block_size,
                                     grid_top_left_y + i * block_size, block_size, block_size), 0)
                case Node_State.OBSTACLE:
                    pygame.draw.rect(surface, obstacle_color, (grid_top_left_x + j * block_size,
                                     grid_top_left_y + i * block_size, block_size, block_size), 0)
                case Node_State.ON_FRONTIER:
                    pygame.draw.rect(surface, frontier_color, (grid_top_left_x + j * block_size,
                                     grid_top_left_y + i * block_size, block_size, block_size), 0)
                case Node_State.EXPLORED:
                    pygame.draw.rect(surface, explored_color, (grid_top_left_x + j * block_size,
                                     grid_top_left_y + i * block_size, block_size, block_size), 0)
                case Node_State.EMPTY:
                    pygame.draw.rect(surface, empty_square_color, (grid_top_left_x + j *
                                     block_size, grid_top_left_y + i * block_size, block_size, block_size), 0)
    draw_grid_lines(surface, grid)

def count_path_length(step_array):
    path_count = 0
    for step in step_array:
        match step[2]:
            case Node_State.ON_PATH:
                path_count += 1
    return path_count