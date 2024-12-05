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

# The Elf looks quizzically at you. Did you misunderstand the assignment?

# Looking for the instructions, you flip over the word search to find that 
# this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're 
# supposed to find two MAS in the shape of an X. One way to achieve that is like this:

# M.S
# .A.
# M.S

# Irrelevant characters have again been replaced with . in the above diagram. 
# Within the X, each MAS can be written forwards or backwards.

# Here's the same example from before, but this time all of the X-MASes have 
# been kept instead:

# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........

# Results in 18 X-MASes.

# -----------------------------------------------------------------------------

# SOLUTION
# -----------------------------------------------------------------------------

def check_xmas_pattern(grid, row, col):
    """Check if there's an X-MAS pattern starting at the given position"""
    rows = len(grid)
    cols = len(grid[0])
    
    # Check bounds for a 3x3 grid
    if row + 2 >= rows or col + 2 >= cols:
        return False
        
    # Check both MAS sequences (can be forwards or backwards)
    def is_mas(a, b, c):
        return (a == 'M' and b == 'A' and c == 'S') or (a == 'S' and b == 'A' and c == 'M')
    
    try:
        # Check diagonal patterns more safely
        top_left_to_bottom_right = is_mas(
            grid[row][col], 
            grid[row+1][col+1], 
            grid[row+2][col+2]
        )
        top_right_to_bottom_left = is_mas(
            grid[row][col+2], 
            grid[row+1][col+1], 
            grid[row+2][col]
        )
        
        return top_left_to_bottom_right and top_right_to_bottom_left
        
    except IndexError:
        # If we somehow still get an index error, return False
        return False

def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for r in range(rows-2):  # -2 to leave room for 3x3 pattern
        for c in range(cols-2):
            if check_xmas_pattern(grid, r, c):
                count += 1
                
    return count

def main():
    with open('input.txt', 'r') as f:
        # Convert each line into a list of characters
        grid = [list(line.strip()) for line in f.readlines()]
    
    result = count_xmas_patterns(grid)
    print(f"Found {result} X-MAS patterns")

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------
