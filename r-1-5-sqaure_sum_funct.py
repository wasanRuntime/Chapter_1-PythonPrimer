"""
R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying on Python’s comprehension syntax and the built-in sum function.
"""
def sqaure_sum_funct(n):
    if n >= 0:
      return sum( i**2 for i in range(1, n))
            
    else:
      return 'Ensure that the number entered is positive'
print(sqaure_sum_funct(4))
