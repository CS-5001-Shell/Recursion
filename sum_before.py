"""
Implement the following recursive Python function sum_before that takes as a parameter a list of integers and returns True if there is a number in the list that equals the sum of all numbers before it in the list and False otherwise.

For full credit your solution may not use any loops.

[1, 2, 3, 4] -> True
[1, 2, 2, 2] -> False
[] -> False
[0] -> True
"""


def sum_before(numbers: list[int], sum=0) -> bool:
    """Returns True if any value in the list is the sum of all numbers before it
    in the list and False otherwise.
    """
    pass