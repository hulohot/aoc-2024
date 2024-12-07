# PROMPT
# -----------------------------------------------------------------------------

# The map shows the current position of the guard with ^ (to indicate the guard 
# is currently facing up from the perspective of the map). Any obstructions - 
# crates, desks, alchemical reactors, etc. - are shown as #.

# Lab guards in 1518 follow a very strict patrol protocol which involves 
# repeatedly following these steps:

# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.

# Following the above protocol, the guard moves up several times until she 
# reaches an obstacle (in this case, a pile of failed suit prototypes):

# ....#.....
# ....^....#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#...

# Because there is now an obstacle in front of the guard, she turns right 
# before continuing straight in her new facing direction:

# ....#.....
# ........>#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#...

# Reaching another obstacle (a spool of several very long polymers), she 
# turns right again and continues downward:

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#......v.
# ........#.
# #.........
# ......#...

# This process continues for a while, but the guard eventually leaves the 
# mapped area (after walking past a tank of universal solvent):

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#v..

# By predicting the guard's route, you can determine which specific 
# positions in the lab will be in the patrol path. Including the guard's 
# starting position, the positions visited by the guard before leaving the 
# area are marked with an X:

# ....#.....
# ....XXXXX#
# ....X...X.
# ..#.X...X.
# ..XXXXX#X.
# ..X.X.X.X.
# .#XXXXXXX.
# .XXXXXXX#.
# #XXXXXXX..
# ......#X..
# In this example, the guard will visit 41 distinct positions on your map.

# -----------------------------------------------------------------------------


# SOLUTION
# -----------------------------------------------------------------------------

def parse_input(filename):
    """Parse input file into grid and starting position."""
    with open(filename) as f:
        lines = f.read().strip().split('\n')
    
    grid = []
    start_pos = None
    for i, line in enumerate(lines):
        row = list(line)
        if '^' in line:
            start_pos = (i, line.index('^'))
            row[start_pos[1]] = '.'  # Replace ^ with . in grid
        grid.append(row)
    
    return grid, start_pos

def get_next_pos(pos, direction):
    """Get next position based on current position and direction."""
    if direction == 'N':
        return (pos[0] - 1, pos[1])
    elif direction == 'E':
        return (pos[0], pos[1] + 1)
    elif direction == 'S':
        return (pos[0] + 1, pos[1])
    else:  # W
        return (pos[0], pos[1] - 1)

def is_valid_pos(pos, grid):
    """Check if position is within grid bounds."""
    return (0 <= pos[0] < len(grid) and 
            0 <= pos[1] < len(grid[0]))

def is_blocked(pos, grid):
    """Check if position contains an obstacle."""
    return grid[pos[0]][pos[1]] == '#'

def turn_right(direction):
    """Get new direction after turning right."""
    directions = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    return directions[direction]

def simulate_patrol(grid, start_pos):
    """Simulate guard's patrol and return set of visited positions."""
    visited = {start_pos}
    pos = start_pos
    direction = 'N'  # Start facing north
    
    while True:
        # Get position in front
        next_pos = get_next_pos(pos, direction)
        
        # Check if we've left the grid
        if not is_valid_pos(next_pos, grid):
            break
            
        # If blocked, turn right
        if is_blocked(next_pos, grid):
            direction = turn_right(direction)
        else:
            # Move forward
            pos = next_pos
            visited.add(pos)
    
    return visited

def main():
    grid, start_pos = parse_input('input.txt')
    visited = simulate_patrol(grid, start_pos)
    print(f"Number of positions visited: {len(visited)}")

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------
