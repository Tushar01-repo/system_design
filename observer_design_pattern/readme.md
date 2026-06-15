# Observer Pattern (Complete Guide)

## 📌 Definition

The **Observer Pattern** is a behavioral design pattern that defines a **one-to-many relationship** between objects. When one object (Subject) changes its state, all its dependents (Observers) are **automatically notified**.

> Also known as **Publish-Subscribe (Pub/Sub)** pattern.

---

## 🎯 Problem Statement

Design a system where:

* Multiple users want updates from a source
* Instead of polling repeatedly, they should be **notified automatically**

Example:

* Users subscribing to a YouTube channel
* Stock price alerts
* Notification systems

---

## 🧠 Core Idea

* Observers **subscribe** to a subject
* Subject maintains a list of observers
* When state changes → subject **notifies all observers**

---

## 🧱 Structure

### 1. Subject (Publisher)

* Maintains list of observers
* Methods:

  * `subscribe(observer)`
  * `unsubscribe(observer)`
  * `notify()`

---

### 2. Observer (Interface)

* Defines:

  * `update(data)`

---

### 3. Concrete Observers

* Implement `update()`
* React to updates

---

## 🧪 Python Implementation

```
from abc import ABC, abstractmethod
from typing import List


# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, data: str) -> None:
        pass


# Subject
class YouTubeChannel:
    def __init__(self):
        self._subscribers: List[Observer] = []
        self._latest_video: str = ""

    def subscribe(self, observer: Observer) -> None:
        self._subscribers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._subscribers.remove(observer)

    def notify(self) -> None:
        for subscriber in self._subscribers:
            subscriber.update(self._latest_video)

    def upload_video(self, title: str) -> None:
        self._latest_video = title
        print(f"📢 New video uploaded: {title}")
        self.notify()


# Concrete Observers
class User(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, data: str) -> None:
        print(f"{self.name} received notification: {data}")


# Client Code
if __name__ == "__main__":
    channel = YouTubeChannel()

    user1 = User("Tushar")
    user2 = User("Rahul")

    channel.subscribe(user1)
    channel.subscribe(user2)

    channel.upload_video("Observer Pattern Explained")
```

---

## 🔄 How It Works

1. Observers subscribe to subject
2. Subject state changes
3. Subject calls `notify()`
4. All observers receive update

---

## ✅ Advantages

* Loose coupling between subject and observers
* Easy to add/remove observers
* Supports event-driven systems
* Scalable notification mechanism

---

## ❌ Disadvantages

* Can cause performance issues with many observers
* Hard to debug cascading updates
* Risk of memory leaks if observers are not removed

---

## ⚡ Real-World Use Cases

### 1. Event Systems

* Kafka consumers
* Pub/Sub architectures

### 2. UI Frameworks

* Button click listeners

### 3. Stock Market Apps

* Price change alerts

### 4. Notification Systems

* Email/SMS alerts

---

## 🆚 Observer vs Strategy

| Feature      | Observer                | Strategy             |
| ------------ | ----------------------- | -------------------- |
| Purpose      | Notify multiple objects | Choose one algorithm |
| Relationship | One → Many              | One → One            |
| Trigger      | State change            | Client-driven        |

---

## 🧠 Interview Insight

> Use Observer Pattern when multiple components need to react automatically to a change in state without tight coupling.

---

## 📝 Quick Summary

* One-to-many dependency
* Automatic notifications
* Core of event-driven systems
* Promotes loose coupling

---
