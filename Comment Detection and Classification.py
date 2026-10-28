import re

def analyze_c_comments(file_path):
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
    except FileNotFoundError:
        print(f"Error: Target file '{file_path}' could not be opened.")
        return []

    # Combined Regex Pattern for Single Line and Multi-Line Comments
    comment_pattern = re.compile(r'(//.*)|(/\*[\s\S]*?\*/)')
    extracted_comments = []

    for match in comment_pattern.finditer(source_code):
        comment_text = match.group()
        if comment_text.startswith('//'):
            comment_type = 'Single-line'
        else:
            comment_type = 'Multi-line'
        extracted_comments.append((comment_text, comment_type))

    return extracted_comments

# Demonstration Execution
if __name__ == "__main__":
    path = input("Enter path to C file: ").strip()
    results = analyze_c_comments(path)

    print("\nExtraction & Classification Results:")
    print("-" * 50)
    for text, c_type in results:
        # Clean formatting for clean print
        formatted_text = text.replace('\n', ' ')
        print(f"[{c_type}] -> {formatted_text}")