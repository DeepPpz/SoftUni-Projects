class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"
    
    def save(self):
        with open(self.filename, "w") as file:
            file.write(self.contents)
