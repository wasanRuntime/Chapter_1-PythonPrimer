"""
C-1.14 Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd
"""
def has_odd_product_pair(seq):
    odd_count = sum(1 for i in seq if i%2 == 1)
    return odd_count >= 2 
data = [5, 8, 3, 2, 9]
print(has_odd_product_pair(data))
