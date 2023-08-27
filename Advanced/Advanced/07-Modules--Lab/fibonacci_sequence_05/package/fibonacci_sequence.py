class FibonacciSequence:
    def __init__(self):
        self.sequence = [0, 1]
    
    def create_sequence(self, count):
        while len(self.sequence) < count:
            next_number = self.sequence[-1] + self.sequence[-2]
            self.sequence.append(next_number)
        
        return self.sequence[:count]
    
    def locate_number(self, number):
        if number in self.sequence:
            index = self.sequence.index(number)
            return f"The number - {number} is at index {index}"
        else:
            return f"The number {number} is not in the sequence"
