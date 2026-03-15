message = input('Tell me something, I will repeat it back to you: ')
print(message)

numbers = input('Enter a number, and I will tell you if it is an odd or even number: ')
numbers = int(numbers)
if numbers % 2 == 0:
    print('Your number is even')
else:
    print('Your number is odd')


#Rental Car
cars_inventory = ['ford', 'bmw', 'audi', 'toyota', 'honda']
user_name = input('What is your name? ')
user_age = int(input('What is your age? '))
is_license = input("DO you have a valid driver license: ")
if user_age >= 18 and is_license:
    users_choice = input('Enter the car name that you would like to rent: ')


    if users_choice in cars_inventory:
        print('You have rented ' + users_choice)
        print('Please return it in 30 days')
    else:
        print('Sorry, we do not have ' + users_choice + ' on our inventory')
else:
    print('we are sincerly sorry, we could not rent you a car this time. ' + user_name)


#While loops

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


current_number = 0

while current_number < 15:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


unconfirmed_users = ['Alice', 'John', 'David']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)
    print('The following users were confirmed:')
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())


responses = {}

polling_active = True
while polling_active:
    name = input('What is your name? ')
    response = input('Which mountain would you like to climb? ')
    responses[name] = response

    repeat = input('Would you like to continue (yes/no)? ')
    if repeat == 'no':
        polling_active = False
print("\n--- Polling Results ---")
for name, response in responses.items():
    print(name + ' would like to climb mount' + response)


#Deli

sandwich_order = ['blt', 'club sandwich', 'egg salad sandwich', 'grilled sandwich', 'tuna sandwich']
finished_order = []

for order in sandwich_order:
    if order not in finished_order:
        print('I made your ' + order)
        finished_order.append(order)
for order in finished_order:
    print(order)