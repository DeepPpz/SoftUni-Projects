from project.factories.abstract_factory import AbstractFactory
from project.furniture.chair import Chair
from project.furniture.sofa import Sofa
from project.furniture.table import Table


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair('modern chair')
    
    def create_sofa(self):
        return Sofa('modern sofa')
    
    def create_table(self):
        return Table('modern table')
