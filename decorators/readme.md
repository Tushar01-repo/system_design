# Decorator Pattern (Complete Guide)

## 📌 Definition

The **Decorator Pattern** is a structural design pattern that allows you to **add new behavior to an object dynamically** without modifying its existing code.

> It follows the principle: **“Favor composition over inheritance.”**

---

## 🎯 Problem Statement

You have a base object and want to support multiple combinations of features.

Example:

* Basic Coffee
* Coffee + Milk
* Coffee + Sugar
* Coffee + Milk + Sugar

Using inheritance:

* Leads to **class explosion** ❌
* Hard to maintain and extend

---

## 💡 Solution

Instead of creating multiple subclasses:

* Wrap the object using **decorators**
* Each decorator adds its own behavior

---

## 🧱 Structure

### 1. Component (Interface / Abstract Class)

Defines the base functionality

### 2. Concrete Component

The original object

### 3. Decorator (Abstract Wrapper)

* Implements same interface
* Holds reference to component

### 4. Concrete Decorators

* Extend behavior dynamically

---

## ☕ Real-World Analogy

Coffee system:

* Base → Espresso
* Add-ons → Milk, Sugar

Instead of creating multiple coffee classes:

* You **wrap** coffee with decorators

---

## 🧪 Python Implementation

```
from abc import ABC, abstractmethod

# 1. Component
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> int:
        pass


# 2. Concrete Component
class BasicCoffee(Coffee):
    def cost(self) -> int:
        return 100


# 3. Decorator Base Class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> int:
        return self._coffee.cost()


# 4. Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self) -> int:
        return self._coffee.cost() + 20


class SugarDecorator(CoffeeDecorator):
    def cost(self) -> int:
        return self._coffee.cost() + 10


# Client Code
if __name__ == "__main__":
    coffee = BasicCoffee()
    
    coffee = MilkDecorator(coffee)
    coffee = SugarDecorator(coffee)

    print(f"Final Cost: ₹{coffee.cost()}")
```

---

## 🔄 How It Works

1. Create base object (`BasicCoffee`)
2. Wrap with `MilkDecorator`
3. Wrap again with `SugarDecorator`
4. Each decorator adds its own behavior

👉 Execution flows from outer → inner → back outward

---

## ✅ Advantages

* Follows **Open/Closed Principle**
* Avoids subclass explosion
* Enables **runtime flexibility**
* Promotes composition

---

## ❌ Disadvantages

* Many small classes
* Debugging can be harder (nested wrapping)
* Order of decorators matters

---

## ⚡ Real-World Use Cases

### 1. Logging

Wrap service with logging behavior

### 2. Caching

Add caching layer dynamically

### 3. Authentication Middleware

Add auth checks around APIs

### 4. UI Frameworks

Add borders, scrollbars, themes

---

## 🆚 Decorator vs Inheritance

| Feature          | Inheritance | Decorator |
| ---------------- | ----------- | --------- |
| Flexibility      | Low         | High      |
| Runtime Behavior | No          | Yes       |
| Class Explosion  | Yes         | No        |

---

## 🆚 Decorator vs Adapter vs Facade

| Pattern   | Purpose                  |
| --------- | ------------------------ |
| Decorator | Add behavior dynamically |
| Adapter   | Convert interface        |
| Facade    | Simplify complex system  |

---

## 🧠 Interview Insight

> Use Decorator Pattern when you need to **add responsibilities dynamically** to objects without modifying existing code.

---

## 📝 Quick Summary

* Wrap objects to extend behavior
* Uses composition over inheritance
* Flexible and scalable
* Common in middleware systems

---
