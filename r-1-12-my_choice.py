"""
R-1.12 Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""
import random

def my_choice(data):
    if not data:
        raise ValueError('Cnnot choose from an empy sequesnce')
    random_index = random.randrange(len(data))
    return data[random_index]

sample_list = [10, 20, 30, 40, 50]
print(my_choice(sample_list))
