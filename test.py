"""
lhs = input("Enter your production rule (LHS): ")
rhs= input("Enter your production rule (use |): " ).split("|")

alpha = [r.strip()[len(lhs):] for r in rhs if r.strip().startswith(lhs)]
beta = [r.strip() for r in rhs if not r.strip().startswith(lhs)]

if alpha:
    print("found left recursion")

    if beta:
        print(lhs, "->", " | ".join(b+ lhs + "'" for b in beta))
        print(lhs + "' ->", " | ".join(a + lhs + "'" for a in alpha), "| epsilon")
    else: 
        print("Cannot eliminate: no beta production")
else:
    print("No left recursion found")

"""

lhs = input("Enter LHS: ")
rhs= [r.strip() for r in input("Enter RHS (use |): ").split("|")]

prefix = rhs[0]
for r in rhs[1:]:
    while prefix and not r.startswith(prefix):
        prefix = prefix[:-1]

if prefix: 
    print("found left factoring")
    print(lhs, "->", prefix + lhs + "'")
    print(lhs + "' ->", " | ".join(r[len(prefix):] or "epsilon" for r in rhs))

else:
    print("No left factoring found")
