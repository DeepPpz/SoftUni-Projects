from project.factories.abstract_factory import AbstractFactory
from project.furniture.chair import Chair
from project.furniture.sofa import Sofa
from project.furniture.table import Table


class FuturisticFactory(AbstractFactory):
    def create_chair(self):
        return Chair('futuristic chair')
    
    def create_sofa(self):
        return Sofa('futuristic sofa')
    
    def create_table(self):
        return Table('futuristic table')
