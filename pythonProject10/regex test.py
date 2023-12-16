"""
import re

# pattern = r"^[0-9]{3}-[0-9]{3}-[0-9]{4}$"
# or
pattern = r"^(\([0-9]{3}+\)+\s*)([0-9]{3}+-)([0-9]{4}$)"  # this line adds the parentheses in the area code of
# number & adds space between area code and first numbers
phone_number = input("Please enter a phone number: ")

if re.match(pattern, phone_number):
    print("This is a valid phone number")

else:
    print("Invalid phone number")
"""
import re
password = r"^([a-fA-F0-9]+{7}[@#$%*!]+{1}+$"
enter_password = input("Please enter a password: ")

if re.match(password, enter_password):
    print("This is a valid password")

else:
    print("This is not a valid password")


# new recursion problem
"""
def recur_sum(n):
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    # recursive function
    else:
        return n + recur_sum(n-1)
"""

# more regular expression practice


