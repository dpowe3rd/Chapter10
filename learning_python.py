# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 10-1

filename = 'txt_files/learning_python'  # Storing the path to the file in a variable

with open(filename) as file_object:  # opens the file as 'file_object'
    contents = file_object.read()  # Reads the entirety of the file and stores that in contents
    print(contents + '\n')  # Print contents

with open(filename) as file_object:  # opens the file as 'file_object'
    lines = file_object.readlines()  # Reads the file line by line and stores it as 'lines'
    for line in lines:  # Create a for loop that takes each individual line stored in lines
        print(line.rstrip())  # and prints it after removing whitespace to the right of the text.
    print('\n')  # Prints a new line

with open(filename) as file_object:  # opens the file as 'file_object'
    outside = file_object.read()  # Reads the entirety of the file and stores it in 'outside' so we can use the
    # contents of the file outside this 'with open' block

print(outside)  # Prints the contents of the file outside of the 'with open' block
