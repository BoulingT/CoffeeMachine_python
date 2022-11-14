from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# power_on = True
# menu = Menu()
# my_maker_machine = CoffeeMaker()
# my_money_machine = MoneyMachine()
#
#
# while power_on:
#     options = menu.get_items()
#     order = input(f"What do you want? ({options}): ")
#     if order == "off":
#         break
#     elif order == "report":
#         my_maker_machine.report()
#         my_money_machine.report()
#     else:
#         drink = menu.find_drink(order)
#         if my_maker_machine.is_resource_sufficient(drink):
#             if my_money_machine.make_payment(drink.cost):
#                 my_maker_machine.make_coffee(drink)
#
#
#
power_on = True

money_machine = MoneyMachine()
machine_maker = CoffeeMaker()
menu = Menu()


def display_report(my_money_machine, my_machine_maker):
    my_money_machine.report()
    my_machine_maker.report()


def check_resources_and_make_coffee(my_machine_maker, my_money_machine, my_drink):
    if my_machine_maker.is_resource_sufficient(my_drink):
        print(f"The price of your {my_drink.name} is ${my_drink.cost}")
        if my_money_machine.make_payment(my_drink.cost):
            my_machine_maker.make_coffee(my_drink)


while power_on:
    options = menu.get_items()
    order = input(f"What do you want? {options}: ")
    if order == "report":
        display_report(money_machine, machine_maker)
    elif order == "off":
        break
    else:
        drink = menu.find_drink(order)
        check_resources_and_make_coffee(machine_maker, money_machine, drink)












































