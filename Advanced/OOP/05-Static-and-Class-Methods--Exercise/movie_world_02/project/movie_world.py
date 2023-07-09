from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str) -> None:
        self.name = name
        self.customers = []
        self.dvds = []
    
    @staticmethod
    def dvd_capacity() -> int:
        return 15
    
    @staticmethod
    def customer_capacity() -> int:
        return 10
    
    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
    
    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)
    
    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = next(filter(lambda x: x.id == customer_id, self.customers))
        dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))
        
        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            else:
                return "DVD is already rented"
        elif dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        else:
            dvd.is_rented = True
            customer.rented_dvds.append(dvd)
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = next(filter(lambda x: x.id == customer_id, self.customers))
        dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))
        
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"
    
    def __repr__(self) -> str:
        result = "\n".join([str(cust) for cust in self.customers])
        result += "\n"
        result += "\n".join(str(dvd) for dvd in self.dvds)
        return result
