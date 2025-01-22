"""
C-1.25 Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this function would return
"Lets try Mike".
"""
import string

def remove_punctuation(s):
    return ''.join(char for char in s if char not in string.punctuation)

            
text = "Let's try, Mike"
print(remove_punctuation(text))
    
