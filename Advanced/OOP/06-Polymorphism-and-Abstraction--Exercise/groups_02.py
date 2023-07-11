from typing import Iterable


class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
    
    def __add__(self, other) -> "Person":
        return Person(self.name, other.surname)
    
    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name: str, people: list) -> None:
        self.name = name
        self.people = people
    
    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other) -> "Group":
        new_name = f"{self.name} {other.name}"
        new_people = self.people + other.people
        return Group(new_name, new_people)
    
    def __getitem__(self, idx):
        return f"Person {idx}: {self.people[idx]}"

    def __repr__(self) -> str:
        return f"Group {self.name} with members {', '.join(repr(p) for p in self.people)}"
    
    def __iter__(self) -> Iterable[str]:
        for idx in range(len(self.people)):
            yield f"Person {idx}: {self.people[idx]}"
