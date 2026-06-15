# Start Solving LLD Problems

Now begin actual Low-Level Design practice.

Do NOT start with advanced systems immediately.

---

# Beginner LLD Problems

## Level 1 Problems

These are the best starting problems:

1. Parking Lot
2. Library Management System
3. ATM Machine
4. Movie Ticket Booking System
5. Hotel Booking System
6. Restaurant Management System
7. Elevator System

---

# What These Problems Teach

| Problem        | Concepts Learned                    |
| -------------- | ----------------------------------- |
| Parking Lot    | Object modeling, enums, composition |
| ATM            | State handling, services            |
| Movie Booking  | Relationships, seat management      |
| Elevator       | State machine, scheduling           |
| Library System | CRUD modeling                       |

---

# Intermediate LLD Problems

After becoming comfortable with beginner problems:

1. Cab Booking System (Uber/Ola)
2. Food Delivery System (Swiggy/Zomato)
3. Splitwise
4. Snake & Ladder
5. Chess
6. Cricbuzz
7. Online Auction System

---

# Advanced LLD Problems

Once your fundamentals are strong:

1. Notification System
2. Rate Limiter
3. Logging Framework
4. Cache System
5. Kafka-like Queue
6. File Storage System

These combine:

* LLD concepts
* Scalability thinking
* Extensibility
* Concurrency handling

---

# What To Practice Inside Every LLD Problem

---

# Step 1 — Requirement Clarification

Always ask questions first.

Example for Parking Lot:

* Multiple floors?
* Different vehicle types?
* Pricing strategy?
* Reservation support?
* Multiple exits?

---

# Step 2 — Identify Entities

Example:

* ParkingLot
* ParkingFloor
* ParkingSpot
* Vehicle
* Ticket
* Payment

---

# Step 3 — Define Relationships

Example:

* ParkingLot HAS Floors
* Floor HAS Spots
* Vehicle GETS Ticket

---

# Step 4 — Assign Responsibilities

Ask yourself:

"Which class should own this behavior?"

This is the core of good design.

---

# Step 5 — Apply SOLID Principles

Check:

* Is any class doing too much?
* Is the system tightly coupled?
* Is the design extensible?
* Should interfaces be introduced?

---

# Step 6 — Add Design Patterns

Examples:

* Strategy Pattern → Pricing
* Factory Pattern → Vehicle creation
* Observer Pattern → Notifications
* State Pattern → Spot status

---

# What Interviewers Actually Evaluate

Interviewers usually care less about perfect UML diagrams.

They mainly evaluate:

* Problem-solving ability
* Object modeling
* Extensibility
* Maintainability
* SOLID principles
* Communication
* Tradeoff discussions

---

# Best Way To Practice LLD

For every problem:

## Round 1

* Read requirements
* Identify entities

## Round 2

* Design class diagram

## Round 3

* Write code

## Round 4

* Refactor using SOLID principles

## Round 5

* Add design patterns

This repetition builds strong intuition.

---

# Recommended Learning Order

Follow this sequence:

1. OOP
2. SOLID Principles
3. Relationships
4. UML Basics
5. Design Patterns
6. Beginner LLD Problems
7. Intermediate Problems
8. Advanced Systems

---

# Recommended First 5 Problems

Start with these:

1. Library Management System
2. Parking Lot
3. ATM Machine
4. Movie Ticket Booking
5. Elevator System

These problems cover most beginner concepts.

---

# Important Advice

Do NOT memorize solutions.

Instead practice:

* Identifying entities
* Assigning responsibilities
* Reducing coupling
* Improving extensibility
* Applying SOLID principles

That is real LLD skill.

---

# Recommended Resources

# YouTube Channels

* Concept && Coding by Piyush Garg
* CodeKarle
* Gaurav Sen

---

# Practice Resources

* LeetCode Discuss LLD Section
* Refactoring Guru

---

# UML Tool

* draw.io

---

# Final Advice

If you are just starting, focus more on:

* Clean thinking
* Object relationships
* SOLID principles
* Extensibility

instead of writing massive amounts of code.

The goal of LLD is not just coding.

The goal is designing maintainable and scalable software systems.

------------------------------------------------------------------------------------------------------


# ENUMS

`Enum` in Python is used to define a fixed set of named constant values. It makes code more readable, safer, and less error-prone than using raw strings or integers.

### Without Enum

```python
vehicle_type = "car"

if vehicle_type == "car":
    print("Park in car slot")
```

The problem:

* Typos are easy (`"Car"`, `"CAR"`, `"carr"`)
* No clear list of valid values
* Harder to maintain

---

### With Enum

```python
from enum import Enum

class VehicleType(Enum):
    CAR = "car"
    BIKE = "bike"
    TRUCK = "truck"

vehicle_type = VehicleType.CAR

if vehicle_type == VehicleType.CAR:
    print("Park in car slot")
```

Benefits:

* Prevents invalid values
* Improves readability
* IDE autocomplete support
* Easier refactoring

---

## Example: Parking Lot System

Instead of:

```python
class ParkingSpot:
    def __init__(self, spot_type):
        self.spot_type = spot_type

spot = ParkingSpot("small")
```

Use:

```python
from enum import Enum

class SpotType(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class ParkingSpot:
    def __init__(self, spot_type: SpotType):
        self.spot_type = spot_type

spot = ParkingSpot(SpotType.SMALL)
```

Now everyone knows the valid spot types are only:

* `SpotType.SMALL`
* `SpotType.MEDIUM`
* `SpotType.LARGE`

---

## Enum with Integers

```python
from enum import Enum

class Status(Enum):
    FREE = 1
    OCCUPIED = 2
```

Usage:

```python
spot_status = Status.FREE

if spot_status == Status.FREE:
    print("Available")
```

---

## Accessing Values

```python
print(VehicleType.CAR)
# VehicleType.CAR

print(VehicleType.CAR.value)
# car

print(VehicleType.CAR.name)
# CAR
```

---

## Common LLD Interview Usage

Enums are frequently used for:

* Vehicle types (`CAR`, `BIKE`, `TRUCK`)
* Parking spot status (`FREE`, `OCCUPIED`)
* Payment status (`PENDING`, `SUCCESS`, `FAILED`)
* Order status (`CREATED`, `SHIPPED`, `DELIVERED`)
* User roles (`ADMIN`, `CUSTOMER`, `DRIVER`)

For LLD interviews, if a field can only take a fixed set of values, using an `Enum` is usually cleaner than using strings.
