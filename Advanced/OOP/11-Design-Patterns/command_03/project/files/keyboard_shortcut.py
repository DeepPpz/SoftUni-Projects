class KeyboardShortcut:
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier
    
    def keypress(self):
        self.command.execute()
