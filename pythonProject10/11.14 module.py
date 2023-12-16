# module 13 - Regular expressions!
# teacher lecture:

# checking to see if a phone number is valid

"""
def phoneNumber():
    while True:

        try:
         phone_number = input("Enter a phone number in the following format: xxx-xxx-xxx: ")

        low_range = True
        mid_range = True
        high_range = True

        length = len(phone_number)
        for i in range(0, 3)
            if not phone_number[i].isdecimal():
                low_range = False
            for i in range(4, 7)
                if not phone_number[i].isdecimal():
                    mid_range = False
            for i in range(8, 11)
                if not phone_number[i].isdecimal():
                    high_range = False

        if phone_number[3] == '-' and phone_number[7] == '-' and length ==

"""
# regular expressions are used to match patterns. You have used them before when searching in a pdf or word doc
import re

#build a pattern
pattern = r"^[a-Z]{1}+:[a-z]{1}\\+[a-z]{1}$"

#creating a regex object using the raw string
file_path = input("Please enter a valid file path: ")

if re.match(pattern, file_path):
    print("This is a valid file path")

else:
    print("This is not a valid file path")


pattern = r"^([A-z]+:+\\)([A-z0-9]+\\)*([A-z0-9]+.txt|.zip|.pdf)$"
#creating a regex object using the raw string. Do we need to have that many repititions if we already use the * ?,
#no so lets remove them

file_path_2 = input("Enter the file path to test if it's valid: ")

if re.match():




# self-taught below:
"""
import re

names = ['Finn Binderballe',
         'Geir Anders Berge',
         'Happy coding Robot',
         'Ron Cromberge',
         'sohil']
# find people with first and last names only
"""
"""
regex = '^\w+ \w+$'
for name in names:
    result = re.search(regex, name)
    if result:
        print(result)
"""
# search for word characters sequence starting with capital C
"""
regex = 'C\w*'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)
        print(match.start())
        print(match.end())
  """
"""
# return a list containing every occurence of "ai"
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
"""
