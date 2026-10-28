import re

def check_start_ab(input_string):
    # Regex pattern: '^' asserts the start of the string, followed by 'ab'
    pattern = r"^ab"
    
    # re.match checks for a match only at the beginning of the string
    if re.match(pattern, input_string):
        return True
    else:
        return False

# Driver code to test the function
if __name__ == "__main__":
    test_strings = ["abcdef", "abs", "bab", "ab", "a", ""]
    
    for s in test_strings:
        result = check_start_ab(s)
        print(f"String: '{s}' -> Starts with 'ab': {result}")