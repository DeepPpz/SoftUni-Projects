from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=15)
    
    def details(self):
        result = f"{self.name} Secondary Service:\n"
        result += f"Robots: {' '.join([r.name for r in self.robots]) if self.robots else 'none'}"
        return result
