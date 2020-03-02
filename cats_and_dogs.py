# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 10-7

file1 = 'txt_files/cats.txt'
file2 = 'txt_files/dogs.txt'

try:
    with open(file1) as file:  # Opens file1
        contents = file.read()  # Reads the entirety of the file and stores it as a string in 'contents'

except FileNotFoundError:  # Catches FileNotFoundError and prints a statement regarding the file
    print("I\'m sorry, but your file does not exist.")

else:
    print(contents)  # Prints the contents of the file


try:
    with open(file2) as file:  # Opens file2
        contents2 = file.read()  # Reads the entirety of the file and stores it as a string in 'contents2'

except FileNotFoundError:
    print("I\'m sorry, but your file does not exist.")

else:
    print(contents2)  # Prints the contents of the file
