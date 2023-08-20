from folder import Folder
from file import File


root = Folder('')

def get_path(path):
    names = path.split('/')[1:]
    node = root
    
    for name in names:
        node = node.children[name]
    
    return node
