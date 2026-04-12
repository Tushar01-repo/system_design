# Liskov's principles implementation

from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def eat(self):
        pass


class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass


class Sparrow(FlyingBird):
    def eat(self):
        print("sparrow is eating")

    def fly(self):
        print("sparrow can fly")


class Penguin(Bird):
    def eat(self):
        print("penguin is eating")

    def swim(self):
        print("penguin can swim")


def make_bird_fly(bird: FlyingBird):
    bird.fly()


sparrow = Sparrow()
make_bird_fly(sparrow)   # ✅ works

penguin = Penguin()
# make_bird_fly(penguin) ❌ DON'T DO THIS
penguin.swim()           # ✅ correct