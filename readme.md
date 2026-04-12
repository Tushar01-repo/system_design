# 🧠 SOLID Principles in Python (Complete Guide with Examples)

This document provides a **complete overview of SOLID principles** with **clear explanations and Python examples**. It is designed for **interview preparation (LLD/System Design)** and writing **clean, scalable code**.

---

# 📌 What is SOLID?

SOLID is a set of 5 object-oriented design principles:

| Principle | Description                     |
| --------- | ------------------------------- |
| **S**     | Single Responsibility Principle |
| **O**     | Open/Closed Principle           |
| **L**     | Liskov Substitution Principle   |
| **I**     | Interface Segregation Principle |
| **D**     | Dependency Inversion Principle  |

---

# 🔵 1. Single Responsibility Principle (SRP)

## 💡 Definition

A class should have **only one reason to change**.

## ❌ Bad Design

```python
class UserService:
    def register(self, username):
        if len(username) < 3:
            raise ValueError("Invalid username")

        print("Saving user to DB")
        print("Sending email")
```

👉 Problem:

* Validation + DB + Notification → all in one class

---

## ✅ Good Design

```python
class UserValidator:
    def validate(self, username):
        if len(username) < 3:
            raise ValueError("Invalid username")


class UserRepository:
    def save(self, username):
        print("Saving user to DB")


class EmailService:
    def send(self, username):
        print("Sending email")


class UserService:
    def __init__(self, repo, validator, email_service):
        self.repo = repo
        self.validator = validator
        self.email_service = email_service

    def register(self, username):
        self.validator.validate(username)
        self.repo.save(username)
        self.email_service.send(username)
```

---

# 🟢 2. Open/Closed Principle (OCP)

## 💡 Definition

Software should be:

* **Open for extension**
* **Closed for modification**

---

## ❌ Bad Design

```python
class DiscountService:
    def apply_discount(self, user_type, amount):
        if user_type == "regular":
            return amount * 0.95
        elif user_type == "premium":
            return amount * 0.90
```

👉 Problem:

* Adding new type → modify code

---

## ✅ Good Design (Strategy Pattern)

```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, amount):
        pass


class RegularDiscount(DiscountStrategy):
    def apply(self, amount):
        return amount * 0.95


class PremiumDiscount(DiscountStrategy):
    def apply(self, amount):
        return amount * 0.90


class DiscountService:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def apply_discount(self, amount):
        return self.strategy.apply(amount)
```

---

# 🟡 3. Liskov Substitution Principle (LSP)

## 💡 Definition

Subclasses should be able to replace their parent class **without breaking behavior**.

---

## ❌ Bad Design

```python
class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Cannot fly")
```

👉 Problem:

* Penguin breaks expected behavior

---

## ✅ Good Design

```python
from abc import ABC, abstractmethod

class Bird(ABC):
    def eat(self):
        print("Eating")

class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow flying")

class Penguin(Bird):
    def swim(self):
        print("Penguin swimming")
```

# 💳 Liskov Substitution Principle (LSP) — Payment System Example

This document explains the **Liskov Substitution Principle (LSP)** using a **real-world Payment System example**.

---

# 🎯 What is LSP?

> A subclass should be able to replace its parent class **without breaking the program’s behavior**.

---

# 🧩 Problem Scenario

We want to design a system where different types of payments can be processed.

Examples:

* Credit Card
* UPI
* Cash on Delivery (COD)

---

# ❌ Bad Design (LSP Violation)

```python
class Payment:
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class CashOnDelivery(Payment):
    def pay(self, amount):
        raise Exception("COD cannot process online payment")
```

---

## 🚨 Problem

Now we write:

```python
def process_payment(payment: Payment):
    payment.pay(100)
```

---

## ❌ What happens?

| Payment Type     | Result    |
| ---------------- | --------  |
| Credit Card      | ✅ Works  |
| UPI              | ✅ Works  |
| Cash on Delivery | ❌ Breaks |

---

## 💥 Why is this wrong?

* `process_payment()` assumes **all payments support `pay()`**
* But `CashOnDelivery` does not support online payment

👉 This means:

> `CashOnDelivery` is NOT a valid substitute for `Payment`

🚨 **LSP is violated**

---

# 🔥 Root Cause

Wrong abstraction:

```text
Payment → pay() ❌
```

Reality:

```text
Some payments are online, some are offline ✅
```

---

# ✅ Good Design (LSP Compliant)

```python
from abc import ABC, abstractmethod


class Payment(ABC):
    pass


class OnlinePayment(Payment):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(OnlinePayment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UpiPayment(OnlinePayment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class CashOnDelivery(Payment):
    def collect_cash(self, amount):
        print(f"Collect {amount} on delivery")
```

---

## ✅ Correct Usage

```python
def process_payment(payment: OnlinePayment):
    payment.pay(100)


credit = CreditCardPayment()
upi = UpiPayment()

process_payment(credit)  # ✅ Works
process_payment(upi)     # ✅ Works

cod = CashOnDelivery()
cod.collect_cash(100)    # ✅ Correct usage
```

---

# 🧠 Key Learning

* Do NOT force all subclasses to support the same behavior
* Design abstractions based on **real-world truth**

---

# ⚠️ LSP Violation Signs

* Methods throwing errors like:

```python
raise Exception("Not supported")
```

* Subclasses overriding behavior incorrectly

---

# 🎯 Final Takeaway

> If a subclass cannot fully support the behavior of its parent,
> the design is wrong and needs to be restructured.

---

# 🚀 One-Line Summary

```text
LSP = Subclasses should behave correctly when used as their parent
```

---

# 🟠 4. Interface Segregation Principle (ISP)

## 💡 Definition

Clients should not be forced to implement methods they don’t use.

---

## ❌ Bad Design

```python
class Worker:
    def work(self): pass
    def eat(self): pass

class Robot(Worker):
    def work(self):
        print("Working")

    def eat(self):
        pass
```

---

## ✅ Good Design

```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Robot(Workable):
    def work(self):
        print("Robot working")

class Human(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")
```

---

# 🔴 5. Dependency Inversion Principle (DIP)

## 💡 Definition

Depend on **abstractions**, not **concrete implementations**.

---

## ❌ Bad Design

```python
class EmailService:
    def send(self, msg):
        print("Email:", msg)

class NotificationService:
    def __init__(self):
        self.email = EmailService()

    def notify(self, msg):
        self.email.send(msg)
```

---

## ✅ Good Design

```python
from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send(self, msg):
        pass

class EmailService(NotificationSender):
    def send(self, msg):
        print("Email:", msg)

class SMSService(NotificationSender):
    def send(self, msg):
        print("SMS:", msg)

class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, msg):
        self.sender.send(msg)
```

---

# 🧠 Quick Revision

```
S → One responsibility per class  
O → Extend without modifying  
L → Subclasses behave correctly  
I → Small, specific interfaces  
D → Depend on abstractions  
```

---

# 🚀 Final Takeaway

* Write **modular code**
* Avoid **tight coupling**
* Prefer **composition over inheritance**
* Design for **change and scalability**

---

# ▶️ Run

```bash
python filename.py
```

---

# 🎯 Purpose

* Interview preparation (LLD / System Design)
* Clean code practices
* Strong OOP fundamentals
