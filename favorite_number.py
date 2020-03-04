# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 10-11 & 10-12 & 10-13

import json  # imports json
filename = 'txt_files/numbers.json'  # Directory of the json file


def get_username():
    """
    Function that asks the user for an input of their name, which then opens the json file and compares the users input
    to all of the keys in the file. If the users input matches a key in the file, the function returns the users input
    and passes the value back to the greet_user() function.

    If the users input doesnt match any of the keys in the json file, they must be a new user and must be input into
    the json file, so the function calls the new_user function and passes it the users input.

    :return: User input
    """
    username = str(input("Hello, what is your name? "))  # Users name from input
    with open(filename) as file:  # Safely opens the JSON file
        data = json.load(file)  # Loads the JSON file so its acts like a normal dictionary
        for k in data:  # Access the keys in the json file
            if username == str(k):  # Compares the username to all the keys in the json file
                user = str(k)  # Stores the username in user and returns it
                return user

        else:  # If non of the keys match the users input they are a new user
            print("Okay, " + username + " let\'s get you setup.")
            new_user(username)


def get_fav_num(username):
    """
    Takes the username of the user as a parameter and matches it to the key it is equal to in the JSON file and returns
    the value associated with the key.
    :param username: Username of the user
    :return: The favorite number of the user
    """
    with open(filename) as file:
        data = json.load(file)  # Loads the json file so I can iterate over it as a regular dictionary.
        for k, v in data.items():  # Loop over its keys and value to match the username to a key
            if username == k:  # If the key matches this function takes the value associated with the key
                num = v  # and stores it in 'num'
                return num  # returns num


def new_user(username):
    """
    Function that stores the users input in a varible and passes the new variable to the function get_new_fav_num
    :param username: The username of the user
    :return:
    """
    new_username = username  # Stores the users input in new_username
    get_new_fav_num(new_username)  # Passes new_username to the get_new_fav_num function.


def get_new_fav_num(new_username):
    """
    Function that creates a new user entry in the JSON file
    :param new_username: Users input
    :return:
    """
    new_num = input("What is your favorite number? ")  # Asks the user their favorite number and stores it in 'new_num'
    fresh_account = {new_username: new_num}  # Dictionary of the new_username and new_num
    with open(filename, 'r+') as file:  # Safely opens the Json file
        data = json.load(file)  # Loads the json file as a dictionary that can be worked with
        data.update(fresh_account)  # Appends fresh_account to the 'data' dictionary
        file.seek(0)  # Positions the file pointer to position 0
        json.dump(data, file, indent=4)  # Rewrites the JSON file after appending the new user to it

    print("\nThank you, " + new_username + ", your favorite number is " + str(new_num) + ", and I will remember it!")


def greet_user():
    """
    Calls the get_username function to retrieve the users name, then calls the get_fav_name function to get the users
    favorite number. If the user is previous user their information is printed.
    :return:
    """
    username = get_username()  # Calls the get_username fucntion and stores its return value in 'username'
    fav_num = get_fav_num(username)  # Calls the get_fav_num function and passes it the returned 'username' and returns
    # the favorite number of said user.

    if username and fav_num:  # Prints a statement about the user and their favorite number if they're both not empty
        print("Hello again, " + username + ", your favorite number is " + fav_num + ".")


greet_user()  # Calls the greet user function to start to program.
