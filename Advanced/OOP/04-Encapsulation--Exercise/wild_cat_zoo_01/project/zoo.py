from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []
    
    def add_animal(self, animal: Animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            animal_type = animal.__class__.__name__
            return f"{animal.name} the {animal_type} added to the zoo"
        elif price > self.__budget:
            return "Not enough budget"
        else:
            return "Not enough space for animal"
    
    def hire_worker(self, worker: Worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
            
        self.workers.append(worker)
        worker_type = worker.__class__.__name__
        return f"{worker.name} the {worker_type} hired successfully"
        
    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda x: x.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"
        
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"
    
    def pay_workers(self):
        total_salaries = sum([s.salary for s in self.workers])
        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"
    
    def tend_animals(self):
        total_care = sum([s.money_for_care for s in self.animals])
        if total_care <= self.__budget:
            self.__budget -= total_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."
    
    def profit(self, amount):
        self.__budget += amount
    
    def animals_status(self):
        lions = [animal for animal in self.animals if isinstance(animal, Lion)]
        tigers = [animal for animal in self.animals if isinstance(animal, Tiger)]
        cheetahs = [animal for animal in self.animals if isinstance(animal, Cheetah)]
        
        lions_str = "\n".join([repr(animal) for animal in lions])
        tigers_str = "\n".join([repr(animal) for animal in tigers])
        cheetahs_str = "\n".join([repr(animal) for animal in cheetahs])

        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions)} Lions:\n{lions_str}\n" \
               f"----- {len(tigers)} Tigers:\n{tigers_str}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n{cheetahs_str}"

    def workers_status(self):
        keepers = [worker for worker in self.workers if isinstance(worker, Keeper)]
        caretakers = [worker for worker in self.workers if isinstance(worker, Caretaker)]
        vets = [worker for worker in self.workers if isinstance(worker, Vet)]
        
        keepers_str = "\n".join([repr(worker) for worker in keepers])
        caretakers_str = "\n".join([repr(worker) for worker in caretakers])
        vets_str = "\n".join([repr(worker) for worker in vets])

        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers)} Keepers:\n{keepers_str}\n" \
               f"----- {len(caretakers)} Caretakers:\n{caretakers_str}\n" \
               f"----- {len(vets)} Vets:\n{vets_str}"
