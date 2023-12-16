# i will first define a function called the sum_of_numbers
# that takes on the argument n
def sum_of_numbers(n):
    if n == 1:  # this is the base case that'll stop the recursion
        return 1
    else:
        return n + sum_of_numbers(n - 1)  # this is the recursive call to the
    # sum_of_numbers function.
    # It keeps adding n to the sum of numbers from 1 to n-1


if __name__ == '__main__':
    number = int(input("Enter a number: ")) # i ask the user to enter a number of their choice
    result = sum_of_numbers(number) # i call the sum_of_numbers function to the number the
    # user chose and storing it in result function
    print(result)
