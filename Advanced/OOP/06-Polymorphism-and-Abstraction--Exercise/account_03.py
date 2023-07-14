from typing import Iterable, List


class Account:
    def __init__(self, owner: str, amount: int = 0, transactions: List = []) -> None:
        self.owner = owner
        self.amount = amount
        self._transactions = transactions
    
    @property
    def balance(self) -> int:
        return self.amount + sum(self._transactions)
    
    def handle_transaction(self, transaction_amount: int) -> str:
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        
        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"
    
    def add_transaction(self, amount) -> str:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        
        return self.handle_transaction(amount)
    
    def __str__(self) -> str:
        return f"Account of {self.owner} with starting amount: {self.amount}"
    
    def __repr__(self) -> str:
        return f"Account({self.owner}, {self.amount})"
    
    def __len__(self) -> int:
        return len(self._transactions)
    
    def __getitem__(self, idx: int):
        return self._transactions[idx]
    
    def __reversed__(self):
        return reversed(self._transactions)
    
    def __eq__(self, other) -> bool:
        return self.balance == other.balance
    
    def __gt__(self, other) -> bool:
        return self.balance > other.balance
    
    def __ge__(self, other) -> bool:
        return self.balance >= other.balance
    
    def __add__(self, other) -> "Account":
        owner = f"{self.owner}&{other.owner}"
        amount = self.amount + other.amount
        transactions = self._transactions + other._transactions
        return Account(owner, amount, transactions)
