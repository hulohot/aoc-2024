# PROMPT
# -----------------------------------------------------------------------------

# The map shows the current position of the guard with ^ (to indicate the guard 
# is currently facing up from the perspective of the map). Any obstructions - 
# crates, desks, alchemical reactors, etc. - are shown as #.

# Lab guards in 1518 follow a very strict patrol protocol which involves 
# repeatedly following these steps:

# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.

# Fortunately, they are pretty sure that adding a single new obstruction 
# won't cause a time paradox. They'd like to place the new obstruction in 
# such a way that the guard will get stuck in a loop, making the rest of the 
# lab safe to search.

# To have the lowest chance of creating a time paradox, The Historians would 
# like to know all of the possible positions for such an obstruction. The new 
# obstruction can't be placed at the guard's starting position - the guard is 
# there right now and would notice.

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

def simulate_patrol_with_obstacle(grid, start_pos, obstacle_pos):
    """Simulate guard's patrol with an additional obstacle and detect loops."""
    visited_states = set()  # Track (position, direction) states
    pos = start_pos
    direction = 'N'
    steps = 0
    max_steps = len(grid) * len(grid[0]) * 4  # Maximum possible unique states
    
    # Add obstacle to grid
    grid = [row[:] for row in grid]  # Make a copy
    grid[obstacle_pos[0]][obstacle_pos[1]] = '#'
    
    while steps < max_steps:
        state = (pos, direction)
        if state in visited_states:
            return True  # Loop detected
        
        visited_states.add(state)
        next_pos = get_next_pos(pos, direction)
        
        if not is_valid_pos(next_pos, grid):
            return False  # Guard leaves grid
            
        if is_blocked(next_pos, grid):
            direction = turn_right(direction)
        else:
            pos = next_pos
            
        steps += 1
    
    return True  # If we reach max steps, assume it's a loop

def find_loop_positions(grid, start_pos):
    """Find all positions where placing an obstacle creates a loop."""
    loop_positions = []
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Skip if position is already blocked or is start position
            if grid[i][j] == '#' or (i, j) == start_pos:
                continue
                
            # Try placing obstacle at this position
            if simulate_patrol_with_obstacle(grid, start_pos, (i, j)):
                loop_positions.append((i, j))
    
    return loop_positions

def main():
    grid, start_pos = parse_input('input.txt')
    loop_positions = find_loop_positions(grid, start_pos)
    print(f"Number of possible positions for new obstacle: {len(loop_positions)}")

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------
