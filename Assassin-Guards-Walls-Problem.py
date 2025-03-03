from collections import deque
import matplotlib.pyplot as plt

def draw_maze(board, explored=None, shortest_path=None):
    """
    Draws the maze with walls, guards, observed areas, and paths.
    
    :param board: List of strings representing the maze.
    :param explored: List of (row, col) positions representing explored paths.
    :param shortest_path: List of (row, col) positions representing the shortest path.
    """
    N, M = len(board), len(board[0])
    
    fig, ax = plt.subplots(figsize=(M, N))
    ax.set_xlim(-0.5, M + 0.5)
    ax.set_ylim(-0.5, N + 0.5)
    
    # Set the background color to light gray
    fig.patch.set_facecolor('lightgray')
    
    # Color mapping
    colors = {
        'X': 'black',  # Walls
        '<': 'red', '>': 'red', '^': 'red', 'v': 'red',  # Guards
        '*': 'lightgray',  # Observed cells
        '.': 'white'  # Empty cells
    }

    # Draw grid
    for i in range(N):
        for j in range(M):
            cell = board[i][j]
            color = colors.get(cell, 'white')
            ax.add_patch(plt.Rectangle((j, N - i - 1), 1, 1, facecolor=color, edgecolor="gray"))
    
    # Draw explored paths
    if explored:
        for (x, y) in explored:
            if shortest_path and (x, y) in shortest_path:
                continue  # Avoid overwriting shortest path color
            ax.add_patch(plt.Rectangle((y, N - x - 1), 1, 1, color="blue", alpha=0.4))
    
    # Draw shortest path in green
    if shortest_path:
        for (x, y) in shortest_path:
            ax.add_patch(plt.Rectangle((y, N - x - 1), 1, 1, color="green", alpha=0.6))

    # Draw assassin position (A)
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'A':
                ax.add_patch(plt.Circle((j + 0.5, N - i - 0.5), 0.3, color="blue", zorder=3))

    # Draw goal position (bottom-right corner)
    ax.add_patch(plt.Circle((M - 1 + 0.5, 0.5), 0.3, color="yellow", zorder=3))

    # Remove axis labels
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

    # Add legend text in the top-left corner
    legend_text = (
        "Legend:\n"
        "Black - Wall\n"
        "Red - Guard\n"
        "Gray - Observed Area\n"
        "White - Empty Cell\n"
        "Blue Circle - Assassin's Position\n"
        "Yellow Circle - Target Position\n"
        "Blue Rectangle - Explored Path\n"
        "Green Rectangle - Shortest Path"
    )
    ax.text(-0.15, 1.1, legend_text, transform=ax.transAxes, fontsize=12, fontstyle='italic', verticalalignment='top', 
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='black', boxstyle='round,pad=0.5'))

    # Add a title in the center of the plot
    ax.set_title("Maze Pathfinding Visualizer", fontsize=20, fontweight='bold', color='darkblue', pad=20)
    
    
    ax.text(M + 0, -0.9, "Written and Developed by:\nLoay Egbaria",
        fontsize=10, fontweight='bold', fontstyle='italic', color='black',
        verticalalignment='bottom', horizontalalignment='left',
        bbox=dict(facecolor='white', alpha=0.7, edgecolor='yellow', boxstyle='round,pad=0.3'))
    
    plt.show()
    
    
    
def solution(B, visualize=False):
    N = len(B)
    M = len(B[0])

    # Convert the board to a list of lists for easier manipulation
    board = [list(row) for row in B]

    # Mark cells observed by guards
    def mark_observed(x, y, dx, dy):
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 'X' or board[nx][ny] in ['<', '>', '^', 'v']:
                break  # Stop if we hit an obstacle or another guard
            if board[nx][ny] in ['.', 'A']:
                board[nx][ny] = '*'  # Mark the cell as observed
            nx += dx
            ny += dy

    # Iterate through the board and mark observed cells
    startX, startY = -1, -1
    for i in range(N):
        for j in range(M):
            c = board[i][j]
            if c == 'A':
                startX, startY = i, j
            elif c == '<':
                mark_observed(i, j, 0, -1)
            elif c == '>':
                mark_observed(i, j, 0, 1)
            elif c == '^':
                mark_observed(i, j, -1, 0)
            elif c == 'v':
                mark_observed(i, j, 1, 0)

    # If the bottom-right cell or the assassin's starting position is observed, return False
    if board[N - 1][M - 1] == '*' or board[startX][startY] == '*':
        if visualize:
            draw_maze(board)
        return False

    # BFS to find a path to the bottom-right cell
    visited = [[False] * M for _ in range(N)]
    queue = deque([(startX, startY, [])])  # Store path along with (x, y)
    visited[startX][startY] = True
    explored = []  # Track explored cells
    shortest_path = []

    while queue:
        x, y, path = queue.popleft()
        explored.append((x, y))

        if x == N - 1 and y == M - 1:
            shortest_path = path + [(x, y)]
            if visualize:
                draw_maze(board, explored, shortest_path)
            return True  # Reached the bottom-right cell

        # Explore all four directions
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if board[nx][ny] == '.':  # Only move into safe, non-observed cells
                    visited[nx][ny] = True
                    queue.append((nx, ny, path + [(x, y)]))

    if visualize:
        draw_maze(board, explored)
    return False  # No path found



# Test Cases and Expected Outputs
test_cases = [
    # Example 1: Basic Path
    {
        "input": [
            "A....",
            ".....",
            ".....",
            ".....",
            "....."
        ],
        "expected_output": True
    },
    
    # Example 2: Blocked Path by Guard and path between two walls
    {
        "input": [
            "A....",
            "..^..",
            "..>..",
            "..X..",
            "X...."
        ],
        "expected_output": True
    },
    
    # Example 3: Guard vision Path blocked by Wall
    {
        "input": [
            "A....",
            "..X..",
            "..^..",
            "..X..",
            "....."
        ],
        "expected_output": True
    },
    
    # Example 4: Guard observing the target position
    {
        "input": [
            "A....",
            ".....",
            "....v",
            ".....",
            ".X..."
        ],
        "expected_output": False
    },
    
    # Example 5: Zigzag path
    {
        "input": [
            "AX..X",
            "..X..",
            "X..X.",
            ".X..X",
            "X.X.."
        ],
        "expected_output": True
    },
    
    # Example 6: Blocked by walls
    {
        "input": [
            "AX...",
            "X....",
            ".....",
            ".....",
            "....."
        ],
        "expected_output": False
    }
]
