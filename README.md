# Chapter 1 Python Primer
`Chapter one of Data Structure and Algorithm`

### Reinforcement

R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
[solution](r-1-1-multiple.py)

R-1.2 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
[solution](r-1-2-even.py)

R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution
[solution](r-1-3-minmax.py)

R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
[solution](r-1-4-sum_of_squares.py)

R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying on Python’s comprehension syntax and the built-in sum function.
[solution](r-1-5-sqaure_sum_funct.py)

R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
[solution](r-1-6-sum_square_odd.py)

R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function.
[solution](r-1-7-compreh_sum_square_odd.py)

R-1.8 Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
[solution](r-1-8-indices.md)

R-1.9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
[solution](r-1-9-range_constructor.md)

R-1.10 What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
[solution](r-1-10-range_construtor_2.md)

R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
[solution](r-1-11-list_compr.py)

R-1.12 Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
[Solution](r-1-12-my_choice.py)

### Creativity

C-1.13 Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing
[Solution](c-1-13-reversing.py)

C-1.14 Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd
[solution](c-1-14-has_odd_product_pair.py)

C-1.15 Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
[solution](c-1-15-are_all_numbers_distinct.py)

C-1.16 In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] = factor. We have discussed that numeric
types are immutable, and that use of the = operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?
[solution](c-1-16-mutation.md)
