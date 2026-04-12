from abc import ABC, abstractmethod

# abstract product
class CardPayment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPIPayment(ABC):
    @abstractmethod
    def pay(self):
        pass

# concrete product
class StripeCard(CardPayment):
    def pay(self):
        print("you have paid via stripe card")

class StripeUpi(UPIPayment):
    def pay(self):
        print("you have paid via stripe UPI")

class RazorpayCard(CardPayment):
    def pay(self):
        print("you have paid via razorpay card")

class RazorpayUpi(UPIPayment):
    def pay(self):
        print("you have paid via razorpay UPI")


# abstract factory
class PaymentFactory(ABC):
    @abstractmethod
    def payment_card(self):
        pass

    @abstractmethod
    def payment_upi(self):
        pass
    
# concrete factories
class StripeFactory(PaymentFactory):
    def payment_card(self):
        return StripeCard()
    
    def payment_upi(self):
        return StripeUpi()

class RazorpayFactory(PaymentFactory):
    def payment_card(self):
        return RazorpayCard()
    
    def payment_upi(self):
        return RazorpayUpi()


# client code 
def payment_process(factory: PaymentFactory):
    pay_via_card = factory.payment_card()
    pay_via_upi = factory.payment_upi()

    pay_via_card.pay()
    pay_via_upi.pay()

# calling the main method 
if __name__ == "__main__":

    # always rememebr we are initializing the concrete classes not the abstract classes here
    # because always remember abstract classes can be initilized
    
    factory = StripeFactory()
    payment_process(factory)

    factory = RazorpayFactory()
    payment_process(factory)