# this module covers open closed principles 

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, amount):
        pass

class RegularDiscount(DiscountStrategy):
    def apply(self, amount):
        return amount*0.20
    
class FestivalDiscount(DiscountStrategy):
    def apply(self, amount):
        return amount*0.50
    
class PremiumDiscount(DiscountStrategy):
    def apply(self, amount):
        return amount*0.70
    
class DiscountService:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def apply_discount(self, amount):
        return self.strategy.apply(amount)
    
if __name__=="__main__":
    amount = 1000

    strategy = [RegularDiscount() ,FestivalDiscount(), PremiumDiscount()]
    
    for i in strategy:
        service = DiscountService(i)
        final_price = service.apply_discount(amount)
        print(f"the discount for the service {type(i).__name__} is : {final_price}")

