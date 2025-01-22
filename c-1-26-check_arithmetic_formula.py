"""
C-1.26 Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”
"""
def check_arithmetic_formula(a, b, c):
    """Checks if the given integers a, b, and c form a valid arithmetic equation."""
    if a + b == c:
        return f"{a} + {b} = {c}"
    elif a - b == c:
        return f"{a} - {b} = {c}"
    elif a * b == c:
        return f"{a} * {b} = {c}"
    elif b != 0 and a / b == c:
        return f"{a} / {b} = {c}"
    else:
        return "No valid arithmetic equation found."

# Taking input from the user
a, b, c = map(int, input("Enter three integers (a b c): ").split())

# Checking the arithmetic formula
print(check_arithmetic_formula(a, b, c))

