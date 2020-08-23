import math


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    return math.sqrt(number)


# Tests
assert 3 == sqrt(9)
assert 0 == sqrt(0)
assert 4 == sqrt(16)
assert 1 == sqrt(1)
assert 5 == sqrt(27)


# print("Pass" if (None == sqrt(None)) else "Fail")#Null input

print("Pass" if (-1 == sqrt(-27)) else "Fail")  # Negative input test

print("Pass" if (0 == sqrt(0)) else "Fail")  # Zero input
print("Pass" if (1 == sqrt(1)) else "Fail")  # 1 input
print("Pass" if (1 == sqrt(2)) else "Fail")  # 2 input
print("Pass" if (1 == sqrt(3)) else "Fail")  # 3 input
print("Pass" if (2 == sqrt(4)) else "Fail")  # Negative input

print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (3 == sqrt(15)) else "Fail")

print("Pass" if (3 == sqrt(9)) else "Fail")

print("Pass" if (4 == sqrt(16)) else "Fail")

print("Pass" if (24 == sqrt(624)) else "Fail")
print("Pass" if (31 == sqrt(1000)) else "Fail")

# Large Number input
print("Pass" if (166564950 == sqrt(27743882883774747)) else "Fail")
