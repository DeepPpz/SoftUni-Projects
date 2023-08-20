class SaveCommand:
    def __init__(self, document):
        self.document = document
    
    def execute(self):
        self.document.save()
