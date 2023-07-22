from typing import Iterator


class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.number = 0
        self.counter = 0
    
    def __iter__(self) -> Iterator[int]:
        return self
    
    def __next__(self) -> int:
        self.counter += 1
        if self.counter <= self.count:
            result = self.number
            self.number += self.step
            return result
        else:
            raise StopIteration()
