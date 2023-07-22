from typing import Iterator

class reverse_iter:
    def __init__(self, iterable: list) -> None:
        self.iterable = iterable
        self.i = len(self.iterable)
    
    def __iter__(self) -> Iterator[int]:
        return self
    
    def __next__(self) -> int:
        self.i -= 1
        if self.i >= 0:
            return self.iterable[self.i]
        else:
            raise StopIteration
