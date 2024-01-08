from abc import abstractmethod


class Animal:

    @abstractmethod
    def eat(self):
        return "This animal is eating"

    @abstractmethod
    def move(self):
        return "This animal is moving"


class Fish(Animal):
    def eat(self):
        return "This fish is eating"

    def move(self):
        return "This fish is moving"


class Hawk(Animal):
    def eat(self):
        return "This hawk is eating"

    def move(self):
        return "This hawk is moving"


class Rabbit(Animal):
    def eat(self):
        return "This rabbit is eating"

    def move(self):
        return "This rabbit is moving"


fish = Fish()
hawk = Hawk()
rabbit = Rabbit()
print(rabbit.eat())
print(fish.move())
print(hawk.eat())
print(hawk.move())
