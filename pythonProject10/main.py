# more recursions
# recursive approach
"""
def walk(steps):
    if steps == 0:
        return
    walk(steps - 1)
    print(f"You take step", {steps})


walk(100)
"""

"""
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(8))
"""


def sum_of_numbers(n): #defines a function called sum_of_numbers that takes on an argument n
    if n == 1: #this is the base case that'll stop the recursion
        return 1
    else:
        return n + sum_of_numbers(n - 1) #this is the recursive call to the sum_of_numbers function
    # it keeps adding n to the sum of numbers from 1 to n-1


number = int(input("Enter a number: ")) #i ask the user to enter a number
result = sum_of_numbers(number) #this calculates the sum of numbers from 1 to the user's input
print(sum_of_numbers(number))#this prints the sum of the numbers that the user entered
