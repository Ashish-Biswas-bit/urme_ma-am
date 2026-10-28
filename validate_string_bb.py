import re

def validate_string_bb(input_string):
    # Regex pattern: checks if 'bb' exists anywhere matching full string structure
    pattern = r".*bb.*"
    
    if re.fullmatch(pattern, input_string):
        return True
    else:
        return False

# Driver code to test the function
if __name__ == "__main__":
    test_strings = ["abb", "aabb", "bba", "aaba", "ab", "b", ""]
    
    for s in test_strings:
        result = validate_string_bb(s)
        print(f"String: '{s}' -> Matches pattern: {result}")