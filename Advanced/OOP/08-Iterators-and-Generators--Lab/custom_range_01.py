from typing import Iterator


class custom_range:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.current = start - 1
    
    def __iter__(self) -> Iterator[int]:
        return self
    
    def __next__(self) -> int:
        self.current += 1
        if self.current <= self.end:
            return self.current
        else:
            raise StopIteration()
