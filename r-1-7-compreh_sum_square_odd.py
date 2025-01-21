"""
R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function.
"""
def comp_odd(n):
    if n >= 0:
        return sum(i**2 for i in range(1, n) if i%2 != 0)
    else:
        return 'number is not positive'
print(comp_odd(8))
