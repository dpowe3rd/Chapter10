# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 10-7


def add():
    """
    Simple Addition function with a try and expect block
    :return: The sum of num1 and num2
    """

    print("Welcome to a simple addition calculator: \n")  # Print simple statement
    flag = True  # Flag for while loop
    while flag:
        try:
            val1 = int(input("Please give me a value you would like to add. "))  # First value to be added
            val2 = int(input("Please give me another value you would like to add. "))  # Second value to be added

        except ValueError:  # Catches ValueErrors and prints a statement about using integers
            print("Please only input integer values. Thank you.\n")

        else:
            ans = val1 + val2  # Adds both values
            print("The answer to '" + str(val1) + " + " + str(val2) + "' is " + str(int(ans)) + ".")

            if ans != '':
                flag = False  # Breaks while loop by changing the flag to False if an answer was given


add()  # Calls function "add"
