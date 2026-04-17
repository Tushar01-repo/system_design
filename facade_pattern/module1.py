# subsystem classes
class AuthService:
    def __init__(self, user):
        self.user = user
    def authenticate(self):
        print(f"[AUTHENTICATE]: the user is {self.user}")
        
class InventoryService:
    def __init__(self, product):
        self.product = product
    def check_stock(self):
        print(f"[CHECK_STOCK]: the product ordered is {self.product}")
        
class PaymentService:
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount
    def process_payment(self):
        print(f"[PROCESS_PAYMENT]: the payment is in process for {self.user} for the amount of {self.amount}")

class OrderService:
    def __init__(self, user, product):
        self.user = user
        self.product = product
    def create_order(self):
        print(f"[CREATE_ORDER]: the user {self.user} ordered product i.e. {self.product}")

class NotificationService:
    def __init__(self, user):
        self.user =  user
    def send_notification(self):
        print(f"[SEND_NOTIFICATION]: the notification is send to the user : {self.user}")


# Facade class
class OrderFacade:

    def __init__(self, user, product, amount):
        self.user = user
        self.product = product
        self.amount = amount

    def place_order(self):
        auth_service = AuthService(self.user)
        inventory_service = InventoryService(self.product)
        order_service = OrderService(self.user, self.product)
        payment_service = PaymentService(self.user, self.amount)
        notification_service = NotificationService(self.user)

        auth_service.authenticate()
        inventory_service.check_stock()
        order_service.create_order()
        payment_service.process_payment()
        notification_service.send_notification()

        print("Hey, if all the steps done you.. it means your order is placed")


# Client Code
if __name__ == "__main__":
    orchestrator = OrderFacade("Tushar", "Jaggery Powder", "100")
    orchestrator.place_order()