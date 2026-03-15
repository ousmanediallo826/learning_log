alien_0 = {'color': 'green', 'points': 5, 'speed': 'mediums'}
print(alien_0['color'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print('The alien is now ' + str(alien_0['color']) + '.')

if alien_0['speed'] == 'slow':
    x_increment =  1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x position is ' + str(alien_0['x_position']))



favorite_languages = {
    'jen': 'python',
    'sarah': 'cs',
    'edward': 'ruby',
    'Ousmane': 'C',
    'phil': 'python'
}
print(favorite_languages)
print('Sarah favorite programming language is ' + favorite_languages['sarah'].title() + '.')


favorite_person = {
    'first_name': 'Fnu',
    'last_name': 'Anchita',
    'age': 18,
    'city': 'New York City',
    'country': 'US',
}
print(favorite_person['first_name'])
print(favorite_person['last_name'])
print(favorite_person['age'])
print(favorite_person['city'])
print(favorite_person['country'])
print(favorite_person['first_name'] + ' ' + favorite_person['last_name'] + ' is ' + str(favorite_person['age']) + ' years old. She lives in ' + favorite_person['city'] + '.')

for key, value in favorite_person.items():
    print(key + ': ' + str(value))


aliens = []
for alien_number in range(30):
    alien = {'color': 'green', 'points': 5, 'speed': 'medium'}
    aliens.append(alien)
for alien in aliens[:5]:
    print(alien)
    print("...")
print('The total number of aliens is ' + str(len(aliens)))
