from typing import List
from enum import Enum
import time

class VehicleSize(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3

class Vehicle:
    def __init__(self, size: VehicleSize, license_plate: str):
        self.size = size
        self.license_plate = license_plate
        self.entry_time = None

class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(VehicleSize.MOTORCYCLE, license_plate)

class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(VehicleSize.COMPACT, license_plate)

class Bus(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(VehicleSize.LARGE, license_plate)

class ParkingSpot:
    def __init__(self, spot_id: int, size: VehicleSize):
        self.spot_id = spot_id
        self.size = size
        self.is_available = True
        self.vehicle: Vehicle = None

    def can_fit(self, vehicle: Vehicle) -> bool:
        return self.is_available and vehicle.size.value <= self.size.value

    def park_vehicle(self, vehicle: Vehicle):
        if self.can_fit(vehicle):
            self.vehicle = vehicle
            self.is_available = False
            vehicle.entry_time = time.time()
            return True
        return False

    def remove_vehicle(self):
        self.vehicle = None
        self.is_available = True

class ParkingTicket:
    def __init__(self, spot_id: int, license_plate: str, entry_time: float):
        self.spot_id = spot_id
        self.license_plate = license_plate
        self.entry_time = entry_time
        self.exit_time = None
        self.fee = 0.0

    def calculate_fee(self, hourly_rate: float):
        self.exit_time = time.time()
        parked_time = (self.exit_time - self.entry_time) / 3600
        self.fee = round(parked_time * hourly_rate, 2)
        return self.fee

class ParkingLot:
    def __init__(self, hourly_rate: float):
        self.spots: list[ParkingSpot] = []
        self.hourly_rate = hourly_rate
        self.tickets = {}

    def add_parking_spot(self, spot: ParkingSpot):
        self.spots.append(spot)

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.spots:
            if spot.can_fit(vehicle):
                if spot.park_vehicle(vehicle):
                    ticket = ParkingTicket(spot.spot_id, vehicle.license_plate, vehicle.entry_time)
                    self.tickets[vehicle.license_plate] = ticket
                    print(f"Vehicle {vehicle.license_plate} parked in spot {spot.spot_id}.")
                    return True
        print(f"No spot available for vehicle {vehicle.license_plate}.")
        return False

    def remove_vehicle(self, license_plate: str):
        for spot in self.spots:
            if spot.vehicle and spot.vehicle.license_plate == license_plate:
                spot.remove_vehicle()
                ticket = self.tickets.pop(license_plate, None)
                if ticket:
                    fee = ticket.calculate_fee(self.hourly_rate)
                    print(f"Vehicle {license_plate} removed from spot {spot.spot_id}. Fee: ${fee}")
                return True
        print(f"Vehicle {license_plate} not found.")
        return False

    def available_spots(self, size: VehicleSize = None) -> List[ParkingSpot]:
        if size:
            return [spot for spot in self.spots if spot.is_available and spot.size == size]
        return [spot for spot in self.spots if spot.is_available]

    def print_summary(self):
        print("Parking Lot Summary:")
        print(f"Total Spots: {len(self.spots)}")
        print(f"Available Spots: {len(self.available_spots())}")
        print("Occupied Spots:")
        for spot in self.spots:
            if not spot.is_available:
                print(f"  Spot {spot.spot_id}: {spot.vehicle.license_plate}")

def main():
    parking_lot = ParkingLot(hourly_rate=10.0)

    parking_lot.add_parking_spot(ParkingSpot(1, VehicleSize.COMPACT))
    parking_lot.add_parking_spot(ParkingSpot(2, VehicleSize.LARGE))
    parking_lot.add_parking_spot(ParkingSpot(3, VehicleSize.MOTORCYCLE))

    car = Car("CAR123")
    motorcycle = Motorcycle("MOTO123")
    bus = Bus("BUS123")

    parking_lot.park_vehicle(car)
    parking_lot.park_vehicle(motorcycle)
    parking_lot.park_vehicle(bus)

    parking_lot.print_summary()

    parking_lot.remove_vehicle("CAR123")
    parking_lot.remove_vehicle("MOTO123")

    parking_lot.print_summary()

if __name__ == "__main__":
    main()
