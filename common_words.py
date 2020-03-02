# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 10-10

file = 'txt_files/lady.txt'  # Stores directory of file in 'file'

with open(file) as file:  # Opens file as file
    contents = file.read()  # Reads entirety of the file and stores it in 'contents'
    print(contents.lower().count('the'))  # Prints the amount of times the word "the" was read in the file.
