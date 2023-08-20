from component import Component


class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}
    
    def add_child(self, child):
        self.parent = self
        self.children[child.name] = child
