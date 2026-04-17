# 🔌 Adapter Pattern — Interview Ready Guide

---

## 📌 Definition

**Adapter Pattern** is a **structural design pattern** that allows **incompatible interfaces to work together** by converting one interface into another that a client expects.

---

## 🧠 Intuition (Easy Understanding)

Think of a **phone charger 🔌**

* Your phone needs **Type-C**
* Wall socket provides a different pin

👉 You use an **adapter**

✔ Converts one interface → another
✔ Enables compatibility

---

## 🔥 Core Idea

👉 Convert one interface into another so that **existing code can work without modification**

---

## 🏗️ Structure

1. **Client** → Uses target interface
2. **Target Interface** → Expected interface
3. **Adaptee** → Existing incompatible class
4. **Adapter** → Bridges the gap

---

## 🧩 Class Diagram (Mental Model)

```id="k2m7xp"
Client → Target Interface
             ↑
         Adapter → Adaptee
```

---

## ❌ Problem Scenario

You have an old system:

```python id="g8q1pw"
class OldPaymentGateway:
    def make_payment(self, amount):
        print(f"Paid {amount} using old gateway")
```

But your system expects:

```python id="zq6w7e"
class PaymentProcessor:
    def pay(self, amount):
        pass
```

👉 Interfaces don’t match ❌

---

## ✅ Solution: Adapter Pattern

---

### 🔹 Step 1: Target Interface

```python id="e7j1cz"
class PaymentProcessor:
    def pay(self, amount):
        pass
```

---

### 🔹 Step 2: Adaptee

```python id="h1g9df"
class OldPaymentGateway:
    def make_payment(self, amount):
        print(f"Paid {amount} using old gateway")
```

---

### 🔹 Step 3: Adapter

```python id="3u7k9x"
class PaymentAdapter(PaymentProcessor):
    def __init__(self, old_gateway):
        self.old_gateway = old_gateway

    def pay(self, amount):
        self.old_gateway.make_payment(amount)
```

---

### 🔹 Step 4: Client Code

```python id="l4p9sd"
gateway = OldPaymentGateway()
adapter = PaymentAdapter(gateway)

adapter.pay(1000)
```

---

## 🧠 Output

```id="r7q2dz"
Paid 1000 using old gateway
```

---

## 🔑 Key Concepts

* Converts incompatible interfaces
* Promotes code reuse
* Avoids modifying legacy code
* Acts as a wrapper

---

## 🆚 Adapter vs Facade

| Feature | Adapter              | Facade                  |
| ------- | -------------------- | ----------------------- |
| Purpose | Interface conversion | Simplify complex system |
| Focus   | Compatibility        | Usability               |
| Usage   | Integration          | Abstraction             |

👉 Shortcut:

* **Adapter = Compatibility**
* **Facade = Simplicity**

---

## 🆚 Adapter vs Decorator

| Feature | Adapter          | Decorator    |
| ------- | ---------------- | ------------ |
| Purpose | Change interface | Add behavior |
| Focus   | Compatibility    | Enhancement  |

---

## 🚀 When to Use

✔ When integrating **legacy systems**
✔ When working with **third-party APIs**
✔ When interfaces don’t match
✔ When reusing existing components

---

## ❌ When NOT to Use

❌ If interfaces already match
❌ If redesigning system is simpler

---

## 🌍 Real-World Examples

* Payment gateway integrations
* Database connectors
* External API adapters
* File format converters

---

## 🧠 Interview One-Liner

> Adapter Pattern converts one interface into another that a client expects, enabling incompatible systems to work together.

---

## ⚡ Advantages

✔ Reusability of existing code
✔ Follows Open/Closed Principle
✔ Improves flexibility
✔ Reduces coupling

---

## ⚠️ Disadvantages

❌ Adds extra layer of abstraction
❌ Can increase complexity
❌ Too many adapters can clutter design

---

## 🔥 Pro Tip (Interview Insight)

If interviewer asks:

👉 *"Why not modify the existing class?"*

Answer:

> Modifying existing or third-party code violates Open/Closed Principle and can introduce risks. Adapter allows safe integration without changing existing implementations.

---

## 🧪 Quick Mental Check

Ask yourself:

* Do I have incompatible interfaces?
* Do I want to reuse existing code?

👉 If YES → Use Adapter Pattern

---

## 📌 Summary

* Adapter = Bridge between incompatible interfaces
* Converts interface
* Enables reuse
* Common in integrations

---

## 🎯 Next Steps

* Implement:

  * Payment Adapter system
  * Third-party API integration layer
* Combine with:

  * Facade Pattern
  * Strategy Pattern

---