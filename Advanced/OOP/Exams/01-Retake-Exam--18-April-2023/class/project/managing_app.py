from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.user import User
from project.route import Route

class ManagingApp:
    def __init__(self) -> None:
        self.users = []
        self.vehicles = []
        self.routes = []
    
    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            user = next(filter(lambda x: x.driving_license_number == driving_license_number, self.users))
            return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:
            self.users.append(User(first_name, last_name, driving_license_number))
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle (self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ["PassengerCar", "CargoVan"]:
            return f"Vehicle type {vehicle_type} is inaccessible."
        
        try:
            vehicle = next(filter(lambda x: x.license_plate_number == license_plate_number, self.vehicles))
            return f"{license_plate_number} belongs to another vehicle."
        except StopIteration:
            pass
        
        if vehicle_type == "PassengerCar":
            self.vehicles.append(PassengerCar(brand, model, license_plate_number))
        elif vehicle_type == "CargoVan":
            self.vehicles.append(CargoVan(brand, model, license_plate_number))
        
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point and r.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif r.start_point == start_point and r.end_point == end_point and r.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            elif r.start_point == start_point and r.end_point == end_point and r.length > length:
                r.is_locked = True
        
        self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."
    
    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = next(filter(lambda x: x.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda x: x.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda x: x.route_id == route_id, self.routes))
        
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        
        vehicle.drive(route.length)
        
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()
        
        return str(vehicle)
    
    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        to_be_fixed = list(sorted(damaged_vehicles, key=lambda x: (x.brand, x.model)))[:count]
        
        for v in to_be_fixed:
            v.is_damaged = False
            v.recharge()
        
        return f"{len(to_be_fixed)} vehicles were successfully repaired!"
    
    def users_report(self):
        users = list(sorted(self.users, key=lambda x: -x.rating))
        result = "*** E-Drive-Rent ***"
        for u in users:
            result += f"\n{str(u)}"
        
        return result
