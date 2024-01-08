# Introduction to Object Oriented Programming (OOP)
'''
TEMPLATES
    e.g. a template for a bag
    size:
    capacity:
    material:
    no_pockets:
    no_slings:
    category:
    price:

    e.g. a template for a car
    size:
    color:
    category:
    engine_size:
    no_passengers:
    price:

This is the fundamental concept of OOP, but instead of being called a template, it is called a class.
You can take that class to create an object, by customizing the values.
(Instantiation: creating an object from a class. Instance: an object created from a class. Attributes/Properties: the values of the class.)

    e.g. an instance of the class car
    size: suv
    color: red
    category: middle
    engine_size: 1800cc
    no_passengers: 4
    price: 25000
'''


# Creating a class
class Bag:
    def __init__(self, my_size, my_capacity, my_material, my_no_pockets, my_no_slings, my_category, my_price):
        self.size = my_size  #initialize the attributes
        self.capacity = my_capacity
        self.material = my_material
        self.no_pockets = my_no_pockets
        self.no_slings = my_no_slings
        self.category = my_category
        self.price = my_price  #'self' refers to the specific instance of the class. It is just a placeholder, and any word can be used. In a class there is a variable called self, and making a new instance copies the variable self.

    def get_size(self): #A function inside a class is called a method.
        return self.size

    def set_price(self, new_price): #You can also use a method to change an attribute of an instance
        self.price = new_price
    def get_price(self):
        return self.price

    def get_certification(self):
        if (self.size in "SM") and (self.capacity < 3):
            output = "Too small for school."
        if (self.size in "SM") and (self.capacity < 8):
            output = "Perfect for school."
        if (self.size in "L") and (3 <= self.capacity <= 8):
            output = "Perfect for school."
        else:
            output = "Too large for school."
        return output

# Create an instance of the class
tote_bag = Bag('M', 5, 'canvas', 0, 2, 'casual', 500)  #initializer function
camping_bag = Bag('L', 50, 'nylon', 5, 2, 'outdoor', 1000)

# Using a method
print(tote_bag.get_size())  #When you create an object, everything in the class is copied into the object, so the method is saved in each instance.
print(Bag.get_size(camping_bag))  #Less commonly used way of calling a method.

old_price = tote_bag.get_price()
print(f"Old price of the bag is {old_price} yen.")
tote_bag.set_price(new_price= 1.5*old_price)
print(f"New price of the bag is {tote_bag.get_price()} yen.")

print(tote_bag.get_certification())
print(camping_bag.get_certification())