# Практичне завдання: створи клас BankAccount:

# __init__(self, owner: str, balance: float = 0.0) -> None — зберігає власника і баланс
# атрибут класу bank_name: str = "PrivatBank" (спільний для всіх рахунків)
# метод deposit(self, amount: float) -> None — додає суму до балансу
# метод withdraw(self, amount: float) -> None — знімає суму, але якщо недостатньо коштів — нічого не робить 
# (або друкує повідомлення; винятки розберемо в пункті 9)
# @classmethod from_zero(cls, owner: str) -> "BankAccount" — альтернативний конструктор, що створює рахунок з балансом 0
# @staticmethod is_valid_amount(amount: float) -> bool — перевіряє, що сума > 0


# Практичне завдання. Повернись до свого класу BankAccount з пункту 6 
# і доопрацюй його:

# Створи два власні винятки: InsufficientFundsError (недостатньо коштів — 
# з атрибутами owner, requested, available) та InvalidAmountError (сума ≤ 0). 
# Заміни в withdraw виклик RuntimeError на InsufficientFundsError, 
# і зроби так, щоб deposit/withdraw тепер підіймали InvalidAmountError, 
# коли сума невалідна, замість того щоб мовчки нічого не робити. 
# Далі напиши невеликий тестовий сценарій із кількома викликами, 
# який ловить обидва типи винятків окремо (різні except), 
# використовує else для повідомлення про успішну операцію і finally, 
# яке завжди друкує щось типу "Операція оброблена". 
# 
# І окремо — маленький приклад на raise ... from ...: наприклад, функція, 
# яка парсить рядок на суму (float(raw)), і якщо ValueError, підіймає твій 
# InvalidAmountError з from e, щоб показати ланцюжок причин.

from cloude_tasks.exceptions.examples import InsufficientFundsError, InvalidAmountError
from pathlib import Path

class BankAccount:
    bank_name: str = 'PrivatBank'
    
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner: str = owner
        self.balance: float = balance
        
    def deposit(self, amount: float | str) -> None:
        amount = BankAccount.validate_amount(amount)
        self.balance += amount
    
    def withdraw(self, amount: float | str) -> None:
        amount = BankAccount.validate_amount(amount)
        if self.balance < amount:
            raise InsufficientFundsError(self.owner, amount, self.balance)
        else:
            self.balance -= amount
            
    @classmethod
    def from_zero(cls, owner: str) -> 'BankAccount':
        return cls(owner)
    
    @staticmethod
    def validate_amount(amount: float | str) -> float:
        try:
            amount = float(amount)
        except (TypeError, ValueError) as e:
            raise InvalidAmountError() from e
        if amount <= 0:
            raise InvalidAmountError()

        return amount

def save_accounts(accounts: list[BankAccount], path: Path) -> None:
    with open(path, 'w', encoding='utf-8') as file:
        for account in accounts:
            file.write(f'{','.join([account.owner, str(account.balance)])}\n')
            
def load_accounts(path: Path) -> list[BankAccount]:
    accounts: list[BankAccount] = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            owner, balance = line.strip().split(',')
            accounts.append(BankAccount(owner, float(balance)))
    return accounts     
    
if __name__ == "__main__":
    BASE_DIR: Path = Path.cwd()
    TARGET_DIR: Path = BASE_DIR / 'src' / 'cloude_tasks' / 'classes'
    TARGET_FILE: Path = TARGET_DIR / 'bank_accounts.txt'

    account_owner_names: list[str] = ['Sergey', 'Igor', 'Tanya', 'Mikhael', 'Lena', 'Mark']
    account_owner_balances: list[float] = [26, 34, 76, 23, 65]
    
    account_owners: list[BankAccount] = []
    for i in range(len(account_owner_names)):
        account_owners.append(
            BankAccount(
                account_owner_names[i],
                account_owner_balances[i])
        )
    
    first_acc = BankAccount('Roman', 25)
    try:
        first_acc.deposit(25)
        first_acc.withdraw('30')
        first_acc.withdraw('d30')
        first_acc.deposit(5)
        first_acc.withdraw(30)
    except InsufficientFundsError as e:
        print(f'Помилка: {e}')
    except InvalidAmountError as e:
        print(f'Помилка: {e}')
    except RuntimeError as e:
        print(f'Невідома помилка: {e}')
    else:
        print(f'Операція успішна!')
    finally:
        print(f'Операція оброблена!')
        
        
    # second_acc = BankAccount.from_zero('Olena')
    # second_acc.deposit(20)
    # try:
    #     second_acc.withdraw(50)
    # except RuntimeError as e:
    #     print(f'Operation(withdraw) was failed. {e}')
    