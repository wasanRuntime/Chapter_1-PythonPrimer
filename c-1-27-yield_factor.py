"""
C-1.27 In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementations, from page 41, was the most efficient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance advantages.
"""
def factors(n):
    """Generate factors of n in increasing order."""
    small_factors = []
    large_factors = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            yield i  # Yield small factor
            if i != n // i:
                large_factors.append(n // i)  # Store large factor

    # Yield large factors in order
    for factor in reversed(large_factors):
        yield factor

# Example usage
n = 100
print(list(factors(n)))  # Output: [1, 2, 4, 5, 10, 20, 25, 50, 100]

