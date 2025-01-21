`for val in data:` iterates over each element by value, meaning `val` is just a reference to each element, not a direct reference to the list itself.

The statement `val = factor` only reassigns the local variable `val` to `factor`, but does not modify the actual list.
This only affects val inside the loop, leaving data unchanged.

*Correct Way to Modify the List*

```python
def scale(data, factor):
    for i in range(len(data)):  # Iterate using indices
        data[i] *= factor  # Modify the list in place

nums = [1, 2, 3, 4, 5]
scale(nums, 3)
print(nums)  # Output: [3, 6, 9, 12, 15] (List modified correctly)

`

