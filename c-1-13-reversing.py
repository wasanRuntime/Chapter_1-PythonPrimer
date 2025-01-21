"""
C-1.13 Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing

FUNCTION ReverseList(arr, n)
    LEFT ← 0
    RIGHT ← n - 1
    WHILE LEFT < RIGHT DO
        TEMP ← arr[LEFT]
        arr[LEFT] ← arr[RIGHT]
        arr[RIGHT] ← TEMP
        LEFT ← LEFT + 1
        RIGHT ← RIGHT - 1
    END WHILE
    RETURN arr
END FUNCTION

"""

def reverse_list(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left = left + 1
        right = right -1
    return arr

# Example Usage
nums = [1, 2, 3, 4, 5]
print(reverse_list(nums))  # Output: [5, 4, 3, 2, 1]



