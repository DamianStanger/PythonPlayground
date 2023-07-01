import re

def apply_operator(accumulator, numbers, operator):
    if accumulator != None:
        numbers.insert(0, accumulator)
    
    if operator == '+':
        result = sum(numbers)
    elif operator == '-':
        result = numbers[0] - sum(numbers[1:])
    elif operator == '*':
        result = 1
        for num in numbers:
            result *= num
    elif operator == '/':
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
    else:
        raise ValueError("Invalid operator")

    return result

def calculate(tokens):
    result = None
    for chunk in tokens:
        result = apply_operator(result, chunk[0], chunk[1])
    return result


def tokenise(input_string):
    chunk_pattern = r'[^-+/*]+[-+/*]'
    chunks = re.findall(chunk_pattern, input_string)
    tokens = []
    for chunk in chunks:
        split_parts = chunk.split()
        numbers = [int(num) for num in split_parts[:-1]]
        operator = split_parts[-1]
        tokens.append((numbers, operator))
    return tokens

def run_test_case(input_string, expected_output):
    tokens = tokenise(input_string)
    output = calculate(tokens)
    return output


def run_test_cases(cases):
    for idx, (test_case, expected_output) in enumerate(cases, start=1):
        print(f"Test Case ({idx})   {test_case}")
        output = run_test_case(test_case, expected_output)
        if output == expected_output:
            print(f"Test Case {idx}: Passed, expected {expected_output}, got {output}")
        else:
            print(f"Test Case {idx}: failed, expected {expected_output}, got {output}")    

valid_test_cases = [
    ("1 2 3 +", 6),
    ("6 2 3 -", 1),
    ("2 2 3 *", 12),
    ("12 3 2 /", 2),
    ("1 2 3 + 4 5 *", 120),
    ("10 5 - 2 2 /", 1.25),
    ("100 20 + 30 10 -", 80),
    ("4 5 2 3 * 4 5 /", 6),
    ("1 2 3 4 5 +", 15),
    ("1 1 + 1 * 1 / 1 -", 1)
]

invalid_test_cases = [
    ("", None),
    ("a", None),
    ("6", None),
    ("+ 1 1", None),
    ("12 3 2", None),
    ("1 2 ^", None)
]

run_test_cases(valid_test_cases + invalid_test_cases) 