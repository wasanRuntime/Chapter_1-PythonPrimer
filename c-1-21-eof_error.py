"""
C-1.21 Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""
def read_and_reverse():
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        for line in reversed(lines):
            print(line)

read_and_reverse()
