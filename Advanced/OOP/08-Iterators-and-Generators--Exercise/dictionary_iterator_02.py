from typing import Iterator


class dictionary_iter:
    def __init__(self, dictionary: dict) -> None:
        self.dictionary = dictionary
        self.keys = [x for x in self.dictionary.keys()]
        self.i = 0
    
    def __iter__(self) -> Iterator[tuple]:
        return self
    
    def __next__(self) -> tuple:
        self.i += 1
        if self.i <= len(self.dictionary):
            key = self.keys[self.i-1]
            return (key, self.dictionary[key])
        else:
            raise StopIteration
