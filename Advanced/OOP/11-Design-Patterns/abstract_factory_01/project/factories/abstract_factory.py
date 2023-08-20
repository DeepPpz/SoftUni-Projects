from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        raise NotImplementedError()
    
    @abstractmethod
    def create_sofa(self):
        raise NotImplementedError()
    
    @abstractmethod
    def create_table(self):
        raise NotImplementedError()
