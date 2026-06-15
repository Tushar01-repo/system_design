# this is my code

from abc import ABC, abstractmethod

# components
class PaymentDependency(ABC):

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


# concrete components
class MargheritaPizza(PaymentDependency):
    def get_description(self):
        return "This is margherita pizza"
    
    def get_cost(self):
        return 100
    

class VegBurger(PaymentDependency):
    def get_description(self):
        return "This is veg burger"
    
    def get_cost(self):
        return 50


# decorator base class
class FoodBaseDecorator(PaymentDependency):
    def __init__(self, paymethod: PaymentDependency):
        self._paymethod = paymethod

    def get_description(self):
        return self._paymethod.get_description()
    
    def get_cost(self):
        return self._paymethod.get_cost()


# concrete decorators
class CheeseDecorator(FoodBaseDecorator):
    def get_description(self):
        return self._paymethod.get_description() + " + cheese"
    
    def get_cost(self):
        return self._paymethod.get_cost() + 50
    

class SauceDecorator(FoodBaseDecorator):
    def get_description(self):
        return self._paymethod.get_description() + " + sauce"
    
    def get_cost(self):
        return self._paymethod.get_cost() + 30
    
class Olivesecorator(FoodBaseDecorator):
    def get_description(self):
        return self._paymethod.get_description() + " + olives"
    
    def get_cost(self):
        return self._paymethod.get_cost() + 10


# client code 
if __name__ == "__main__":
    food = MargheritaPizza()
    food = CheeseDecorator(food)
    food = Olivesecorator(food)

    print(food.get_description())
    print(food.get_cost())


    print("\n")
    
    food2 = VegBurger()
    food2 = CheeseDecorator(food2)
    food2 = SauceDecorator(food2)
    
    print(food2.get_description())
    print(food2.get_cost())
    

# -------------------------------------------------------------------

# this is chatgpt production ready code

from abc import ABC, abstractmethod


# Component
class FoodItem(ABC):

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> int:
        pass


# Concrete Components
class MargheritaPizza(FoodItem):
    def get_description(self) -> str:
        return "Margherita Pizza"
    
    def get_cost(self) -> int:
        return 200
    

class VegBurger(FoodItem):
    def get_description(self) -> str:
        return "Veg Burger"
    
    def get_cost(self) -> int:
        return 150


# Decorator Base Class
class FoodBaseDecorator(FoodItem):
    def __init__(self, food: FoodItem):
        self._food = food

    def get_description(self) -> str:
        return self._food.get_description()
    
    def get_cost(self) -> int:
        return self._food.get_cost()


# Concrete Decorators
class CheeseDecorator(FoodBaseDecorator):
    def get_description(self) -> str:
        return self._food.get_description() + " + Cheese"
    
    def get_cost(self) -> int:
        return self._food.get_cost() + 50
    

class SauceDecorator(FoodBaseDecorator):
    def get_description(self) -> str:
        return self._food.get_description() + " + Sauce"
    
    def get_cost(self) -> int:
        return self._food.get_cost() + 30
    

class OlivesDecorator(FoodBaseDecorator):
    def get_description(self) -> str:
        return self._food.get_description() + " + Olives"
    
    def get_cost(self) -> int:
        return self._food.get_cost() + 40


# Client Code
if __name__ == "__main__":
    food = MargheritaPizza()
    food = CheeseDecorator(food)
    food = OlivesDecorator(food)

    print(food.get_description())
    print(food.get_cost())
    
    print("\n")
    
    food2 = VegBurger()
    food2 = CheeseDecorator(food2)
    food2 = SauceDecorator(food2)
    
    print(food2.get_description())
    print(food2.get_cost())