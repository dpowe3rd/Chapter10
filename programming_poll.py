# Darrell Powe III
# This is a practice exercise from the book "Python Crash Course"
# Exercise 10-5

filename = 'txt_files/responses.txt'

while True:
    response = input("Hello, may you please tell me why you like programming? Please enter 'I dont' if you wish to quit"
                     ".  ")
    if response.lower() == 'i dont':
        print("Ending program.")
        break

    print("Thank you for your input!\n")
    with open(filename, 'a') as file:
        file.write(response + '\n')
