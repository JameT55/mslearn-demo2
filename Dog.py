## Dog Class
class Dog():

# CLASS OBJECT ATTRIBUTE
# SAME FOR ANY INTANCE OF A CLASS
    species = 'mammal'

    def __init__ (self,breed,name):

    # Attributes
    # We take in the argument
    # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

# OPERATIONS/Actions ---> Methods
    def bark(self,number):
        print("WOOF! My name is {} and the number is {}".format(self.name,number))

my_dog = Dog('Lab', 'Frankie')

print(my_dog.species)
print(my_dog.name)
print(my_dog.breed)
my_dog.bark(2)
