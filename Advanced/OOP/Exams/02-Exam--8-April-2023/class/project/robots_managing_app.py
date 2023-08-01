from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICES_TYPES = ["MainService", "SecondaryService"]
    ROBOT_TYPES = ["MaleRobot", "FemaleRobot"]
    
    def __init__(self):
        self.robots = []
        self.services = []
    
    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICES_TYPES:
            raise Exception("Invalid service type!")
        
        if service_type == "MainService":
            self.services.append(MainService(name))
        else:
            self.services.append(SecondaryService(name))
        
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")
        
        if robot_type == "MaleRobot":
            self.robots.append(MaleRobot(name, kind, price))
        else:
            self.robots.append(FemaleRobot(name, kind, price))
        
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(filter(lambda x: x.name == robot_name, self.robots))
        service = next(filter(lambda x: x.name == service_name, self.services))
        
        if type(robot).__name__ == "MaleRobot" and type(service).__name__ == "SecondaryService" or \
                type(robot).__name__ == "FemaleRobot" and type(service).__name__ == "MainService":
            return f"Unsuitable service."
        
        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")
        
        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."
    
    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(filter(lambda x: x.name == service_name, self.services))
        
        try:
            robot = next(filter(lambda x: x.name == robot_name, service.robots))
        except StopIteration:
            raise Exception("No such robot in this service!")
        
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."
    
    def feed_all_robots_from_service(self, service_name: str):
        service = next(filter(lambda x: x.name == service_name, self.services))
        
        for r in service.robots:
            r.eating()
        
        return f"Robots fed: {len(service.robots)}."
    
    def service_price(self, service_name: str):
        service = next(filter(lambda x: x.name == service_name, self.services))
        total_price = 0
        
        for r in service.robots:
            total_price += r.price
        
        return f"The value of service {service_name} is {total_price:.2f}."
    
    def __str__(self):
        result = ""
        for s in self.services:
            result += s.details() + "\n"
        
        return result.rstrip("\n")
