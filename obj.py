# working with objects and OOP
# as a convention, always capitalize the first letter of the object
class Dog(object):

    #class object attribute, outside of the function, 'global scope' if you will
    species = 'mammal'
    location = 'Texas'

    def __init__(self, breed, name, fur, fixed, age):

        self.breed = breed
        self.name = name
        self.fur = fur
        self.fixed = fixed
        self.age = age

sam = Dog(breed = 'Lab',
          name = 'Joey',
          fur = True,
          fixed = False,
          age = 4)

print sam.name
print sam.breed
print sam.age
print sam.fixed
print sam.fur
print sam.location

'''
Joey
Lab
4
False
True
Texas
'''
