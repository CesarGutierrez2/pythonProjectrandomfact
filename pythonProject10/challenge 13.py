import re
# i use regular expressions to validate the password
# i make ensure that the password contains atleats one lowercase letter in the first group
# then i make sure theres atleast one upper case letter in the second group
# i also use the (?=.*\d) to ensure that the password contains atleast one number
# i also ensure that there is atleast one special character in the password
# lastly i make sure the total length of the password is 8 letters or longer
password_validate = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%*!]).{8,}$'

# i ask for the user to enter their password for validation
enter_password = input("Please enter a password: ")

# in this line i use the re.match function to match what the user entered
# with the standards i wrote in the password_validate variable
if re.match(password_validate, enter_password):
    print("This is a valid password")

# if the password does not meet standards, this else function is called
else:
    print("This is not a valid password")
