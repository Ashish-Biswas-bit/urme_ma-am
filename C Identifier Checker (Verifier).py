# Standard C Language Reserved Keywords Set
C_KEYWORDS = {
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "inline", "int", "long", "register", "restrict", "return", "short",
    "signed", "sizeof", "static", "struct", "switch", "typedef", "union",
    "unsigned", "void", "volatile", "while"
}

def is_alpha(symbol):
    """Check if character is in range a-z or A-Z."""
    return ('a' <= symbol <= 'z') or ('A' <= symbol <= 'Z')

def is_digit(symbol):
    """Check if character is in range 0-9."""
    return '0' <= symbol <= '9'

def validate_identifier_manual(token):
    """Manual custom parsing approach."""
    if not token or token in C_KEYWORDS:
        return False

    # Verify starting symbol
    first = token[0]
    if not (is_alpha(first) or first == '_'):
        return False

    # Verify trailing symbols
    for char in token[1:]:
        if not (is_alpha(char) or is_digit(char) or char == '_'):
            return False

    return True

def validate_identifier_builtin(token):
    """Python native method implementation."""
    return token.isidentifier() and (token not in C_KEYWORDS)

# Demonstration / Execution
if __name__ == "__main__":
    user_input = input("Enter candidate identifier: ").strip()

    # Primary evaluation
    if validate_identifier_manual(user_input):
        print(f"'{user_input}' is a VALID C identifier.")
    else:
        print(f"'{user_input}' is NOT a valid C identifier.")