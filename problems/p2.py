"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
    By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.
"""


def problem2(max_number):
    x = z = total = 0
    y = 1
    while z <= max_number:
        z = x + y
        x = y
        y = z
        if z % 2 == 0:
            total += z

    return total


