# Interface Segregation Principle (ISP)
# please always remember this as we can't instantiate abstract classes
# eat_service = Eatable()
# work_service = Workable()

from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work():
        pass

class Eatable(ABC):
    @abstractmethod
    def eat():
        pass

class Robots(Workable):
    def work(self):
        print("yes, robot can only work")

class Human(Workable, Eatable):
    def work(self):
        print("yes, human can work")

    def eat(self):
        print("yes, human can eat")


if __name__ == "__main__":
    human = Human()
    robots = Robots()

    human.work()
    human.eat()

    robots.work()