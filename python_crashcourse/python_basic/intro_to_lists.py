bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

message = 'My first bicycle was a ' + bicycles[3].title() + '.'
print(message)


names = ['Twaambo', 'Wei', 'David', 'Nazia']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

greeting = 'Good Morning ' + names[0] + '. How are you?'
greeting1 = 'Good Morning ' + names[1] + '. How are you?'
greeting2 = 'Good Morning ' + names[2] +'. How are you?'
greeting3 = 'Good Morning ' + names[3] + '. How are you?'
print(greeting)
print(greeting1)
print(greeting2)
print(greeting3)


motocycles = ['Honda', 'BMW', 'Yamaha']
motocycles[0] = 'ducati'
motocycles.append('Suzuki')
message1 = 'I would like to own ' + motocycles[0] + '.'
message2 = 'I would like to own ' + motocycles[1] + '.'
message3 = 'I would like to own ' + motocycles[2] + '.'
message4 = 'I would like to own ' + motocycles[3] + '.'
motocycles.insert(0, 'Toyota')
motocycles.insert(2, 'Audi')
del motocycles[0]
print(motocycles)
print(message1)
print(message2)
print(message3)
print(message4)


#Guest List

guest_lists = ['Twaambo', 'Wei', 'David', 'Nazia', 'Alhassane']
guest_lists.remove('David')
guest_lists.insert(2, "Franciane")
print(guest_lists)
send_message = 'Hi ' + guest_lists[0] + '. How are you? I would love to invite to dinner on Saturday night.'
send_message1 = 'Hi ' + guest_lists[1] + '. How are you? I would like to invite to dinner on Saturday night.'
send_message2 =  'Hi ' + guest_lists[2] + '. How are you? I would like to invite to dinner on Saturday night.'
send_message3 =  'Hi ' + guest_lists[3] + '. How are you? I would like to invite to dinner on Saturday night.'
send_message4 =  'Hi ' + guest_lists[1] + '. How are you? I would like to invite to dinner on Saturday night.'
out_of_guest = guest_lists[2] + "Can't make to the dinner."
print(out_of_guest)

print(send_message)
print(send_message1)
print(send_message2)
print(send_message3)
print(send_message4)


cars = ['BMW', 'Audi', 'Toyota Camri', 'Honda']
cars.sort()
print(cars)
print(len(cars))


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print('that was a great trick.')
    print("I can't wait to see your next tricks " + magician.title())
print("Thank you, everyone! That was a great magic show")


pizzas = ['Cheese Pizza', 'pepperoni pizza', 'meat pizza']
for pizza in pizzas:
    print('I like this '+ pizza.title() + '.')
print('How much you like our Pizza?')


numbers = list(range(1, 11))
print(numbers)

squares = []
for values in range(1, 11):
    squares.append(values * values)
print(squares)


players = ['Michael', 'martina', 'charles', 'florence', 'eli']
for player in players[:3]:
    print(player)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print('My favourite foods are:')
print(my_foods)
print('\nMy friend\'s favourite foods are:')
print(friend_foods)


#Tuples
dimenssions = (200, 50)

print(dimenssions[0])
print(dimenssions[1])

buffets = ('cake', 'biryani', 'chicken over rice', 'salad')

for buffet in buffets:
    print(buffet)