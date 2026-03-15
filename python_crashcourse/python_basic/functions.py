# from re import fullmatch
#
#
# def greet_user(username):
#     print('Hello ' + username.title() + '!')
# greet_user('Ousmane')
# greet_user('Anchita')
# greet_user('Twaambo')
#
# def display_message():
#     print('Hello everyone! Today I am learning functions in python!')
#
# display_message()
#
# def favorite_book(title):
#     print('My favorite book is ' + title + '.')
#
# favorite_book('Alice in Wonderland')
#
#
# def describe_pet(animal_type, pet_name):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
# describe_pet('hamster', 'harry')
#
#
# def make_shirt(size='Large', text='I love python'):
#     print('\n the size of the shirt is ' + size + ' ' + text)
#
# make_shirt()
#
# def describe_cities(city, country):
#     print('\n the city is ' + city + ', and it is in ' + country + '.')
#
# describe_cities('New York City', 'USA')
#
#
# def get_formatted_name(first_name, last_name):
#     full_name =  first_name + ' ' + last_name
#     return full_name.title()
#
#
#
# while True:
#     print("\nPlease tell me your name")
#     f_name = input()
#     l_name = input()
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello " + formatted_name)
#     break
#
# def build_person(first_name, last_name):
#     person = {'first_name': first_name, 'last_name': last_name}
#     return person
# person = build_person('Ousmane', 'Diallo')
# print(person)
#
#
#
# def make_album(name, album_title, numbers_of_tracks=1):
#     album = {'name': name, 'album_title': album_title, 'numbers_of_tracks': numbers_of_tracks}
#     return album
#
# while True:
#     print("\nPlease tell me your album")
#     name = input("Enter your name: ")
#     album_title = input('Enter the album title ')
#     number_of_tracks = int(input('Enter the number of tracks '))
#     album = make_album(name, album_title, number_of_tracks)
#
#     print(album)
#     break


magicians = ['Ali', 'John', 'Kedar']

def display_magicians(names):
    for name in names:
        print('Hello ' + name + '.')

display_magicians(magicians)
