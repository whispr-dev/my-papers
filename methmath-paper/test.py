import itertools

def mpa_n(props):
    """Generalized MPA for n propositions: all must be identical AND true."""
    if not props:
        return False
    first = props[0]
    return all(p == first for p in props) and first

# Test for n=2
truths2 = list(itertools.product([True, False], repeat=2))
fixed2 = [t for t in truths2 if mpa_n(t)]
print("n=2 fixed points:", fixed2)

# Test for n=3
truths3 = list(itertools.product([True, False], repeat=3))
fixed3 = [t for t in truths3 if mpa_n(t)]
print("n=3 fixed points:", fixed3)

# Corrected iterative revision-style approximation for MPA
def iterate_mpa(initial, steps=5):
    """Iterative revision-style approximation.
    Starts with a list of bools. At each step the joint truth value
    (all True?) is propagated to every component. Demonstrates:
    - Mixed start → collapses to all-False
    - All-True start → stable fixed point"""
    current = list(initial)  # ensure mutable copy
    history = [current[:]]
    for _ in range(steps):
        all_true = all(current)
        current = [all_true] * len(current)  # reinforce jointly
        history.append(current[:])
    return history

print("Iterative example starting [True, False]:", iterate_mpa([True, False]))
print("Iterative example starting [True, True]:", iterate_mpa([True, True]))