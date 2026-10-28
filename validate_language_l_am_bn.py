import re

def validate_language_ab(input_string):
    # Regex pattern: ^a+b+$ ensures one or more 'a's followed by one or more 'b's exclusively
    pattern = r"^a+b+$"
    
    if re.match(pattern, input_string):
        return True
    else:
        return False

# Driver code to test the function
if __name__ == "__main__":
    test_strings = ["ab", "aab", "abb", "aaabbb", "a", "b", "ba", ""]
    
    for s in test_strings:
        result = validate_language_ab(s)
        print(f"String: '{s}' -> Valid in L: {result}")