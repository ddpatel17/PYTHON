    # hybrid inheritance
    #

# # parent class
class Animal:
    def sound(self):
        print("Animals make sounds")

# chiled class
class Mammal(Animal):
    def walk(self):
        print("Mammals can walk")

class Bird(Animal):
    def fly(self):
        print("Birds can fly")

class Bat(Mammal, Bird):
    def features(self):
        print("Bats can both fly and walk")

# Usage
bat = Bat()
bat.sound()      # From Animal
bat.walk()       # From Mammal
bat.fly()        # From Bird
bat.features()   # Defined in Bat




# perent class
class animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("some sound....")

# chiled class 
class dog(animal):
    def speak(self):
        print("say woof.....")

class cat(animal):
    def speak(self):
        print("say meow.....")


class pet(dog,cat):
    def features(self):
        print("pet can walk.....")


# # PET = pet()
# PET.features()
p = pet('buddy')
p.speak()        # Which one will it call?
p.features()     # Should print "pet can walk....."






