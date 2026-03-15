cars = ['audi', 'bmw', 'subaru', 'mercedes', 'honda']
for car in cars:
    if car == 'honda':
        print(car.upper())
    else:
        print(car.title())


requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
elif 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
elif 'extra cheese' in requested_toppings:
    print('Adding extra cheese')


car = 'bmw'
print('true')
print(car == 'bmw')
print('false')
print(car == 'honda')
age = 23
print('false')
print(age == 24)


age = 16

if age >= 18:
    print('You are old enough to vote')
else:
    print('Sorry, you are too young to vote')
    print('Please register as soon as you get 18.')


usernames = []
if usernames:
    for user in usernames:
        if user == 'Admin':
            print('Hello ' + user.title() + '! would you like to see a status report?')
        else:
            print('Hello ' + user.title() + '! Thank you for logging in again.')

else:
    print('Sorry, we need to find some users.')
current_users = ['Ousmane', 'Anchita', 'Twaambo']
new_users = ['Wei', 'Ousmane', 'Anchita', 'Fnu', 'Tehreem']

for user in new_users:
    if user in current_users:
        print('you need to enter a new username. this already been used.')
    else:
        print('username ' + user.title() + ' is now available.')