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