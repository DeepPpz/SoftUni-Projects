class ToolbarDocument:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname
    
    def click(self):
        self.command.execute()
