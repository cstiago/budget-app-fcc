class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = list()

    def deposit(self, amount, description=str()):
        return 0

    def withdraw(self, amount, description=str()):
        return 0

    def get_balance(self):
        balance = float()

        for operation in self.ledger:
            balance += operation['amount']

        return balance

    def transfer(self, amount, destination):
        return 0

    def check_funds(self, amount):
        return True if amount <= self.get_balance() else False

def create_spend_chart(categories):
    return 0
