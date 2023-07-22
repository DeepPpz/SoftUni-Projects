from typing import Iterator


class countdown_iterator:
    def __init__(self, count: int) -> None:
        self.count = count
        self.countdown = count + 1
    
    def __iter__(self) -> Iterator[int]:
        return self
    
    def __next__(self) -> int:
        self.countdown -= 1
        if self.countdown < 0:
            raise StopIteration
           
        return self.countdown
