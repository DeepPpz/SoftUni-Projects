class MenuItem:
    def __init__(self, menu_name, item_name):
        self.menu = menu_name
        self.item = item_name
    
    def click(self):
        self.command.execute()
