import re

# Standard C Reserved Keywords
C_KEYWORDS = {
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "inline", "int", "long", "register", "restrict", "return", "short",
    "signed", "sizeof", "static", "struct", "switch", "typedef", "union",
    "unsigned", "void", "volatile", "while"
}

def extract_c_identifiers(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []

    # 1. Remove multi-line comments (/* */)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # 2. Remove single-line comments (// ...)
    content = re.sub(r'//.*', '', content)
    # 3. Strip string literals ("...") and character constants ('.')
    content = re.sub(r'"([^"\\]|\\.)*"', '', content)
    content = re.sub(r"'([^'\\]|\\.)*'", '', content)

    # 4. Extract candidates matching C identifier syntax
    candidates = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', content)

    # 5. Filter out reserved C keywords and deduplicate
    unique_identifiers = set(candidates) - C_KEYWORDS

    return sorted(list(unique_identifiers))

if __name__ == "__main__":
    file_path = input("Enter C source file path: ").strip()
    identifiers = extract_c_identifiers(file_path)

    print("\nExtracted User-Defined Identifiers:")
    for ident in identifiers:
        print(f"  {ident}")