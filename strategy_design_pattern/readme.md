# Strategy Design Pattern (Complete Implementation)

## 📌 Definition

The **Strategy Pattern** allows you to define a family of algorithms, encapsulate each one, and make them interchangeable at runtime.

> It helps eliminate large `if-else` or `switch` statements by delegating behavior to separate classes.

---

## 🎯 Problem Statement

Design a **Payment Processing System** where users can pay using different methods:

* Credit Card
* UPI
* PayPal

The system should:

* Allow switching payment methods at runtime
* Avoid `if-else` conditions
* Be easily extendable

---

## 🧱 Structure

1. **Strategy Interface** → Common contract
2. **Concrete Strategies** → Different implementations
3. **Context** → Uses a strategy

---

## 🧪 Python Implementation

```python
from abc import ABC, abstractmethod
from typing import Optional

# 1. Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: int) -> str:
        pass


# 2. Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: int) -> str:
        return f"Paid ₹{amount} using Credit Card"


class UPIPayment(PaymentStrategy):
    def pay(self, amount: int) -> str:
        return f"Paid ₹{amount} using UPI"


class PayPalPayment(PaymentStrategy):
    def pay(self, amount: int) -> str:
        return f"Paid ₹{amount} using PayPal"


# 3. Context
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def process_payment(self, amount: int) -> str:
        return self._strategy.pay(amount)


# Client Code
if __name__ == "__main__":
    processor = PaymentProcessor(UPIPayment())
    
    print(processor.process_payment(1000))
    
    # Change strategy dynamically
    processor.set_strategy(CreditCardPayment())
    print(processor.process_payment(2000))
    
    processor.set_strategy(PayPalPayment())
    print(processor.process_payment(3000))
```

---

## 🔄 How It Works

1. Define multiple payment strategies
2. Inject one into the `PaymentProcessor`
3. Processor delegates execution to the selected strategy
4. Strategy can be changed at runtime

---

## ✅ Advantages

* Eliminates `if-else` logic
* Easy to extend (add new strategies)
* Follows Open/Closed Principle
* Promotes clean code and separation of concerns

---

## ❌ Disadvantages

* Increased number of classes
* Client must be aware of available strategies

---

## ⚡ Real-World Use Cases

* Payment systems
* Discount engines
* Sorting algorithms
* ML model selection

---

## 🧠 Interview Insight

> Strategy Pattern is used when you have **multiple interchangeable behaviors** and want to **select one at runtime without modifying the context class**.

---

## 📝 Quick Summary

* Encapsulates algorithms
* Makes them interchangeable
* Removes conditionals
* Improves scalability

---
