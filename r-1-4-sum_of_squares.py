"""
R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""
def sum_of_square(n):
    if n > 0:
        sum_of_s = 0
        for i in range(1, n):
            #s = i ** 2
            sum_of_s += i ** 2

    return sum_of_s
print(sum_of_square(4))

