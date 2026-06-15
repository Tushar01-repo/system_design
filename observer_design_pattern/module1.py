from abc import ABC, abstractmethod

# observer interface
class observer(ABC):
    @abstractmethod
    def update(self, stock_name, price):
        pass


# subject
class stock:
    def __init__(self, name):
        self.name = name
        self._observers = []
        self._price = None

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self.name, self._price)

    def set_price(self, price):
        if self._price != price:
            self._price = price
            self.notify()


# implementing observer (user)
class User(observer):
    def __init__(self, name):
        self.name = name

    def update(self, stock_name, price):
        print(f"{self.name} notified : {stock_name} price is now {price}")

if __name__ == "__main__":
    apple = stock("AAPL")
    u1 = User("Alex")
    u2 = User("John")

    apple.subscribe(u1)
    apple.subscribe(u2)

    apple.set_price(150)
    apple.set_price(155)

    apple.unsubscribe(u1)
    apple.set_price(160)`