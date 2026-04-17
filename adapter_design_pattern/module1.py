# BEFORE PATTERN -- THIS IS ALSO CORRECT
from abc import ABC, abstractmethod

# target interface
class PaymentProcess(ABC):
    @abstractmethod
    def pay(self):
        pass

# adaptee interface
class StripeGateway:
    def make_payment(self, amount):
        print(f"stripe pay : {amount}")

class PayPalGateway:
    def send_payment(self, amount):
        print(f"paypal pay : {amount}")

class RazorPayGateway:
    def process_transaction(self, amount):
        print(f"razorpay pay : {amount} ")

# adapter interface
class StripeAdapter:
    def __init__(self, gateway):
        self.gateway = gateway

    def pay(self, amount):
        self.gateway.make_payment(amount)

class PaypalAdapter:
    def __init__(self, gateway):
        self.gateway = gateway

    def pay(self, amount):
        self.gateway.send_payment(amount)

class RazorpayAdapter:
    def __init__(self, gateway):
        self.gateway = gateway

    def pay(self, amount):
        self.gateway.process_transaction(amount)

# Client Code
def client_code(payment):
    payment.pay()

if __name__ == "__main__":
    payment = [
        StripeAdapter(StripeGateway()),
        PaypalAdapter(PayPalGateway()),
        RazorpayAdapter(RazorPayGateway())
    ]

    for p in payment:
        p.pay(1000)



# AFTER IMPLEMENTATION -- THIS IS ALSO CORRECT BUT THIS IS CLEANER VERSION

from abc import ABC, abstractmethod

# -------------------------
# Target Interface
# -------------------------
class PaymentProcess(ABC):
    @abstractmethod
    def pay(self, amount):   # ✅ added amount
        pass


# -------------------------
# Adaptee Classes (unchanged)
# -------------------------
class StripeGateway:
    def make_payment(self, amount):
        print(f"Stripe pay: {amount}")

class PayPalGateway:
    def send_payment(self, amount):
        print(f"PayPal pay: {amount}")

class RazorPayGateway:
    def process_transaction(self, amount):
        print(f"Razorpay pay: {amount}")


# -------------------------
# Adapters (now inherit target)
# -------------------------
class StripeAdapter(PaymentProcess):   # ✅ inherit
    def __init__(self, gateway):
        self.gateway = gateway

    def pay(self, amount):
        self.gateway.make_payment(amount)


class PayPalAdapter(PaymentProcess):   # ✅ fixed naming + inherit
    def __init__(self, gateway):
        self.gateway = gateway

    def pay(self, amount):
        self.gateway.send_payment(amount)


class RazorpayAdapter(PaymentProcess):   # ✅ consistent naming
    def __init__(self, gateway):
        self.gateway = gateway

    def pay(self, amount):
        self.gateway.process_transaction(amount)


# -------------------------
# Client Code
# -------------------------
def client_code(payment: PaymentProcess, amount):   # ✅ type clarity
    payment.pay(amount)


if __name__ == "__main__":
    payments = [
        StripeAdapter(StripeGateway()),
        PayPalAdapter(PayPalGateway()),
        RazorpayAdapter(RazorPayGateway())
    ]

    for p in payments:
        client_code(p, 1000)