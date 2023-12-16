# chapter 6, 7, 8 most time on, also chapter 2 and so on
# main function and another function
# strings, string manipulation, lists
# list, grab the number

"""
Main function
function called greetings 1st
call greetings from main 2nd
print hello world in greetings in first function of greetings

create a variable that stores last name as a string line:17
"""

"""
def loops(n):
    for i in range(0, n):
        print("hello world")
        print(i)
    choice = input("DO you want to play a game?: ").lower()
    while choice == "yes":
        print("Hello World")
        choice = input("DO you want to play a game?: ").lower()
    while True:
        if choice == "no":
            break
        else:
            print("Hello World")
    # can only sort in a list with the same data type
    my_list = [1, 45, 5.5, "Hello"]
    my_list2 = [5, -4, 0, 50, 2]

    my_list.index("Hello World")
    print(my_list[3])

    my_tuple = (1, 4, 5)
    
    # more like the final
    
    my_string = "12hello3"
    empty_list = []
    for char in my_string:
        if char.isnumeric():
            empty_list.append(char)
                print(empty_list)


def main():
    num = int(input("Enter a number:"))
    loops(num)


if __name__ == "__main__":
    main()

"""

# write a function that takes a list of words and returns a new list with
# the words sorted alphabetically
"""
def sort_words(word_list):
    return sorted(word_list)


words = ["apple", "banana", "orange", "grape", "kiwi"]
sorted_words = sort_words(words)
print(sorted_words)

if __name__ == "__main__":
    sort_words(words)
"""

"""
def my_string():
    new_string = "12hello3"
    dif_string = " "
    for char in new_string:
        if char.isnumeric():
            dif_string = char
            print(dif_string)


if __name__ == "__main__":
    my_string()
    
"""

"""
# creat a code where you take a string and put only the numerical 
# characters in the new list 
def poop():
    my_string = "12hello3"
    empty_list = []
    for char in my_string:
        if char.isnumeric():
            empty_list.append(char)
            print(empty_list)


if __name__ == "__main__":
    poop()
"""

# if you want to get the last character in a list use the -1 index
"""
my_list = [10, 20, 30, 40]
print(my_list[-1], my_list[-2], my_list[-3], my_list[-4])
"""


def sort_words(word_list):
    return sorted(words)


words = ["banana", "orange", "grape", "kiwi"]
sorted_words = sort_words(words)
print(sorted_words)
if __name__ == "__main__":
    sort_words(words)

