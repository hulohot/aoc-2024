# PROMPT
# -----------------------------------------------------------------------------
# Building on part 1, the Problem Dampener is a reactor-mounted module that lets 
# the reactor safety systems tolerate a single bad level in what would otherwise 
# be a safe report. It's like the bad level never happened!
#
# Now, the same rules apply as before, except if removing a single level from an 
# unsafe report would make it safe, the report instead counts as safe.
#
# Examples:
# - 7 6 4 2 1: Safe without removing any level.
# - 1 2 7 8 9: Unsafe regardless of which level is removed.
# - 9 7 6 2 1: Unsafe regardless of which level is removed.
# - 1 3 2 4 5: Safe by removing the second level, 3.
# - 8 6 4 4 1: Safe by removing the third level, 4.
# - 1 3 6 7 9: Safe without removing any level.
# -----------------------------------------------------------------------------


# SOLUTION
# -----------------------------------------------------------------------------

def is_safe(report):
    # Run the normal check first
    if (all(report[i] < report[i+1] for i in range(len(report)-1)) or 
        all(report[i] > report[i+1] for i in range(len(report)-1))) and \
       all(abs(report[i] - report[i+1]) >= 1 and abs(report[i] - report[i+1]) <= 3 
           for i in range(len(report)-1)):
        return True
    
    # Now check if removing any single level makes the report safe
    if len(report) < 3:
        return False
    
    # Create a list of lists where one level is removed
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if (all(new_report[i] < new_report[i+1] for i in range(len(new_report)-1)) or 
            all(new_report[i] > new_report[i+1] for i in range(len(new_report)-1))) and \
           all(abs(new_report[i] - new_report[i+1]) >= 1 and abs(new_report[i] - new_report[i+1]) <= 3 
               for i in range(len(new_report)-1)):
            return True
    
    return False

# Read the input into a list of lists
with open('input.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file]

# Count the number of safe reports, with the Problem Dampener
safe_reports = sum(1 for report in reports if is_safe(report))

print(safe_reports)

# -----------------------------------------------------------------------------