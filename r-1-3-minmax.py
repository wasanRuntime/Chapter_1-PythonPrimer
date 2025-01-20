"""
R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution
"""
def minmax(data):
    min = data[0]
    max = data[0]
    x = []
    for i in range(len(data)):
        if max < data[i]:
            max = data[i]
        if min > data[i]:
            min = data[i]
    #x.append(min)
    #x = x.append(max)
    x = min, max
    return x
data = (2, 3, 20, 100, 5, 6, 80, 23)
print(minmax(data))
