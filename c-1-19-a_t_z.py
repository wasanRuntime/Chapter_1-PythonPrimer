"""
"""
def a_to_z():
    result = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    return result
print(a_to_z())
