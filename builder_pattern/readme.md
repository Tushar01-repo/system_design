# 🏗️ Builder Pattern — Interview Ready Guide

---

## 📌 Definition

**Builder Pattern** is a **creational design pattern** used to construct **complex objects step by step**, allowing different representations using the same construction process.

---

## 🧠 Intuition (Easy Understanding)

Think of building a **burger 🍔**:

You can customize:

* Bun
* Patty
* Cheese
* Sauce

Different combinations:

* Veg Burger
* Chicken Burger
* Cheese-loaded Burger

❌ Without Builder:

```python
Burger(bun, patty, cheese, sauce, ...)
```

👉 This becomes messy when parameters increase.

✔ With Builder:

```python
builder.add_bun().add_patty().add_cheese().build()
```

✔ Clean
✔ Flexible
✔ Readable

---

## 🚀 When to Use

Use Builder when:

✔ Object has **many optional parameters**
✔ Object creation is **complex**
✔ You want **step-by-step construction**
✔ You want **different representations of same object**

---

## 🏗️ Structure

1. **Product** → Final object
2. **Builder (Interface)** → Defines steps
3. **Concrete Builder** → Implements steps
4. **Director (Optional)** → Controls construction order

---

## 🧩 Class Diagram (Mental Model)

```
Builder
 ├── add_partA()
 ├── add_partB()
 ├── build()

ConcreteBuilder
 ├── constructs Product

Product
 ├── final object
```

---

## 💻 Complete Python Example

### 🔹 Step 1: Product

```python
class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.cheese = False
        self.sauce = None

    def __str__(self):
        return f"Burger(bun={self.bun}, patty={self.patty}, cheese={self.cheese}, sauce={self.sauce})"
```

---

### 🔹 Step 2: Builder Interface

```python
from abc import ABC, abstractmethod

class BurgerBuilder(ABC):

    @abstractmethod
    def add_bun(self):
        pass

    @abstractmethod
    def add_patty(self):
        pass

    @abstractmethod
    def add_cheese(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def build(self):
        pass
```

---

### 🔹 Step 3: Concrete Builder

```python
class VegBurgerBuilder(BurgerBuilder):

    def __init__(self):
        self.burger = Burger()

    def add_bun(self):
        self.burger.bun = "Wheat Bun"
        return self

    def add_patty(self):
        self.burger.patty = "Veg Patty"
        return self

    def add_cheese(self):
        self.burger.cheese = True
        return self

    def add_sauce(self):
        self.burger.sauce = "Mint Sauce"
        return self

    def build(self):
        return self.burger
```

---

### 🔹 Step 4: Client Code

```python
builder = VegBurgerBuilder()

burger = (
    builder
    .add_bun()
    .add_patty()
    .add_cheese()
    .add_sauce()
    .build()
)

print(burger)
```

---

## 🧠 Output

```
Burger(bun=Wheat Bun, patty=Veg Patty, cheese=True, sauce=Mint Sauce)
```

---

## 🧩 Director (Optional)

```python
class BurgerDirector:
    def build_standard_burger(self, builder: BurgerBuilder):
        return (
            builder
            .add_bun()
            .add_patty()
            .add_sauce()
            .build()
        )
```

---

## 🔑 Key Concepts

* Step-by-step object creation
* Avoids constructor complexity
* Supports method chaining
* Same process → different outputs

---

## 🆚 Builder vs Abstract Factory

| Feature | Builder                   | Abstract Factory           |
| ------- | ------------------------- | -------------------------- |
| Purpose | Build one complex object  | Create families of objects |
| Focus   | Step-by-step construction | Grouped object creation    |
| Output  | Single object             | Multiple related objects   |

👉 Shortcut:

* **Builder = One complex object**
* **Abstract Factory = Family of objects**

---

## 🌍 Real-World Examples

* API Request Builders
* SQL Query Builders
* Configuration Objects
* Complex JSON Construction

---

## ⚡ Advantages

✔ Improves readability
✔ Handles complex construction
✔ Promotes immutability (optional)
✔ Flexible object creation

---

## ⚠️ Disadvantages

❌ More classes required
❌ Overkill for simple objects
❌ Slight increase in complexity

---

## 🧠 Interview One-Liner

> Builder Pattern constructs complex objects step by step, allowing different representations using the same construction process.

---

## 🔥 Pro Tip (Interview Insight)

If interviewer asks:

👉 *"Why not use constructor?"*

Answer:

> Constructors become messy with many optional parameters. Builder improves clarity, flexibility, and maintainability.

---

## 🧪 Quick Mental Check

Ask yourself:

* Is object **complex**?
* Are there **many optional fields**?
* Do I need **step-by-step control**?

👉 If YES → Use Builder Pattern

---

## 📌 Summary

* Builder = Step-by-step object creation
* Solves constructor explosion
* Clean and readable design
* Widely used in real-world systems

---

## 🎯 Next Steps

* Try implementing:

  * HTTP Request Builder
  * Database Query Builder
* Compare with:

  * Factory Pattern
  * Abstract Factory
  * Dependency Injection

---

✨ You are now ready to confidently explain Builder Pattern in interviews!
