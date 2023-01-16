class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = list()

    def deposit(self, amount, description=str()):
        return 0

    def withdraw(self, amount, description=str()):
        return 0

    def get_balance(self):
        return 0

    def transfer(self, amount, destination):
        return 0

    def check_funds(self, amount):
        return 0

def create_spend_chart(categories):
    return 0
