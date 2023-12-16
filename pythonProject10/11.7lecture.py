# module 12 lecture

# Recursions:

# Anything can be solved with recursion can be solved iteratively

# Iteration is usually more efficient; however, the problem could be easier to solve with recursion

# Recursion continuously breaks a problem down into smaller and smaller parts

# A function that calls itself is called a recursive function

# The recursive function must have some means to control the number of times it's repeated

# The number of times the function calls itself is called the 'depth of recursion'

# Recursion uses the stack and pushes and pops values. This can also cause stack overflows. The stack is a LIFO

# complexity analysis - Big-O Notation
# millisecond = 1/1000 of a second, ms

# Base case (when to stop)
# work toward base case (this is where we make the problem simpler)
# recursive call (call ourselves)

# example 1
"""


def factorial(n):
    # base case == 0, because 0! is 1. So this is the only case where the problem can be solved without recursion

    if n == 0:  # what happens if i make this 1?
        return 1
    # recursive case, where we need to keep breaking the problem down into smaller sets
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    result = factorial(number)
    print(result)
"""

"""
def recursion(n):
    if n <= 0:
        return
    display_asterisks(n - 1)
    print('*' * n)


n = 5
display_asterisks(n)
"""


def recur(n):
    if n == 1:
        print("*")
    else:
        recur(n - 1)
        print("*" * n)


n = 5
recur(n)
