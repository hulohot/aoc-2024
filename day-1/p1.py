# PROMPT
# -----------------------------------------------------------------------------
# Given a list of number pairs in input.txt, find the cumulative sum of the absolute
# differences between each pair after sorting both lists of numbers independently.
# For example, if the input has pairs (5,3) and (1,4), we first sort both lists
# to get [1,5] and [3,4], then sum the absolute differences: |1-3| + |5-4| = 3
# -----------------------------------------------------------------------------


# SOLUTION
# -----------------------------------------------------------------------------

# Read the input into a list of tuples
with open('input.txt', 'r') as file:
    pairs = [tuple(map(int, line.split())) for line in file]

# Make two lists, one for the left values and one for the right values
left_values = [pair[0] for pair in pairs]
right_values = [pair[1] for pair in pairs]

# Sort the left and right values
left_values.sort()
right_values.sort()

# Find the cumulative sum of the absolute differences between the left and right values
cumulative_sum = sum(abs(left - right) for left, right in zip(left_values, right_values))

print(cumulative_sum)

# -----------------------------------------------------------------------------