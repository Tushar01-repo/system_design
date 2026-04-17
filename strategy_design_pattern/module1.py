# this code is also correct implementation also you can use similar cleaner code from chatgpt 

from abc import ABC, abstractmethod

# strategy interface
class StrategyInterface(ABC):
    @abstractmethod
    def calculate_price(self, amount):
        pass

# concrete startegies
class NoDiscount(StrategyInterface):
    def calculate_price(self, amount):
        print(f"[NO DISCOUNT] : There is no discount for : {amount}")
        return amount

class FlatDiscount(StrategyInterface):
    def calculate_price(self, amount):
        final_price = amount - 500
        print(f"[FLAT] : The final price after discount is {final_price}")
        return final_price

class PercentageDiscount(StrategyInterface):
    def calculate_price(self, amount):
        final_price = amount * 0.10
        print(f"[PERCENTAGE DISCOUNT 10%] : The final price after discount is {amount - final_price}")
        return amount - final_price


class FestivalDiscount(StrategyInterface):
    def calculate_price(self, amount):
        final_price = amount * 0.20
        print(f"[Festival Discount 20% + 200 off] : The final price after discount is {amount - final_price - 200}")
        return amount - final_price - 200
    
# context
class PaymentProcess:
    def __init__(self, strategy: StrategyInterface):
        self.__strategy = strategy

    def set_strategy(self, strategy: StrategyInterface):
        self.__strategy = strategy

    def process_discount(self, amount):
        return self.__strategy.calculate_price(amount)
    
# client code
if __name__ == "__main__":
    processor = PaymentProcess(NoDiscount())
    print(processor.process_discount(2000))

    processor = PaymentProcess(FlatDiscount())
    print(processor.process_discount(2000))

    processor = PaymentProcess(PercentageDiscount())
    print(processor.process_discount(2000))

    processor = PaymentProcess(FestivalDiscount())
    print(processor.process_discount(2000))




# chatgpt generated code basically for interview ready
from abc import ABC, abstractmethod

# Strategy Interface
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_price(self, amount: int) -> int:
        pass


# Concrete Strategies
class NoDiscount(DiscountStrategy):
    def calculate_price(self, amount: int) -> int:
        return amount


class FlatDiscount(DiscountStrategy):
    def __init__(self, discount: int = 500):
        self.discount = discount

    def calculate_price(self, amount: int) -> int:
        return max(0, amount - self.discount)


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float = 0.10):
        self.percent = percent

    def calculate_price(self, amount: int) -> int:
        discount = amount * self.percent
        return max(0, int(amount - discount))


class FestivalDiscount(DiscountStrategy):
    def calculate_price(self, amount: int) -> int:
        discount = (amount * 0.20) + 200
        return max(0, int(amount - discount))


# Context
class PricingEngine:
    def __init__(self, strategy: DiscountStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DiscountStrategy):
        self._strategy = strategy

    def get_final_price(self, amount: int) -> int:
        return self._strategy.calculate_price(amount)


# Client Code
if __name__ == "__main__":
    engine = PricingEngine(NoDiscount())

    print(engine.get_final_price(2000))

    engine.set_strategy(FlatDiscount())
    print(engine.get_final_price(2000))

    engine.set_strategy(PercentageDiscount())
    print(engine.get_final_price(2000))

    engine.set_strategy(FestivalDiscount())
    print(engine.get_final_price(2000))