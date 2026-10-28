lhs = input("Enter LHS: ")
rhs = [r.strip() for r in input("Enter RHS (use |): ").split("|")]

prefix = rhs[0]
for r in rhs[1:]:
    while prefix and not r.startswith(prefix):
        prefix = prefix[:-1]

if prefix:
    print("Left Factoring Found")
    print(lhs, "->", prefix + lhs + "'")
    print(lhs + "' ->", " | ".join(
        r[len(prefix):] or "epsilon" for r in rhs))
else:
    print("No Left Factoring Found")
