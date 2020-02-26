# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 10-4

filename = 'txt_files/guest_book.txt'

while True:
    new_name = input("Hello, what is your name? If you do not want to attend our event type 'quit' instead. ").title()
    # Takes an input of the users name and stores it in 'new_name'
    if new_name.lower() == 'quit':  # Reads if your name is 'quit' and if so it ends the loop.
        print("Goodbye.")  # Prints a ending statement.
        break
    print("Thank you for coming today " + new_name + ", we're glad you could make it.\n")  # Prints a greeting.
    with open(filename, 'a') as file:  # Opens the file in append mode as 'file'
        file.write(new_name + "\n")  # Writes 'new_name' onto the file with a newline at the end
