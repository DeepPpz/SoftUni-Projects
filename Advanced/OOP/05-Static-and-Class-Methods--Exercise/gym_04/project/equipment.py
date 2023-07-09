class Equipment:
    id = 1
    
    def __init__(self, name: str) -> None:
        self.id = Equipment.id
        self.name = name
        Equipment.id += 1
    
    @staticmethod
    def get_next_id() -> int:
        return Equipment.id

    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"
