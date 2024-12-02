# Read the input into a list of tuples
with open('input.txt', 'r') as file:
    pairs = [tuple(map(int, line.split())) for line in file]

# Make two lists, one for the left values and one for the right values
left_values = [pair[0] for pair in pairs]
right_values = [pair[1] for pair in pairs]

# print(left_values)
# print(right_values)

# Sort the left and right values
left_values.sort()
right_values.sort()

# print(left_values)
# print(right_values)

# Find the cumulative sum of the absolute differences between the left and right values
cumulative_sum = sum(abs(left - right) for left, right in zip(left_values, right_values))

print(cumulative_sum)