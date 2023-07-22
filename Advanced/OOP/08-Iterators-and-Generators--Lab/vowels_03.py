from typing import Iterator


class vowels:
    VOWELS = "aeiouy"
    def __init__(self, text: str) -> None:
        self.vowels = [v for v in text if v.lower() in vowels.VOWELS]
        self.i = - 1
    
    def __iter__(self) -> Iterator[str]:
        return self
    
    def __next__(self) -> str:
        self.i += 1
        if self.i >= len(self.vowels):
            raise StopIteration

        return self.vowels[self.i]
