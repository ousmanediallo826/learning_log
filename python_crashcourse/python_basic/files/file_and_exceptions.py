with open("pi_digits.txt") as file:
    for line in file:
        print(line.strip())



filename = 'programming.txt'
with open(filename, 'w') as file:
    file.write("hello I love programming")
    file.write("\nI love building games")


with open(filename, 'a') as file:
    file.write("\nI also love finding meaning in large datasets")
    file.write("\nI love creating apps that can run in the browser")



guest_lists = 'guest_lists.txt'

while True:
    try:


        print("Welcome to the guest lists")
        guest_name = input("What is your guest name? ")
        with open(guest_lists, 'a') as file:
            file.write("\n" + guest_name )
        again = input("Would you like to continue (y/n)? ")
        if again == 'y':
            continue
        else:
            break
    except FileNotFoundError:
        print("Sorry, that file does not exist")

import json
numbers = [2, 3, 5, 13, 34, 45]

filename = 'numbers.json'
with open(filename) as file:
    number =json.load(file)
print(number)

def greet_user():
     filename1 = 'username.json'
     username = input('Enter your username: ')
     with open(filename1, 'w') as file:
         json.dump(username, file)
         print("We will remember you when you come back " + username + "!")

     with open(filename1) as file:
         username1 = json.load(file)
         print("Welcome back " + username1)

greet_user()

import json

def user_favorite_number():
    favorite_number = 'favorite_num.json'
    user_input = input('Please enter your favorite number: ')
    with open(favorite_number, 'w') as f:
        json.dump(user_input, f)

    with open(favorite_number) as file:
        favorite_number1 = json.load(file)
        print("I know your favorite number, and it is " + favorite_number1 + ".")


user_favorite_number()