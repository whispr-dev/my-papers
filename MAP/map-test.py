import itertools

def mpa(a, b):
    """Mutual Palindromic Affirmation operator as defined in the paper.
    Returns True only when A and B are identical AND both true."""
    return (a == b) and (a and b)

# Generate all 4 possible truth assignments for (A, B)
truths = list(itertools.product([True, False], repeat=2))

# Find fixed points under the MPA operator
fixed_points = [(a, b) for a, b in truths if mpa(a, b)]

print("Fixed points:", fixed_points)