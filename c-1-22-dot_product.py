"""
C-1.22 Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.
"""
def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError('length of a is not equal to length of b')
    return [a[i] * b[i] for i in range(len(a))]

a = [1,2,3,4,5,6]
b = [1, 2, 3, 4, 5]
try:
    print(dot_product(a, b))
except ValueError as e:
    print(e)

