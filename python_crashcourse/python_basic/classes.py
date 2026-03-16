class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolls over!")


my_dog = Dog('Julia', 18)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + ".")
print(my_dog.sit())
print(my_dog.roll_over())


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, open_restaurants):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open_restaurants = open_restaurants

    def describe_restaurant(self):
        print("The restaurant is " + self.restaurant_name.title() + ".")
        print("This restaurant is " + self.cuisine_type.title() + ".")
    def open_restaurant(self):
        if self.open_restaurants:
            print("The restaurant is open.")
        else:
            print("The restaurant is closed.")


Indian_restaurant = Restaurant('Indian Restaurant', 'Indian Cuisine Type', True)
print(Indian_restaurant.restaurant_name + " " + Indian_restaurant.cuisine_type  + " " + str(Indian_restaurant.open_restaurants))



class User():
    def __init__(self, first_name, last_name, age, email, is_active):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.is_active = is_active

    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        print(full_name + " is " + str(self.age) + " years old. and he/she is active: " + str(self.is_active ))

    def greet_user(self):
        print("Hello, " + self.first_name + ", " + self.last_name + "!")
        print("Welcome back to our platform")



ousmane = User('Ousmane', 'Diallo', 25, '', True)
Anchita = User('Fnu', 'Anchita', 18, '', True)

print(ousmane.describe_user())
print(ousmane.greet_user())
print(Anchita.describe_user())
print(Anchita.greet_user())




class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('Ford', 'Mustang', 2026)
my_new_car.odometer_reading = 25
my_new_car.read_odometer()
print(my_new_car.descriptive_name())
print(my_new_car.read_odometer())

my_second_car = Car('Audi', 'a4', 2025)
print(my_second_car.descriptive_name())
print(my_second_car.read_odometer())



