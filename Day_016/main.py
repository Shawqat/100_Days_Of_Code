from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker   = CoffeeMaker()
menu = Menu()

def coffee_machine():
    while True:

        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        drink = menu.find_drink(choice)
        if choice == "off":
            break

        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        elif choice not in menu.get_items():
            print("Invalid choice.")
            continue

        if coffee_maker.is_resource_sufficient(drink):
            payment = money_machine.make_payment(drink.cost)
            if payment:
                coffee_maker.make_coffee(drink)


coffee_machine()