# Read the input into a list of tuples
with open('input.txt', 'r') as file:
    pairs = [tuple(map(int, line.split())) for line in file]

# Make two lists, one for the left values and one for the right values
left_values = [pair[0] for pair in pairs]
right_values = [pair[1] for pair in pairs]

# print(left_values)
# print(right_values)

# Find the similarity score
# For each item in the left values, multiply it by the count of that item in the right values
similarity_score = sum(left * right_values.count(left) for left in left_values)

print(similarity_score)