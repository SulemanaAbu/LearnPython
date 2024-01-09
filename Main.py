# functions
from abc import abstractmethod


class Animal:
    alive = True


@abstractmethod
class Prey:
    def flee(self):
        return "This animal is fleeing"


@abstractmethod
class Predator:
    def hunt(self):
        return "This animal is hunting"


class Fish(Animal, Prey, Predator):
    def flee(self):
        return "This fish is fleeing from a bigger fish"

    def hunt(self):
        return "This fish is hunting bigger fish"


class Hawk(Animal, Predator):
    def hunt(self):
        return "This hawk is hunting"


class Rabbit(Animal, Prey):
    def flee(self):
        return "This rabbit is fleeing"


animal = Animal()
fish = Fish()
rabbit = Rabbit()
hawk = Hawk()

print(animal.alive)
print(fish.flee())
print(fish.hunt())
print(rabbit.flee())
print(hawk.hunt())
