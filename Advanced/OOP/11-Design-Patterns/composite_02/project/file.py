from component import Component


class File(Component):
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents
