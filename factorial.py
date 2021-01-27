# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n):
    if type(n) != int:
        raise TypeError("Value must be a positive integer")
    if n < 1:
        raise ValueError("Value mube be greater than 0")
    if (n == 1):
        return 1
    else:
        return n * factorial(n-1)
    pass

print(factorial(5))
# => 120