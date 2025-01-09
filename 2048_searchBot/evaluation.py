
def tile_positioning(grid):
    """
    (grid)-->int
    returns a higher score if the tiles with higher values are at the edge of the board
    """
    position_score = 0
    for y in range(4):
        for x in range(4):
            value = grid[y][x]

            if y == 0 or y == 3:
                y_score = 1
            else:
                y_score = 0.5

            if x == 0 or x == 3:
                x_score = 1
            else:
                x_score = 0.5

            position_score += y_score * value + x_score * value

    return position_score


def monotonicity(row):
    """
    list-->int
    returns a higher score if the rows are in ascending/descending order
    """
    ascending = 0
    descending = 0

    # check ascending
    for i in range(len(row) - 1):
        if row[i] <= row[i + 1]:
            ascending += 1

    # check descending
    for j in range(len(row) - 1):
        if row[j] >= row[j + 1]:
            descending += 1

    return max(ascending, descending)


def monotonicity_score(grid):
    """
    grid-->int
    calculates the monotonicity score for the whole game grid
    """
    score = 0

    for line in grid:
        score += monotonicity(line)

    for col in range(4):
        column = [grid[row][col] for row in range(4)]
        score += monotonicity(column)

    return score


def log_base2(n):
    """
    int-->int
    returns the logarithm base 2 of the number n using a bit-shift
    """
    return n.bit_length - 1


def smoothness(row):
    """
    row-->int
    returns the smoothness score for a single row in the grid
    """
    score = 0
    for i in range(len(row) - 1):
        if row[i] <= row[i + 1]:
            score += log_base2(row[i + 1]) - log_base2(row[i])
        else:
            score += log_base2(row[i]) - log_base2(row[i + 1])
    return score


def smoothness_score(grid):
    """
    grid--> int
    returns the smoothness score for an entire grid
    """
    score = 0

    for line in grid:
        score += monotonicity(line)

    for col in range(4):
        column = [grid[row][col] for row in range(4)]
        score += monotonicity(column)

    return score


def max_value(grid):
    """
    grid-->int
    returns the maximum tile value in the grid
    """
    max_val = 0
    for line in grid:
        for i in line:
            if i >= max_val:
                max_val = i
    return max_val


def empty_squares(grid):
    empty_count = 0

    for line in grid:
        for i in line:
            if i == 0:
                empty_count += 1
    return empty_count


def total_score(grid, weights):
    score = (weights[0] * tile_positioning(grid) + weights[1] * monotonicity_score(grid) + weights[2] * smoothness_score(grid) +
             weights[3] * max_value(grid) + weights[4] * empty_squares(grid))
    return score



