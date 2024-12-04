# PROMPT
# -----------------------------------------------------------------------------
# Given a list of number pairs in input.txt, find the similarity score between
# the two lists. For each number in the left list, multiply it by how many times
# that same number appears in the right list, then sum all these products.
# For example, if left=[1,2,1] and right=[1,3,1], the score would be:
# 1 × (appears twice in right) + 2 × (appears zero times) + 1 × (appears twice) = 4
# -----------------------------------------------------------------------------


# SOLUTION
# -----------------------------------------------------------------------------

# Read the input into a list of tuples
with open('input.txt', 'r') as file:
    pairs = [tuple(map(int, line.split())) for line in file]

# Make two lists, one for the left values and one for the right values
left_values = [pair[0] for pair in pairs]
right_values = [pair[1] for pair in pairs]

# Find the similarity score
# For each item in the left values, multiply it by the count of that item in the right values
similarity_score = sum(left * right_values.count(left) for left in left_values)

print(similarity_score)

# -----------------------------------------------------------------------------