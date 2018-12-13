# A class of Animals
class Animal:
    species = "Mammal"

    def __init__(self):
        """
        set characteristics of animals
        """
        self.number_of_limbs = 4
        self.mode_of_feading = "Ominvorous"
        self.communicate = True
        self.pets = False
    
    def __str__(self):
        return "Species " + self.species + " and mode of feeding is: " + self.mode_of_feading


# A class of lions as Animal
class Lion(Animal):
    
    def __init__(self):
        """
        override characteristics of Animals specific to Lions
        """
        self.mode_of_feading = "Carnivorous"
        self.scary = True


# A class of lizard as Animals
class Lizard(Animal):
    species = "Reptile"

    def __init__(self):
        """
        override characters of Animals specific to Lizard and add more
        """
        self.communicate = False
        self.mode_of_feading = "Carnivorous"
        self.funny_fact = "They do push-ups almost everytime. Lol"

    def __str__(self):
        """
        show us this anytime class is instantiated
        """
        return "Funny Fact: " + self.funny_fact + " Communication: " + str(self.communicate)


animal = Animal()
print(animal)

lion = Lion()
print(lion)

lizard = Lizard()
print(lizard)