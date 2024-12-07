# PROMPT
# -----------------------------------------------------------------------------

# You ask how long it'll take; the engineers tell you that it only needs 
# final calibrations, but some young elephants were playing nearby and stole 
# all the operators from their calibration equations! They could finish the 
# calibrations if only someone could determine which test values could 
# possibly be produced by placing any combination of operators into their 
# calibration equations (your puzzle input).

# For example:

# 190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20

# Each line represents a single equation. The test value appears before the 
# colon on each line; it is your job to determine whether the remaining 
# numbers can be combined with operators to produce the test value.

# Operators are always evaluated left-to-right, not according to precedence 
# rules. Furthermore, numbers in the equations cannot be rearranged. Glancing 
# into the jungle, you can see elephants holding two different types of 
# operators: add (+) and multiply (*).

# Only three of the above equations can be made true by inserting operators:

# 190: 10 19 has only one position that accepts an operator: between 10 and 19. 
# Choosing + would give 29, but choosing * would give the test value (10 * 19 = 190).
# 3267: 81 40 27 has two positions for operators. Of the four possible 
# configurations of the operators, two cause the right side to match the test 
# value: 81 + 40 * 27 and 81 * 40 + 27 both equal 3267 (when evaluated 
# left-to-right)!

# 292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.
# The engineers just need the total calibration result, which is the sum of 
# the test values from just the equations that could possibly be true. In the 
# above example, the sum of the test values for the three equations listed 
# above is 3749.

# -----------------------------------------------------------------------------


# SOLUTION
# -----------------------------------------------------------------------------

def evaluate_expression(nums, operators):
    """Evaluate expression with given numbers and operators left-to-right."""
    result = nums[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += nums[i + 1]
        else:  # '*'
            result *= nums[i + 1]
    return result

def generate_operator_combinations(n):
    """Generate all possible combinations of + and * operators for n positions."""
    if n == 0:
        return [[]]
    combinations = []
    for combo in generate_operator_combinations(n - 1):
        combinations.append(combo + ['+'])
        combinations.append(combo + ['*'])
    return combinations

def parse_line(line):
    """Parse input line into test value and numbers."""
    test_value, nums_str = line.split(': ')
    return int(test_value), [int(x) for x in nums_str.split()]

def can_make_test_value(test_value, nums):
    """Check if test value can be made with any combination of operators."""
    num_operators_needed = len(nums) - 1
    operator_combinations = generate_operator_combinations(num_operators_needed)
    
    for operators in operator_combinations:
        if evaluate_expression(nums, operators) == test_value:
            return True
    return False

def main():
    total = 0
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            test_value, nums = parse_line(line)
            if can_make_test_value(test_value, nums):
                total += test_value
    print(f"Total calibration value: {total}")

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------
