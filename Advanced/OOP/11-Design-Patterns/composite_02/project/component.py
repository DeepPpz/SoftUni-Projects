class Component:
    def __init__(self, name):
        self.name = name
        self.parent = None
    
    def move(self, new_path):
        from main import get_path
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self
        self.parent = new_folder
    
    def delete(self):
        del self.parent.children[self.name]
