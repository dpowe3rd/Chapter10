# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 10-3

filename = 'txt_files/guests.txt'  # Takes the path of the new file and stores it in 'filenname'

new_name = input("Hello, what is your name? ").title()  # Asks user for an input of their name and stores it in new name
print("Okay, " + new_name + ", I have added your name to our list.")  # Prints a statement for the user

with open(filename, 'a') as file:  # pens the file in append mode and momentarily names it 'file'
    file.write(new_name + '\n')  # Writes the users name on a new line of a text file.
