# Concrete Class in Low-Level Design (LLD)

## 🔹 What is a Concrete Class?

A **concrete class** is a class that has a **complete implementation** and can be **instantiated (object can be created)**.

> In simple terms:
> A class with **no abstract methods left** is called a *concrete class*.

---

## 🔹 Abstract Class vs Concrete Class

| Type           | Can Instantiate? | Has Implementation? |
| -------------- | ---------------- | ------------------- |
| Abstract Class | ❌ No             | Partial             |
| Concrete Class | ✅ Yes            | Complete            |

---

## 🔹 Example in Python

### Step 1: Abstract Class

from abc import ABC, abstractmethod

class Payment(ABC):

```
@abstractmethod
def pay(self, amount):
    pass
```

* This is **not a concrete class**
* It has an abstract method
* Cannot create object of Payment

---

### Step 2: Concrete Class

class CreditCardPayment(Payment):

```
def pay(self, amount):
    print(f"Paid {amount} using Credit Card")
```

* Implements all abstract methods
* Can create objects → **This is a concrete class**

p = CreditCardPayment()
p.pay(1000)

---

## 🔹 Real-Life Analogy

* **Abstract Class = Blueprint**

  * "Vehicle should have start() method"

* **Concrete Class = Actual Implementation**

  * Car → start with key
  * Bike → start with kick

---

## 🔹 Another Example

from abc import ABC, abstractmethod

class Animal(ABC):

```
@abstractmethod
def speak(self):
    pass
```

class Dog(Animal):   # Concrete Class
def speak(self):
return "Bark"

class Cat(Animal):   # Concrete Class
def speak(self):
return "Meow"

* Dog and Cat are **Concrete Classes**
* They implement all abstract methods

---

## 🔹 Key Characteristics of Concrete Class

A class is **concrete if**:

* All methods are implemented
* No @abstractmethod left
* Objects can be created
* Used in actual execution

---

## 🔹 Why Important in LLD?

Concrete classes are important because they:

* Represent real implementations
* Are used in object creation
* Work with design patterns like:

  * Factory Pattern
  * Strategy Pattern
  * Dependency Injection

---

## 🔹 Example in LLD (Payment System)

from abc import ABC, abstractmethod

class Payment(ABC):

```
@abstractmethod
def pay(self, amount):
    pass
```

class UPIPayment(Payment):
def pay(self, amount):
print(f"Paid {amount} using UPI")

class CardPayment(Payment):
def pay(self, amount):
print(f"Paid {amount} using Card")

def process_payment(payment_method: Payment):
payment_method.pay(500)

process_payment(UPIPayment())
process_payment(CardPayment())

---

## 🔹 Interview One-Liner

A **concrete class** is a class that provides full implementation and can be instantiated.

---

## 🔹 Quick Summary

* Abstract class → incomplete (cannot instantiate)
* Concrete class → complete (can instantiate)
* Used in real-world implementations
* Core part of LLD and design patterns

---
