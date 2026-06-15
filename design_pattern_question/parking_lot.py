# ENUMS : {car , bike, truck} | {med, small, large} | {free, occupied}
# class vehicle --> init (number, type)
# class parking_spot --> init (id, type, vehicle), is_free, park_vehicle, remove_vehicle 
# class parking_floor --> init (floor_no, spot) , add_spot, find_available_spot
# class parking_lot --> init (floor) , add_floor, park_vehicles, remove_vehicles

from enum import Enum
from abc import ABC, abstractmethod
from datetime import datetime 

class vehicleType(Enum):
    CAR = "CAR"
    BIKE = "BIKE"
    TRUCK = "TRUCK"

class spotType(Enum):
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"
    LARGE = "LARGE"

class spotStatus(Enum):
    FREE = "FREE"
    OCCUPIED = "OCCUPIED"


class Vehicle:
    def __init__(self, number, vehicle_type):
        self.number = number
        self.vehicle_type = vehicle_type

class parkingSpot:
    def __init__(self, id, vehicle_type, vehicle):
        self.id = id
        self.type = vehicle_type
        self.status = spotStatus.FREE
        self.vehicle = None

    def is_free(self):
        return self.status == spotStatus.FREE

    def can_park_vehicle(self, vehicle):
        if vehicle.vehicle_type == vehicleType.BIKE:
            return self.spot_type == spotType.SMALL

        elif vehicle.vehicle_type == vehicleType.CAR:
            return self.spot_type == spotType.MEDIUM

        elif vehicle.vehicle_type == vehicleType.TRUCK:
            return self.spot_type == spotType.LARGE


        return False

    def park_vehicle(self, vehicle):

        if not self.is_free():
            raise Expectation("spot already occupied")

        if not self.can_park_vehicle(vehicle):
            raise Expectation("vehicle not compatible")

        self.vehicle = vehicle
        self.status = spotStatus.OCCUPIED



    def remove_vehicle(self):
        self.vehicle = None
        self.status = spotStatus.FREE


# class parking_floor --> init (floor_no, spot) , add_spot, find_available_spot
class parkingFloor:

    def __init__(self, floor_no):
        self.floor_no = floor_no
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def find_available_spot(self, vehicle):
        for spot in self.spots:
            if spot.is_free() and spot.can_park_vehicle(vehicle):
                return spot

        return None


# class parking_lot --> init (floor) , add_floor, park_vehicles, remove_vehicles
class Ticket:

    def __init__(self, vehicle, spot, floor):
        self.vehicle = vehicle 
        self.spot = spot
        self.floor = floor
        self.entry_time = datetime.now()

class parkingLot:
    def __init__(self, name):
        self.name = name
        self.floors = []

    def add_floor(self, floor):
        self.floors.append(floor)

    def park_vehicle(self, vehicle):

        for floor in self.floors:
            spot = floor.park_vehicle(vehicle)

            if spot in None:
                ticket = Ticket(vehicle, spot, floor)
                return ticket

        raise EXCEPTION("parking lot full")

    def remove_vehicle(self, ticket):

        floor = ticket.floor
        spot_id - ticket.spot.spot_id

        floor.remove_vehicle(spot_id)




#########################################################################################################################################


from enum import Enum
from datetime import datetime


# =========================
# ENUMS
# =========================

class VehicleType(Enum):
    CAR = "CAR"
    BIKE = "BIKE"
    TRUCK = "TRUCK"


class SpotType(Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class SpotStatus(Enum):
    FREE = "FREE"
    OCCUPIED = "OCCUPIED"


# =========================
# VEHICLE
# =========================

class Vehicle:

    def __init__(self, number, vehicle_type):
        self.number = number
        self.vehicle_type = vehicle_type


# =========================
# PARKING SPOT
# =========================

class ParkingSpot:

    def __init__(self, spot_id, spot_type):

        self.spot_id = spot_id
        self.spot_type = spot_type
        self.status = SpotStatus.FREE
        self.vehicle = None

    def is_free(self):

        return self.status == SpotStatus.FREE

    def can_park_vehicle(self, vehicle):

        if vehicle.vehicle_type == VehicleType.BIKE:
            return self.spot_type == SpotType.SMALL

        elif vehicle.vehicle_type == VehicleType.CAR:
            return self.spot_type == SpotType.MEDIUM

        elif vehicle.vehicle_type == VehicleType.TRUCK:
            return self.spot_type == SpotType.LARGE

        return False

    def park_vehicle(self, vehicle):

        if not self.is_free():
            raise Exception("Spot already occupied")

        if not self.can_park_vehicle(vehicle):
            raise Exception("Vehicle not compatible with spot")

        self.vehicle = vehicle
        self.status = SpotStatus.OCCUPIED

    def remove_vehicle(self):

        self.vehicle = None
        self.status = SpotStatus.FREE


# =========================
# PARKING FLOOR
# =========================

class ParkingFloor:

    def __init__(self, floor_no):

        self.floor_no = floor_no
        self.spots = []

    def add_spot(self, spot):

        self.spots.append(spot)

    def find_available_spot(self, vehicle):

        for spot in self.spots:

            if spot.is_free() and spot.can_park_vehicle(vehicle):
                return spot

        return None

    def park_vehicle(self, vehicle):

        spot = self.find_available_spot(vehicle)

        if spot is None:
            return None

        spot.park_vehicle(vehicle)

        return spot

    def remove_vehicle(self, spot_id):

        for spot in self.spots:

            if spot.spot_id == spot_id:

                spot.remove_vehicle()
                return True

        return False


# =========================
# TICKET
# =========================

class Ticket:

    def __init__(self, vehicle, spot, floor):

        self.vehicle = vehicle
        self.spot = spot
        self.floor = floor
        self.entry_time = datetime.now()

    def print_ticket(self):

        print("\n===== PARKING TICKET =====")
        print(f"Vehicle Number : {self.vehicle.number}")
        print(f"Vehicle Type   : {self.vehicle.vehicle_type.value}")
        print(f"Floor Number   : {self.floor.floor_no}")
        print(f"Spot ID        : {self.spot.spot_id}")
        print(f"Entry Time     : {self.entry_time}")
        print("==========================\n")


# =========================
# PARKING LOT
# =========================

class ParkingLot:

    def __init__(self, name):

        self.name = name
        self.floors = []

    def add_floor(self, floor):

        self.floors.append(floor)

    def park_vehicle(self, vehicle):

        for floor in self.floors:

            spot = floor.park_vehicle(vehicle)

            if spot is not None:

                ticket = Ticket(vehicle, spot, floor)

                print(f"{vehicle.number} parked successfully")
                return ticket

        raise Exception("Parking Lot Full")

    def remove_vehicle(self, ticket):

        floor = ticket.floor
        spot_id = ticket.spot.spot_id

        removed = floor.remove_vehicle(spot_id)

        if removed:
            print(f"{ticket.vehicle.number} removed successfully")
        else:
            print("Vehicle removal failed")


# =========================
# DRIVER CODE
# =========================

if __name__ == "__main__":

    # Create parking lot
    parking_lot = ParkingLot("City Mall Parking")

    # Create floors
    floor1 = ParkingFloor(1)
    floor2 = ParkingFloor(2)

    # Add spots to floor 1
    floor1.add_spot(ParkingSpot(1, SpotType.SMALL))
    floor1.add_spot(ParkingSpot(2, SpotType.MEDIUM))
    floor1.add_spot(ParkingSpot(3, SpotType.LARGE))

    # Add spots to floor 2
    floor2.add_spot(ParkingSpot(4, SpotType.SMALL))
    floor2.add_spot(ParkingSpot(5, SpotType.MEDIUM))

    # Add floors to parking lot
    parking_lot.add_floor(floor1)
    parking_lot.add_floor(floor2)

    # Create vehicles
    bike = Vehicle("KA01-BIKE-1111", VehicleType.BIKE)
    car = Vehicle("KA01-CAR-2222", VehicleType.CAR)
    truck = Vehicle("KA01-TRUCK-3333", VehicleType.TRUCK)

    # Park vehicles
    bike_ticket = parking_lot.park_vehicle(bike)
    car_ticket = parking_lot.park_vehicle(car)
    truck_ticket = parking_lot.park_vehicle(truck)

    # Print tickets
    bike_ticket.print_ticket()
    car_ticket.print_ticket()
    truck_ticket.print_ticket()

    # Remove vehicle
    parking_lot.remove_vehicle(car_ticket)