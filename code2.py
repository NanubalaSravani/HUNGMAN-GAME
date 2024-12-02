from collections import deque

# Define directions for movements
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

def is_in_bounds(x, y, m, n):
    """ Check if (x, y) is within matrix bounds """
    return 0 <= x < m and 0 <= y < n

def can_place_sofa(x, y, orientation, matrix):
    """ Check if sofa can be placed at (x, y) with given orientation """
    if orientation == "horizontal":
        return (is_in_bounds(x, y + 1, len(matrix), len(matrix[0])) and
                matrix[x][y] == ' ' and matrix[x][y + 1] == ' ')
    elif orientation == "vertical":
        return (is_in_bounds(x + 1, y, len(matrix), len(matrix[0])) and
                matrix[x][y] == ' ' and matrix[x + 1][y] == ' ')
    return False

def get_possible_moves(x, y, orientation, matrix):
    """ Get all valid moves from current position (x, y) in given orientation """
    moves = []
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if can_place_sofa(nx, ny, orientation, matrix):
            moves.append((nx, ny, orientation))
    return moves

def can_rotate(x, y, matrix):
    """ Check if sofa can rotate within a 2x2 area starting at (x, y) """
    return (is_in_bounds(x + 1, y + 1, len(matrix), len(matrix[0])) and
            matrix[x][y] == ' ' and matrix[x][y + 1] == ' ' and
            matrix[x + 1][y] == ' ' and matrix[x + 1][y + 1] == ' ')

def bfs(matrix, start_pos, target_pos):
    m, n = len(matrix), len(matrix[0])
    queue = deque([(start_pos[0], start_pos[1], "horizontal", 0)])  # (x, y, orientation, steps)
    visited = set([(start_pos[0], start_pos[1], "horizontal")])

    while queue:
        x, y, orientation, steps = queue.popleft()

        # Check if target is reached
        if (x, y) == target_pos and orientation == "horizontal":
            return steps

        # Try all possible moves
        for nx, ny, new_orientation in get_possible_moves(x, y, orientation, matrix):
            if (nx, ny, new_orientation) not in visited:
                queue.append((nx, ny, new_orientation, steps + 1))
                visited.add((nx, ny, new_orientation))

        # Try rotation if a 2x2 area is available
        if can_rotate(x, y, matrix):
            new_orientation = "vertical" if orientation == "horizontal" else "horizontal"
            if (x, y, new_orientation) not in visited:
                queue.append((x, y, new_orientation, steps + 1))
                visited.add((x, y, new_orientation))

    return -1  # Return -1 if no valid path is found

# Example matrix
matrix = [
    [' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 's', 's', 'H', ' ', ' ', ' ', ' ', ' ', 'S', 'S', ' ', ' '],
    [' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

# Define start and target positions for the sofa
start_pos = (2, 2)  # starting position (top-left corner of sofa)
target_pos = (2, 10)  # target position (top-left corner of target)

# Run the BFS to find the minimum steps
steps = bfs(matrix, start_pos, target_pos)
print("Minimum steps to move the sofa to the target:", steps)