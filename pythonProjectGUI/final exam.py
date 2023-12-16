
#given string
challenge_string = "2 Happy 60 To End 7 This 8 Semester 54"
#making sure i want my word to be an integer and checking the
# string if there is a word that's a digit, take it from there
# and put it in the list
integers = [int(word) for word in challenge_string.split() if word.isdigit()]
# sorting out the order i want the integers to be so i put
# reverse to being true
integers.sort(reverse=True)
# prints out the list of the integers i want in reverse order
print(integers)


