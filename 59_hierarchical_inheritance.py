    # hierarchical inheritance 
    # 1 parent and multiple chiled class use 1 parent 


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



DOG = dog("FILGU")
DOG.speak()

CAT = cat("MINIII")
CAT.speak()