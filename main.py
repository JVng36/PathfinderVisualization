import pygame
import pygame_gui
import settings as s
from node import Node_State
from grid import create_grid, draw_window, count_path_length
from pathfinding_algorithms import breadth_first_search, depth_first_search, astar, dijkstra, convert_node_grid_to_grid_square_grid
from utils import screen_to_grid, generate_grid_line_points
import time
import random
from enum import Enum, auto
import copy

# Global variables
draw_on = False
erase_on = False
choose_start = False
choose_goal = False


class Selected_Algo(Enum):
    BFS = auto()
    DFS = auto()
    A_STAR = auto()
    DIJKSTRA = auto()


selected_algo = Selected_Algo.BFS

pygame.init()
pygame.display.set_caption('Pathfinding Algorithm Thunderdome')
window_surface = pygame.display.set_mode(s.get_window_size())
manager = pygame_gui.UIManager(s.get_window_size())

grid_top_left_x, grid_top_left_y = s.get_grid_top_left_coordinates()
grid_width, grid_height = s.get_grid_size()

drop_down = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(grid_top_left_x + grid_width - 350 + 2, grid_top_left_y + grid_height + 5, 110, 30),
                                               manager=manager, options_list=[
    '20x20', '40x40', '80x80', '100x100', '200x200'],
    starting_option='20x20')

algo_drop_down = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(grid_top_left_x + grid_width - 250 + 12, grid_top_left_y + grid_height + 5, 100, 30),
                                                    manager=manager, options_list=[
    'BFS', 'DFS', 'A*', 'Dijkstra'],
    starting_option='BFS')

set_start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((grid_top_left_x - 2, grid_top_left_y - 55), (155, 50)),
                                                text='Choose Start',
                                                manager=manager)

set_goal_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((grid_top_left_x + 153, grid_top_left_y - 55), (155, 50)),
                                               text='Choose Goal',
                                               manager=manager)

draw_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((grid_top_left_x + 153 + 155, grid_top_left_y - 55), (155, 50)),
                                           text='Draw Obstacles',
                                           manager=manager)

erase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((grid_top_left_x + 153 + 155 + 155, grid_top_left_y - 55), (155, 50)),
                                            text='Erase Obstacles',
                                            manager=manager)

random_obstacle_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((grid_top_left_x + 153 + 155 + 155 + 155, grid_top_left_y - 55), (155, 50)),
                                                      text='Random Obstacles',
                                                      manager=manager)

clear_grid_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((grid_top_left_x - 2, grid_top_left_y + grid_height + 5), (140, 30)),
                                                 text='Clear Grid',
                                                 manager=manager)

reset_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((grid_top_left_x + grid_width - 140 + 2, grid_top_left_y + grid_height + 55), (140, 40)),
                                            text='Reset',
                                            manager=manager)

find_path_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((grid_top_left_x + grid_width - 140 + 2, grid_top_left_y + grid_height + 5), (140, 50)),
                                                text='Find Path',
                                                manager=manager)

steps_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((grid_top_left_x + 137, grid_top_left_y + grid_height + 5), (316, 30)),
                                                      start_value=5,
                                                      value_range=(1, 1500),
                                                      manager=manager)

text_block = pygame_gui.elements.UITextBox('<font face=fira_code size=5 #FFFFFF>'
                                           '</font>',
                                           pygame.Rect(
                                               (grid_top_left_x - 2, grid_top_left_y + grid_height + 35), (665, 60)),
                                           manager=manager)


def reset_all_buttons():
    global draw_on, erase_on, choose_start, choose_goal

    draw_on = False
    erase_on = False
    choose_start = False
    choose_goal = False
    set_start_button.unselect()
    draw_button.unselect()
    erase_button.unselect()
    set_goal_button.unselect()


def main():

    global selected_algo
    start_node = None
    goal_node = None
    last_mouse_position = None
    mouse_down = False
    global draw_on, erase_on, choose_start, choose_goal
    global text_block

    clock = pygame.time.Clock()
    is_running = True
    grid = create_grid()

    all_states = None
    counter = 0
    steps_per_frame = 5

    # Main pygame loop
    while is_running:
        time_delta = clock.tick(60)/1000.0

        hovered_while_mouse_down = []

        if all_states:
            for _ in range(steps_per_frame):
                if counter < len(all_states):
                    # Process one algorithm step
                    node_to_change = grid[all_states[counter]
                                          [0]][all_states[counter][1]]
                    node_to_change.state = all_states[counter][2]
                    counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == find_path_button:
                    # print('Clicked Find Path!')
                    # Reset display if previous visual is still up
                    if all_states:
                        all_states.clear()
                    counter = 0
                    for i in range(len(grid)):
                        for j in range(len(grid[i])):
                            if grid[i][j].state == Node_State.START or grid[i][j].state == Node_State.GOAL or grid[i][j].state == Node_State.OBSTACLE:
                                pass
                            else:
                                grid[i][j].state = Node_State.EMPTY
                    reset_all_buttons()
                    text_block_font_size = 3
                    match selected_algo:
                        case Selected_Algo.BFS:
                            # Make a copy of grid_parameter so the algorithm is not immediately acting on the state of the original grid
                            grid_copy = copy.deepcopy(grid)
                            tic = time.perf_counter()
                            all_states = breadth_first_search(
                                grid_copy, start_node)
                            toc = time.perf_counter()
                            text_block.kill()
                            text_block = pygame_gui.elements.UITextBox(
                                f'<font face=fira_code size={text_block_font_size} #FFFFFF>Breadth First Search:\n   Path length = {count_path_length(all_states) + 1}, ran in {(toc - tic) * 1000:0.2f} milliseconds, performed {len(all_states):,} steps.</font>', pygame.Rect(
                                    (grid_top_left_x - 2, grid_top_left_y + grid_height + 35), (665, 60)), manager=manager)
                        case Selected_Algo.DFS:
                            # Make a copy of grid_parameter so the algorithm is not immediately acting on the state of the original grid
                            grid_copy = copy.deepcopy(grid)
                            tic = time.perf_counter()
                            all_states = depth_first_search(
                                grid_copy, start_node)
                            toc = time.perf_counter()
                            text_block.kill()
                            text_block = pygame_gui.elements.UITextBox(
                                f'<font face=fira_code size={text_block_font_size} #FFFFFF>Depth First Search:\n   Path length = {count_path_length(all_states) + 1}, ran in {(toc - tic) * 1000:0.2f} milliseconds, performed {len(all_states):,} steps.</font>', pygame.Rect(
                                    (grid_top_left_x - 2, grid_top_left_y + grid_height + 35), (665, 60)), manager=manager)
                        case Selected_Algo.A_STAR:
                            modified_grid, start, end = convert_node_grid_to_grid_square_grid(
                                grid)
                            tic = time.perf_counter()
                            all_states = astar(modified_grid, start, end)
                            toc = time.perf_counter()
                            text_block.kill()
                            text_block = pygame_gui.elements.UITextBox(
                                f'<font face=fira_code size={text_block_font_size} #FFFFFF>A*:\n   Path length = {count_path_length(all_states)}, ran in {(toc - tic) * 1000:0.2f} milliseconds, performed {len(all_states):,} steps.</font>', pygame.Rect(
                                    (grid_top_left_x - 2, grid_top_left_y + grid_height + 35), (665, 60)), manager=manager)
                        case Selected_Algo.DIJKSTRA:
                            modified_grid, start, end = convert_node_grid_to_grid_square_grid(
                                grid)
                            tic = time.perf_counter()
                            all_states = dijkstra(modified_grid, start, end)
                            toc = time.perf_counter()
                            text_block.kill()
                            text_block = pygame_gui.elements.UITextBox(
                                f'<font face=fira_code size={text_block_font_size} #FFFFFF>Dijkstra\'s:\n   Path length = {count_path_length(all_states)}, ran in {(toc - tic) * 1000:0.2f} milliseconds, performed {len(all_states):,} steps.</font>', pygame.Rect(
                                    (grid_top_left_x - 2, grid_top_left_y + grid_height + 35), (665, 60)),
                                manager=manager)
                if event.ui_element == clear_grid_button:
                    # print('Clicked Clear!')
                    if all_states:
                        all_states.clear()
                    if start_node:
                        start_node = None
                    if goal_node:
                        goal_node = None
                    counter = 0
                    grid = create_grid()
                    text_block.kill()
                    text_block = pygame_gui.elements.UITextBox(f'<font face=fira_code size=5 #FFFFFF></font>',
                                                               pygame.Rect(
                                                                   (grid_top_left_x - 2, grid_top_left_y + grid_height + 35), (665, 60)),
                                                               manager=manager)

                if event.ui_element == reset_button:
                    # print('Clicked Reset!')
                    if all_states:
                        all_states.clear()
                    counter = 0
                    for i in range(len(grid)):
                        for j in range(len(grid[i])):
                            if grid[i][j].state == Node_State.START or grid[i][j].state == Node_State.GOAL or grid[i][j].state == Node_State.OBSTACLE:
                                pass
                            else:
                                grid[i][j].state = Node_State.EMPTY

                if event.ui_element == random_obstacle_button:
                    # print('Clicked Random Obstacle!')
                    for i in range(len(grid)):
                        for j in range(len(grid[i])):
                            if grid[i][j].state == Node_State.START or grid[i][j].state == Node_State.GOAL or grid[i][j].state == Node_State.OBSTACLE:
                                pass
                            else:
                                if random.randint(1, 100) < 20:
                                    grid[i][j].state = Node_State.OBSTACLE

                if event.ui_element == draw_button:
                    # print('Clicked Draw!')
                    draw_on = not draw_on
                    if draw_on:
                        reset_all_buttons()
                        draw_on = True
                        draw_button.select()
                    else:
                        draw_button.unselect()

                if event.ui_element == erase_button:
                    # print('Clicked Erase!')
                    erase_on = not erase_on
                    if erase_on:
                        reset_all_buttons()
                        erase_on = True
                        erase_button.select()
                    else:
                        erase_button.unselect()

                if event.ui_element == set_start_button:
                    choose_start = not choose_start
                    if choose_start:
                        reset_all_buttons()
                        choose_start = True
                        set_start_button.select()
                    else:
                        set_start_button.unselect()

                if event.ui_element == set_goal_button:
                    choose_goal = not choose_goal
                    if choose_goal:
                        reset_all_buttons()
                        choose_goal = True
                        set_goal_button.select()
                        set_start_button.unselect()
                    else:
                        set_goal_button.unselect()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
                last_mouse_position = pygame.mouse.get_pos()
                click_grid_pos = screen_to_grid(last_mouse_position)
                hovered_while_mouse_down.append(click_grid_pos)

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
                last_mouse_position = None

            if event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    current_mouse_position = pygame.mouse.get_pos()
                    if last_mouse_position:
                        start_grid = screen_to_grid(last_mouse_position)
                        end_grid = screen_to_grid(current_mouse_position)
                        line_points = generate_grid_line_points(
                            start_grid, end_grid)
                        hovered_while_mouse_down.extend(line_points)
                    last_mouse_position = current_mouse_position

            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == drop_down:
                    # print("Grid size dropdown changed to:", event.text)
                    delimiter = event.text.find('x')
                    s.set_columns(int(event.text[:delimiter]))
                    grid = create_grid()
                elif event.ui_element == algo_drop_down:
                    # print("Algorithm dropdown changed to:", event.text)
                    if event.text == 'BFS':
                        selected_algo = Selected_Algo.BFS
                    elif event.text == 'DFS':
                        selected_algo = Selected_Algo.DFS
                    elif event.text == 'A*':
                        selected_algo = Selected_Algo.A_STAR
                    elif event.text == 'Dijkstra':
                        selected_algo = Selected_Algo.DIJKSTRA

            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == steps_slider:
                    steps_per_frame = steps_slider.get_current_value()
                    # print(f"Steps per frame adjusted to: {steps_per_frame}")

            manager.process_events(event)

        for grid_pos in hovered_while_mouse_down:
            grid_column, grid_row = grid_pos
            if 0 <= grid_row < len(grid) and 0 <= grid_column < len(grid[0]):
                # Update grid based on button state, draw_on, erase_on, etc.
                if draw_on:
                    grid[grid_row][grid_column].state = Node_State.OBSTACLE
                elif erase_on:
                    grid[grid_row][grid_column].state = Node_State.EMPTY
                elif choose_start:
                    for i in range(len(grid)):
                        for j in range(len(grid[i])):
                            if grid[i][j].state == Node_State.START:
                                grid[i][j].state = Node_State.EMPTY
                    grid[grid_row][grid_column].state = Node_State.START
                    start_node = grid[grid_row][grid_column]
                elif choose_goal:
                    for i in range(len(grid)):
                        for j in range(len(grid[i])):
                            if grid[i][j].state == Node_State.GOAL:
                                grid[i][j].state = Node_State.EMPTY
                    grid[grid_row][grid_column].state = Node_State.GOAL
                    goal_node = grid[grid_row][grid_column]
        manager.update(time_delta)

        draw_window(window_surface, grid, start_node, goal_node)
        manager.draw_ui(window_surface)
        pygame.display.update()


if __name__ == "__main__":
    main()
