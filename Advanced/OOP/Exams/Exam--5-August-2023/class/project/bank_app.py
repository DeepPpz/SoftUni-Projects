from project.loans.base_loan import BaseLoan
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.clients.adult import Adult


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []
    
    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")
        
        self.loans.append(self.VALID_LOANS[loan_type]())
        return f"{loan_type} was successfully added."
    
    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")
        
        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."
        else:
            self.clients.append(self.VALID_CLIENTS[client_type](client_name, client_id, income))
            return f"{client_type} was successfully added."
    
    def grant_loan(self, loan_type: str, client_id: str):
        loan = next(filter(lambda x: type(x).__name__ == loan_type, self.loans))
        client = next(filter(lambda x: x.client_id == client_id, self.clients))
        
        if (type(client).__name__ == "Student" and loan_type == "MortgageLoan") or (type(client).__name__ == "Adult" and loan_type == "StudentLoan"):
            raise Exception("Inappropriate loan type!")
        
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
    
    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda x: x.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")
        
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."
    
    def increase_loan_interest(self, loan_type: str):
        changed_loans = 0
        
        for loan in self.loans:
            if type(loan).__name__ == loan_type:
                loan.increase_interest_rate()
                changed_loans += 1
        
        return f"Successfully changed {changed_loans} loans."
    
    def increase_clients_interest(self, min_rate: float):
        changed_clients = 0
        
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_clients += 1
        
        return f"Number of clients affected: {changed_clients}."
    
    def get_statistics(self):
        granted_loans = sum(len(client.loans) for client in self.clients)
        
        granted_sum = 0
        for client in self.clients:
            granted_sum += sum(loan.amount for loan in client.loans)
        
        if not self.clients:
            avg_interest = 0
        else:
            avg_interest = sum(client.interest for client in self.clients) / len(self.clients)
        
        result = f"Active Clients: {len(self.clients)}"
        result += f"\nTotal Income: {sum(client.income for client in self.clients):.2f}"
        result += f"\nGranted Loans: {granted_loans}, Total Sum: {granted_sum:.2f}"
        result += f"\nAvailable Loans: {len(self.loans)}, Total Sum: {sum(loan.amount for loan in self.loans):.2f}"
        result += f"\nAverage Client Interest Rate: {avg_interest:.2f}"

        return result
