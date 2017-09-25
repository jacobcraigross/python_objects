# working with objects and OOP
# as a convention, always capitalize the first letter of the object
class Dog(object):

    #class object attribute, outside of the function
    species = 'mammal'

    def __init__(self, breed, name):

        self.breed = breed
        self.name = name

sam = Dog(breed = 'Lab', name = 'Joey')

print sam.name
print sam.breed

# Joey
# Lab
