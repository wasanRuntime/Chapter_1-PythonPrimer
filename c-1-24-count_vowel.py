"""
C-1.24 Write a short Python function that counts the number of vowels in a given
character string.
"""
def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    return sum(1 for i in sentence if i in vowels)
text = "Hello, World!"
print(count_vowels(text))
