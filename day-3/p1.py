# PROMPT
# -----------------------------------------------------------------------------
# It seems like the goal of the program is just to multiply some numbers.
# It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers.
# For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024.
# Similarly, mul(123,4) would multiply 123 by 4.

# However, because the program's memory has been corrupted, there are also many invalid
# characters that should be ignored, even if they look like part of a mul instruction.
# Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
# -----------------------------------------------------------------------------


# SOLUTION
# -----------------------------------------------------------------------------

def parse_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def find_valid_multiplications(text):
    result = 0
    i = 0
    while i < len(text):
        if text[i:i+4] == 'mul(' and i+4 < len(text):
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
    input_text = parse_input('input.txt')
    result = find_valid_multiplications(input_text)
    print(f"Sum of all valid multiplications: {result}")

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------
