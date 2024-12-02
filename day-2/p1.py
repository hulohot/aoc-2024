# Read the input into a list of tuples
# The unusual data (your puzzle input) consists of many reports, `one report per line`.
# Each report is a list of numbers called levels that are separated by spaces

# Read the input into a list of lists
with open('input.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file]

# print(reports)

# A report only counts as safe if both of the following are true:
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.

# Count the number of safe reports
safe_reports = sum(1 for report in reports if (all(report[i] < report[i+1] for i in range(len(report)-1)) or all(report[i] > report[i+1] for i in range(len(report)-1))) and all(abs(report[i] - report[i+1]) >= 1 and abs(report[i] - report[i+1]) <= 3 for i in range(len(report)-1)))

print(safe_reports)