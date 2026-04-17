# Chain of Responsibility Pattern (Complete Guide)

## 📌 Definition

The **Chain of Responsibility (CoR)** is a behavioral design pattern that allows a request to **pass through a chain of handlers**, where each handler gets a chance to process it.

If a handler cannot process the request, it forwards it to the next handler in the chain.

---

## 🎯 Problem It Solves

Imagine you have multiple ways to handle a request:

* Level 1 Support
* Level 2 Support
* Manager

Without CoR:

* You write multiple `if-else` or `switch` conditions ❌
* Code becomes tightly coupled and hard to extend

---

## 💡 Solution

Create a chain of handler objects:

* Each handler decides:

  * **Can I handle this?**
  * If yes → handle it
  * If no → pass to next handler

---

## 🧱 Structure

### 1. Handler (Abstract Class / Interface)

Defines:

* Reference to next handler
* Method to process request

### 2. Concrete Handlers

Actual implementations that:

* Handle specific types of requests

### 3. Client

Sends request to the first handler

---

## 🧑‍💼 Real-World Analogy

Customer support system:

1. **Level 1 Support** → handles basic issues
2. **Level 2 Support** → handles intermediate issues
3. **Manager** → handles critical issues

Request flows until someone resolves it.

---

## 🧪 Python Implementation

```python
from abc import ABC, abstractmethod

# 1. Handler
class SupportHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, request):
        pass


# 2. Concrete Handlers
class Level1Support(SupportHandler):
    def handle(self, request):
        if request == "basic":
            print("Level 1 handled the request")
        elif self.next_handler:
            self.next_handler.handle(request)


class Level2Support(SupportHandler):
    def handle(self, request):
        if request == "intermediate":
            print("Level 2 handled the request")
        elif self.next_handler:
            self.next_handler.handle(request)


class Manager(SupportHandler):
    def handle(self, request):
        if request == "critical":
            print("Manager handled the request")
        else:
            print("Request cannot be handled")


# 3. Setup Chain
handler_chain = Level1Support(
    Level2Support(
        Manager()
    )
)

# 4. Client Requests
handler_chain.handle("basic")
handler_chain.handle("intermediate")
handler_chain.handle("critical")
handler_chain.handle("unknown")
```

---

## 🔄 How It Works

Step-by-step:

1. Client sends request to first handler
2. Handler checks if it can process
3. If yes → handles it
4. If no → forwards to next handler
5. Process continues until handled or chain ends

---

## ✅ Advantages

* Reduces coupling between sender and receiver
* Follows **Open/Closed Principle**
* Easy to add/remove handlers
* Clean and scalable design

---

## ❌ Disadvantages

* Request might go unhandled
* Debugging can be tricky
* Performance overhead if chain is long

---

## 🆚 Chain of Responsibility vs If-Else

| Feature       | If-Else | Chain of Responsibility |
| ------------- | ------- | ----------------------- |
| Flexibility   | Low     | High                    |
| Scalability   | Poor    | Good                    |
| Coupling      | Tight   | Loose                   |
| Extendability | Hard    | Easy                    |

---

## 🧠 When to Use

Use this pattern when:

* Multiple objects can handle a request
* You don’t know which handler will process it
* You want to decouple sender and receiver
* You want dynamic request handling flow

---

## ⚡ Real-World Use Cases

### 1. Middleware Pipelines

* Logging → Auth → Validation → Business Logic

### 2. Event Handling Systems

* GUI event propagation

### 3. Access Control Systems

* Role-based permission chains

### 4. Exception Handling Chains

* Try multiple handlers sequentially

---

## 🧩 Key Insight (Interview Tip)

Instead of writing:

```python id="lzpl67"
if request == "basic":
    ...
elif request == "intermediate":
    ...
elif request == "critical":
    ...
```

Use:

```python id="z7jz2u"
handler_chain.handle(request)
```

---

## 📝 Quick Summary

* Pass request through a chain of handlers
* Each handler decides to process or forward
* Promotes loose coupling
* Highly extensible and scalable

---
