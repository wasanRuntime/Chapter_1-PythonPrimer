"""
C-1.23 Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!”
"""
def edit_list(data, index, value):
    try:
        data[index] = value
        return data
    except IndexError:
        return ("Don’t try buffer overflow attacks in Python!")
data = [2,3,1,7,6,9]
edited = edit_list(data, 20, 100)
print(edited)
