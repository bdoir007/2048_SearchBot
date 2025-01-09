import logic
import evaluation


def available_moves(grid):
    grid_right = logic.move_right(grid)
    grid_left = logic.move_left(grid)
    grid_up = logic.move_up(grid)
    grid_down = logic.move_down(grid)

    move_list = ['R', 'L', 'U', 'D']
    i = 0
    if grid_right == grid:
        move_list.pop(0)
        i += 1
    if grid_left == grid:
        move_list.pop(1 - i)
        i += 1
    if grid_up == grid:
        move_list.pop(2 - i)
        i += 1
    if grid_down == grid:
        move_list.pop(3 - i)
        i += 1
    return move_list


def available_moves_probability(grid):
    possible_moves = available_moves(grid)
    prob = 1 / len(possible_moves)
    return [(move, prob) for move in possible_moves]


def simulation(grid, move):
    """
    grid,move-->grid
    """
    if move == 'R':
        returned_grid = logic.move_right(grid)
    elif move == 'L':
        returned_grid = logic.move_left(grid)
    elif move == 'U':
        returned_grid = logic.move_up(grid)
    else:
        returned_grid = logic.move_down(grid)

    return returned_grid


def simulate_spawn(grid, tile_value, coords):
    new_grid = grid.copy()
    new_grid[coords[0]][coords[1]] = tile_value
    return new_grid


def find_empty_squares(grid):
    coord_list = []
    for i in range(len(grid)):
        for j in range(i):
            if grid[i][j] == 0:
                coord_list.append((i, j))
    return coord_list


def remove_tile(grid, i, j):
    grid[i][j] = 0
    return grid


def available_spawns_probability(grid):
    squares_values_probability = []
    for x in find_empty_squares(grid):
        squares_values_probability.append((x, 2, 9 / 10))
        squares_values_probability.append((x, 4, 1 / 10))
    return squares_values_probability


def expectimax_search(grid, depth, player_turn, weights):
    if depth == 0 or logic.get_current_state(grid) == 'LOST':
        return evaluation.total_score(grid, weights)

    value = 0

    if player_turn:

        for move in available_moves(grid):
            new_board = simulation(grid, move)

            score = expectimax_search(new_board, depth - 1, False, weights)
            #print(score)
        value = max(score, value)

    else:
        score = 0
        for x in find_empty_squares(grid):

            score += 1/evaluation.empty_squares(grid) * expectimax_search(grid, depth - 1, True, weights)
        value = max(score, value)

    return value


def find_best_move(grid, weights):
    depth = 5
    best_move = None
    best_score = 0

    for move in available_moves(grid):
        #print("Looking at: " + move)
        new_board = simulation(grid, move)
        score = expectimax_search(new_board, depth, True, weights)
        #print("Search score: " + str(score) + " Best score: " + str(best_score))
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


# print(available_moves([[0,0,0,0], [0,0,0,0],[0,0,2,4],[0,0,2,4]]))
# print(simulation([[0,0,0,0], [0,2,0,0],[0,0,0,0],[0,0,0,0]], 'R#'))
#print(expectimax_search([[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 3, True))

# print(find_best_move([[0, 0, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4]]))

# print(evaluation.total_score(logic.move_down([[0, 0, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4]])))
# print(evaluation.total_score(logic.move_right([[0, 0, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4]])))
