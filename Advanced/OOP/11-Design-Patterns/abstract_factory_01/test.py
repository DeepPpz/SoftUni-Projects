from project.factories.abstract_factory import AbstractFactory
from project.factories.futuristic_factory import FuturisticFactory
from project.factories.modern_factory import ModernFactory
from project.factories.victorian_factory import VictorianFactory


fac_victorian = VictorianFactory()
fac_modern = ModernFactory()
fac_futuristic = FuturisticFactory()

print(fac_victorian.create_chair())
print(fac_victorian.create_sofa())
print(fac_victorian.create_table())
