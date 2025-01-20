"""
R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.

"""
def sum_of_square(n):
    if n >= 0:
        sum_of_s = 0
        for i in range(1, n):
            if (i&1) == 1:
                sum_of_s += i ** 2
    else:
       # print('ensure that your number is positive')
        return 'ensure that your number is positive'

    return sum_of_s
print(sum_of_square(8))
