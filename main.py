import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category('Food')
food.deposit(100, 'Initial deposit')
food.withdraw(10, 'Purchase 1')
food.withdraw(29.99, 'Purchase 2')

clothing = budget.Category('Clothing')
food.transfer(30, clothing)
clothing.withdraw(10.25, 'Purchase 1')
clothing.withdraw(15, 'Purchase 2')

auto = budget.Category('Auto')
auto.deposit(500, 'Initial deposit')
auto.withdraw(125.50, 'Purchase 1')
auto.withdraw(9.99, 'Purchase 2')

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))

main(module='test_module', exit=False)
