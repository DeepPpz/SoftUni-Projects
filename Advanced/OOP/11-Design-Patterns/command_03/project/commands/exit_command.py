class ExitCommand:
    def __init__(self, window):
        self.window = window
    
    def execute(self):
        self.window.exit()
