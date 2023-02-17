class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
    
    def __str__(self):
        lines = str()
        sum = float()

        title = self.name
        title = title.center(30, '*')

        for operation in self.ledger:
            lines += operation['description'][:23].ljust(23) + format(operation['amount'], '.2f')[:7].rjust(7) + '\n'
            sum += operation['amount']

        total = 'Total: ' + format(sum, '.2f')
        string = '\n'.join([title, lines[:-1], total])

        return string

    def deposit(self, amount, description=str()):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=str()):
        enough_funds = bool(self.check_funds(amount))

        if enough_funds:
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
        
        return enough_funds

    def get_balance(self):
        balance = float()

        for operation in self.ledger:
            balance += operation['amount']

        return balance

    def transfer(self, amount, destination):
        enough_funds = bool(self.check_funds(amount))
        
        if enough_funds:
            self.withdraw(amount, 'Transfer to ' + destination.name)
            destination.deposit(amount, 'Transfer from ' + self.name)
        
        return enough_funds

    def check_funds(self, amount):
        return True if amount <= self.get_balance() else False

def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    label = 100
    bars = list()
    expenses = list()

    while label >= 0:
        bars.append([label, str(label).rjust(3) + '|'])
        label -= 10
    
    for index, category in enumerate(categories):
        expenses.append(0)
        
        for operation in category.ledger:
            if operation['amount'] < 0:
                expenses[index] += operation['amount'] * (-1)

    return chart
