In Python, lists are mutable, meaning their contents can be changed in place.
When a list is passed to a function, the function receives a reference to the same list object in memory, not a copy.
When we do `data[j] = data[j] * factor`, the new value is stored back into the same index of the list.
Even though numbers are immutable, the list itself is mutable, and modifying its elements updates the original list in place. That’s why the caller's list is affected.
