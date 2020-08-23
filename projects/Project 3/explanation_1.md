## Square Root of an Integer

We're looking for the largest number that when squared, results in a number that is not bigger than the input number.

We could naively start at 1, square it, compare to the input and increment until we exceed or equal the input number. This would be an O(n) algorithm, but we can do better with a binary search.

To implement the binary search, we define the search range