# PROMPT
# -----------------------------------------------------------------------------
# As the search for the Chief continues, a small Elf who lives on the 
# station tugs on your shirt; she'd like to know if you could help her 
# with her word search (your puzzle input). She only has to find one word: XMAS.

# This word search allows words to be horizontal, vertical, diagonal, 
# written backwards, or even overlapping other words. It's a little unusual, 
# though, as you don't merely need to find one instance of XMAS - you need 
# to find all of them. Here are a few ways XMAS might appear, where 
# irrelevant characters have been replaced with .:

# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....

# The actual word search will be full of letters instead. For example:

# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX

# In this word search, XMAS occurs a total of 18 times; here's the same 
# word search again, but where letters not involved in any XMAS have been 
# replaced with .:

# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX

# -----------------------------------------------------------------------------

# SOLUTION
# -----------------------------------------------------------------------------

def check_direction(grid, row, col, dr, dc):
    # Check all positions (current and next 3) are within bounds
    for i in range(4):
        new_row = row + i*dr
        new_col = col + i*dc
        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            return False
    
    # Only access positions after we've confirmed they're all valid
    try:
        result = (grid[row][col] == 'X' and 
                grid[row+dr][col+dc] == 'M' and
                grid[row+2*dr][col+2*dc] == 'A' and 
                grid[row+3*dr][col+3*dc] == 'S')
    except IndexError:
        return False
    
    return result

def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # Check all 8 directions
    directions = [
        (-1,-1), (-1,0), (-1,1),  # Up diagonals and vertical
        (0,-1),         (0,1),    # Horizontal
        (1,-1),  (1,0),  (1,1)    # Down diagonals and vertical
    ]
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(grid, r, c, dr, dc):
                    count += 1
                    
    return count

def main():
    with open('input.txt', 'r') as f:
        # Convert each line into a list of characters
        grid = [list(line.strip()) for line in f.readlines()]
    
    result = count_xmas(grid)
    print(f"Found {result} instances of XMAS")

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------
