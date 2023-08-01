from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=30)
    
    def details(self):
        result = f"{self.name} Main Service:\n"
        result += f"Robots: {' '.join([r.name for r in self.robots]) if self.robots else 'none'}"
        return result
