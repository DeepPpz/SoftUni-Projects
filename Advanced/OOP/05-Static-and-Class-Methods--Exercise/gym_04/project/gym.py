from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self) -> None:
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []
    
    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)
    
    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)
    
    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)
    
    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)
    
    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
    
    def subscription_info(self, subscription_id: int) -> str:
        subscription = next(filter(lambda x: x.id == subscription_id, self.subscriptions))
        customer = next(filter(lambda x: x.id == subscription.customer_id, self.customers))
        trainer = next(filter(lambda x: x.id == subscription.trainer_id, self.trainers))
        plan = next(filter(lambda x: x.id == subscription.exercise_id, self.plans))
        equipment = next(filter(lambda x: x.id == plan.equipment_id, self.equipment))
        
        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
