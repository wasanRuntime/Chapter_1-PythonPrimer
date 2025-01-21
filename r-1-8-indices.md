If a string s has length `n`, and we use a negative index `k` (where `-n ≤ k < 0`), the equivalent non-negative index `j` can be found using the formula:

`𝑗 = 𝑛 + 𝑘`
`j=n+k`
*Explanation:*

In Python, negative indices count from the end of the sequence.
`s[-1]` refers to the last character of `s`, which is `s[n-1]`.
`s[-2]` refers to the second-to-last character, which is `s[n-2]`, and so on.
The general formula to convert a negative index `k` to a non-negative index `j` is `j = n + k`.
