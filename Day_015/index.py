from data import MENU, resources, profit

def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]

    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False

    return True


def process_coins():
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (
        quarters * 0.25
        + dimes * 0.10
        + nickels * 0.05
        + pennies * 0.01
    )

    return total


def is_payment_successful(money_received, drink_cost):
    global profit

    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    change = money_received - drink_cost
    print(f"Here is ${change:.2f} in change.")

    profit += drink_cost

    return True


def make_coffee(drink, ingredients):
    ingredients = MENU[drink]["ingredients"]

    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here is your {drink} Enjoy!")


def print_report():
    print(f"Water : {resources['water']}ml")
    print(f"Milk  : {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money : ${profit:.2f}")


def coffee_machine():
    while True:

        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

        if choice == "off":
            break

        if choice == "report":
            print_report()
            continue

        if choice not in MENU:
            print("Invalid choice.")
            continue

        if check_resources(choice):

            payment = process_coins()

            if is_payment_successful(payment,MENU[choice]["cost"]):
                make_coffee(choice)