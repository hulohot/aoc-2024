# PROMPT
# -----------------------------------------------------------------------------
# It seems like the goal of the program is just to multiply some numbers.
# It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers.
# For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024.
# Similarly, mul(123,4) would multiply 123 by 4.

# However, because the program's memory has been corrupted, there are also many invalid
# characters that should be ignored, even if they look like part of a mul instruction.
# Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

# As you scan through the corrupted memory, you notice that some of the conditional
# statements are also still intact. If you handle some of the uncorrupted conditional
# statements in the program, you might be able to get an even more accurate result.

# There are two new instructions you'll need to handle:

# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.
# Only the most recent do() or don't() instruction applies. At the beginning of the 
# program, mul instructions are enabled.
# -----------------------------------------------------------------------------


# SOLUTION
# -----------------------------------------------------------------------------

def parse_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def find_valid_multiplications(text):
    result = 0
    i = 0
    enabled = True
    while i < len(text):
        # Check for do/don't instructions
        if text[i:i+3] == 'do(' and i+4 < len(text):
            if text[i+3] == ')':
                enabled = True
                i += 4
                continue
        elif text[i:i+6] == "don't(" and i+7 < len(text):
            if text[i+6] == ')':
                enabled = False
                i += 7
                continue
                
        # Process mul instructions only if enabled
        if enabled and text[i:i+4] == 'mul(' and i+4 < len(text):
            # Found potential mul instruction
            j = i + 4
            num1 = ''
            num2 = ''
            # Get first number
            while j < len(text) and text[j].isdigit():
                num1 += text[j]
                j += 1
            # Check for comma
            if j < len(text) and text[j] == ',' and len(num1) > 0 and len(num1) <= 3:
                j += 1
                # Get second number
                while j < len(text) and text[j].isdigit():
                    num2 += text[j]
                    j += 1
                # Check for closing parenthesis
                if j < len(text) and text[j] == ')' and len(num2) > 0 and len(num2) <= 3:
                    result += int(num1) * int(num2)
        i += 1
    return result

def main():
    # input_text = parse_input('test.txt')
    input_text = parse_input('input.txt')
    result = find_valid_multiplications(input_text)
    print(f"Sum of all valid multiplications: {result}")

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------
