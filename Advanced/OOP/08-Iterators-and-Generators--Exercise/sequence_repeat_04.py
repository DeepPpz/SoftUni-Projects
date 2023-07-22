from typing import Iterator


class sequence_repeat:
    def __init__(self, sequence: str, number: int) -> None:
        self.sequence = sequence
        self.number = number
        self.i = -1
        self.total = 0
    
    def __iter__(self) -> Iterator[str]:
        return self
    
    def __next__(self) -> str:
        self.i += 1
        self.total += 1
        if self.total > self.number:
            raise StopIteration
        
        if self.i >= len(self.sequence):
            self.i = 0
        return self.sequence[self.i]
