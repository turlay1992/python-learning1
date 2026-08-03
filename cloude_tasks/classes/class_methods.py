# Практичне завдання: створи клас BankAccount:

# __init__(self, owner: str, balance: float = 0.0) -> None — зберігає власника і баланс
# атрибут класу bank_name: str = "PrivatBank" (спільний для всіх рахунків)
# метод deposit(self, amount: float) -> None — додає суму до балансу
# метод withdraw(self, amount: float) -> None — знімає суму, але якщо недостатньо коштів — нічого не робить 
# (або друкує повідомлення; винятки розберемо в пункті 9)
# @classmethod from_zero(cls, owner: str) -> "BankAccount" — альтернативний конструктор, що створює рахунок з балансом 0
# @staticmethod is_valid_amount(amount: float) -> bool — перевіряє, що сума > 0

class BankAccount:
    bank_name: str = 'PrivatBank'
    
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner: str = owner
        self.balance: float = balance
        
    def deposit(self, amount: float) -> None:
        if BankAccount.is_valid_amount(amount):
            self.balance += amount
        
    def withdraw(self, amount: float) -> None:
        if BankAccount.is_valid_amount(amount):
            if self.balance < amount:
                error_message: str = f'Hello {self.owner}! Not enough money on your balance!'
                raise RuntimeError(error_message)
            else:
                self.balance -= amount
            
    @classmethod
    def from_zero(cls, owner: str) -> 'BankAccount':
        return cls(owner)
    
    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        return amount > 0
    
if __name__ == "__main__":
    first_acc = BankAccount('Roman', 25)
    first_acc.deposit(25)
    first_acc.withdraw(30)
    try:
        first_acc.withdraw(30)
    except RuntimeError as e:
        print(f'Exception: {e}')

    second_acc = BankAccount.from_zero('Olena')
    second_acc.deposit(20)
    try:
        second_acc.withdraw(50)
    except RuntimeError as e:
        print(f'Operation(withdraw) was failed. {e}')
    