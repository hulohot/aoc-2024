# PROMPT
# -----------------------------------------------------------------------------

# Safety protocols clearly indicate that new pages for the safety manuals must be 
# printed in a very specific order. The notation X|Y means that if both page 
# number X and page number Y are to be produced as part of an update, page 
# number X must be printed at some point before page number Y.

# The Elf has for you both the page ordering rules and the pages to produce in 
# each update (your puzzle input), but can't figure out whether each update 
# has the pages in the right order.

# For example:

# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47
# The first section specifies the page ordering rules, one per line. 
# The first rule, 47|53, means that if an update includes both page 
# number 47 and page number 53, then page number 47 must be printed at some 
# point before page number 53. (47 doesn't necessarily need to be immediately 
# before 53; other pages are allowed to be between them.)

# The second section specifies the page numbers of each update. Because most 
# safety manuals are different, the pages needed in the updates are different 
# too. The first update, 75,47,61,53,29, means that the update consists of 
# page numbers 75, 47, 61, 53, and 29.

# To get the printers going as soon as possible, start by identifying which 
# updates are already in the right order.

# In the above example, the first update (75,47,61,53,29) is in the right order:

# 75 is correctly first because there are rules that put each other page after it: 
# 75|47, 75|61, 75|53, and 75|29.
# 47 is correctly second because 75 must be before it (75|47) and every 
# other page must be after it according to 47|61, 47|53, and 47|29.
# 61 is correctly in the middle because 75 and 47 are before it (75|61 and 47|61) 
# and 53 and 29 are after it (61|53 and 61|29).
# 53 is correctly fourth because it is before page number 29 (53|29).
# 29 is the only page left and so is correctly last.
# Because the first update does not include some page numbers, the ordering 
# rules involving those missing page numbers are ignored.

# The second and third updates are also in the correct order according to the 
# rules. Like the first update, they also do not include every page number, 
# and so only some of the ordering rules apply - within each update, the 
# ordering rules that involve missing page numbers are not used.

# The fourth update, 75,97,47,61,53, is not in the correct order: it would 
# print 75 before 97, which violates the rule 97|75.

# The fifth update, 61,13,29, is also not in the correct order, since it 
# breaks the rule 29|13.

# The last update, 97,13,75,29,47, is not in the correct order due to 
# breaking several rules.

# For some reason, the Elves also need to know the middle page number of each 
# update being printed. Because you are currently only printing the correctly-
# ordered updates, you will need to find the middle page number of each 
# correctly-ordered update. In the above example, the correctly-ordered 
# updates are:

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# These have middle page numbers of 61, 53, and 29 respectively. Adding these 
# page numbers together gives 143.

# While the Elves get to work printing the correctly-ordered updates, you have 
# a little time to fix the rest of them.

# For each of the incorrectly-ordered updates, use the page ordering rules to 
# put the page numbers in the right order. For the above example, here are the 
# three incorrectly-ordered updates and their correct orderings:

# 75,97,47,61,53 becomes 97,75,47,61,53.
# 61,13,29 becomes 61,29,13.
# 97,13,75,29,47 becomes 97,75,47,29,13.

# After taking only the incorrectly-ordered updates and ordering them correctly, 
# their middle page numbers are 47, 29, and 47. Adding these together produces 123.

# -----------------------------------------------------------------------------


# SOLUTION
# -----------------------------------------------------------------------------

def parse_input(filename):
    """Parse input file into rules and updates."""
    with open(filename) as f:
        content = f.read().strip().split('\n\n')
    
    # Parse rules into a set of tuples (before, after)
    rules = set()
    for line in content[0].split('\n'):
        before, after = map(int, line.split('|'))
        rules.add((before, after))
    
    # Parse updates into lists of integers
    updates = []
    for line in content[1].split('\n'):
        update = list(map(int, line.split(',')))
        updates.append(update)
    
    return rules, updates

def is_valid_order(update, rules):
    """Check if an update follows all applicable rules."""
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            x, y = update[i], update[j]
            if (y, x) in rules:
                return False
    return True

def get_middle_number(update):
    """Get the middle number of an update."""
    return update[len(update) // 2]

def sort_update(update, rules):
    """Sort the update according to the rules using topological sort."""
    # Build adjacency list
    graph = {x: set() for x in update}
    for x in update:
        for y in update:
            if x != y and (x, y) in rules:
                graph[x].add(y)
    
    # Calculate in-degrees
    in_degree = {x: 0 for x in update}
    for x in graph:
        for y in graph[x]:
            in_degree[y] += 1
    
    # Topological sort using Kahn's algorithm
    result = []
    queue = [x for x in update if in_degree[x] == 0]
    
    while queue:
        x = queue.pop(0)
        result.append(x)
        
        for y in graph[x]:
            in_degree[y] -= 1
            if in_degree[y] == 0:
                queue.append(y)
    
    return result

def main():
    rules, updates = parse_input('input.txt')
    
    # Find and fix invalid updates
    middle_sum = 0
    for update in updates:
        if not is_valid_order(update, rules):
            fixed_update = sort_update(update, rules)
            middle_num = get_middle_number(fixed_update)
            middle_sum += middle_num
            print(f"Fixed update: {update} -> {fixed_update}, middle number: {middle_num}")
    
    print(f"\nSum of middle numbers of fixed updates: {middle_sum}")

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------
