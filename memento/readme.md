# Memento Design Pattern (Complete Guide)

## 📌 Definition

The **Memento Pattern** is a behavioral design pattern that allows you to **capture and restore an object’s previous state without exposing its internal details**.

> Commonly used for **Undo/Redo functionality**

---

## 🎯 Problem Statement

You have an object whose state changes over time, and you want to:

* Save its state at certain points
* Restore it later

But:

* You should NOT expose internal variables
* You should NOT tightly couple external classes to internal state

---

## 💡 Solution

* Create a **Memento object** to store state
* Let the main object (**Originator**) create and restore mementos
* Use a **Caretaker** to manage history

---

## 🧠 Core Idea

```text
Change State → Save Snapshot → Change Again → Restore Snapshot
```

---

## 🧱 Structure

### 1. Originator

* The main object whose state needs saving
* Creates and restores mementos

---

### 2. Memento

* Stores the state of the object
* Should be **immutable**

---

### 3. Caretaker

* Stores and manages mementos
* Does NOT modify them

---

## 🧩 Real-World Analogy

### 💾 Text Editor (Undo Feature)

* You type text
* System saves snapshots
* You press **Undo**
* Previous state is restored

---

## 🧪 Python Implementation

```
# Memento
class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state


# Originator
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text: str) -> None:
        self._content += text

    def get_content(self) -> str:
        return self._content

    def save(self) -> Memento:
        return Memento(self._content)

    def restore(self, memento: Memento) -> None:
        self._content = memento.get_state()


# Caretaker
class History:
    def __init__(self):
        self._mementos = []

    def push(self, memento: Memento) -> None:
        self._mementos.append(memento)

    def pop(self) -> Memento:
        return self._mementos.pop()


# Client Code
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Hello ")
    history.push(editor.save())

    editor.write("World!")
    print(editor.get_content())  # Hello World!

    editor.restore(history.pop())
    print(editor.get_content())  # Hello 
```

---

## 🔄 How It Works

1. Originator modifies state
2. Saves snapshot using `save()`
3. Caretaker stores snapshot
4. Later, restore using `restore()`

---

## ✅ Advantages

* Enables undo/redo functionality
* Maintains encapsulation
* Separates state management from business logic

---

## ❌ Disadvantages

* High memory usage if many snapshots
* Caretaker can grow large
* Performance overhead for large states

---

## ⚡ Real-World Use Cases

* Text editors (Undo/Redo)
* Game save states
* Database rollback systems
* Version control systems

---

## 🆚 Memento vs Command

| Feature  | Memento        | Command          |
| -------- | -------------- | ---------------- |
| Focus    | State snapshot | Action execution |
| Use Case | Undo state     | Undo operations  |
| Storage  | Saves state    | Saves actions    |

---

## 🧠 Interview Insight

> Use Memento Pattern when you need to **capture and restore object state without exposing internal structure**, especially for undo/rollback systems.

---

## 📝 Quick Summary

* Saves object state as snapshots
* Restores previous state
* Keeps encapsulation intact
* Used in undo/redo systems

---

## 🧠 One-Line Memory Trick

> **Memento = Snapshot of object state for future restore**

---
