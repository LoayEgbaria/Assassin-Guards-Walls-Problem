# Maze Pathfinding with Guard Vision and Walls

This repository contains a Python script that implements a pathfinding algorithm to determine if an assassin can safely reach a target position in a maze while avoiding obstacles and guards. The maze is represented as a grid, and the algorithm uses **Breadth-First Search (BFS)** to find the shortest path from the assassin’s starting position to the target position, while considering walls, guard vision, and obstacles.

## Key Features

- **Maze Representation**: The maze is defined as a grid of characters:
  - **'A'**: Assassin's starting position
  - **'.'**: Walkable empty space
  - **'X'**: Walls that block movement
  - **'<'**, **'>'**, **'^'**, **'v'**: Guards, each observing in a specific direction
  - **'*'**: Cells observed by guards (determined dynamically)

- **Guard Vision**: The script dynamically marks the cells observed by guards based on their direction (left, right, up, down).

- **Pathfinding Algorithm**: The **Breadth-First Search (BFS)** algorithm is used to explore paths from the assassin's starting position to the target (bottom-right corner) while avoiding walls and areas observed by guards.

- **Visualization**: The `draw_maze` function provides a visual representation of the maze, including:
  - Explored paths (blue)
  - Shortest path (green, if found)
  - Walls, guards, and observed areas with distinct colors
  - Assassin's starting position (blue circle)
  - Target position (yellow circle)

## How It Works

### 1. **Guard Vision**:
   - Each guard (denoted by **'<'**, **'>'**, **'^'**, **'v'**) marks a straight line of sight in the direction they are facing.
   - The `mark_observed` function marks cells as observed (`*`) as they are in the guard's line of sight, stopping when a wall (`X`) or another guard is encountered.

### 2. **BFS Pathfinding**:
   - The **BFS** algorithm starts from the assassin's position (**'A'**) and explores neighboring cells (up, down, left, right).
   - The algorithm ensures that only cells marked as unobserved and walkable (i.e., **'.'**) are explored. If a path leads to the target position (bottom-right corner), it is marked as the shortest path.

### 3. **Visualization**:
   - The maze is displayed with visual elements showing:
     - **Walls** (black)
     - **Guards** (red)
     - **Observed Areas** (light gray)
     - **Explored Paths** (blue)
     - **Shortest Path** (green)
     - **Assassin's Position** (blue circle)
     - **Target Position** (yellow circle)

### 4. **Functionality**:
   - The `solution` function runs the algorithm and determines if a path exists from the assassin's starting position (**'A'**) to the target position (bottom-right corner).
   - If visualization is enabled (`visualize=True`), the function will display the maze and exploration process.

## Running the Code

### Requirements:
- Python 3.x
- Required Python libraries:
  - `matplotlib`
  - `collections` (built-in)

### To run the script:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/maze-pathfinding.git
   cd maze-pathfinding
Install the required dependencies (if you don’t have them installed):

bash
Copy
Edit
pip install matplotlib
Run the pathfinding.py script:

bash
Copy
Edit
python pathfinding.py
This will run the test cases and show visualizations of the maze and the BFS exploration process.

How to Create and Test Your Own Maze:
To create your own maze, modify the test_cases section in the script. The maze is represented as a list of strings, where each string corresponds to a row of the maze. Here's an example of how to define your maze:

python
Copy
Edit
test_cases = [
    {
        "input": 
        [
            "A....",

            ".....",

            ".....",

            ".....",

            "....."
        ],
        
        "expected_output": True
    }
]

'A': The starting position of the assassin.

'.': Walkable space.

'X': Walls.

'<', '>', '^', 'v': Guards, each observing in a specific direction.

'*': Cells observed by guards.

You can modify the maze layout and define multiple test cases to check different scenarios.

Example Test Cases
Here are a few test cases you can run:

Basic Path: The assassin can move freely to the target position.

python
Copy
Edit

"input": 
[
    "A....",

    ".....",

    ".....",

    ".....",

    "....."
]

Blocked Path by Guard and Path Between Two Walls: The assassin can still find a path avoiding the guards.

python
Copy
Edit

"input": 
[
    "A....",

    "..^..",

    "..>..",

    "..X..",

    "X...."
]

Guard Observing the Target Position: The assassin cannot reach the target as the target is observed by the guard.

python
Copy
Edit

"input": 
[
    "A....",

    ".....",

    "....v",

    ".....",

    ".X..."
]

Walls Surrounding the Assassin: The assassin is trapped by walls and cannot move.

python
Copy
Edit

"input": 
[
    "AXXX.",

    ".....",

    ".....",

    ".....",

    "....."
]

License
This project is licensed under the MIT License - see the LICENSE file for details.

Developed by:
Loay Egbaria