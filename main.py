from base import MENU
from base import resources
from art import logo


def chose_number():
    while True:
        number = input("Press the number: ")
        if number == "off":
            print("Coffee Machine is shutting down.\n****Goodbye****")
            exit()
        elif number == 'report':
            report()
        elif number == '1':
            return 'espresso'
        elif number == '2':
            return 'latte'
        elif number == '3':
            return 'cappuccino'
        else:
            print("You chose wrong number. Try again, please.")


def check_resources(type_of_coffee):
    for item in type_of_coffee:
        if type_of_coffee[item] >= resources[item]:
            print(f"Not enough {item}. Please, fill the tank.")
            exit()
        return True


def transaction(type_of_coffee):
    print(f"{type_of_coffee.capitalize()} costs {MENU[type_of_coffee]['cost']}$")
    print("You can pay in quarters, dimes, nickels and pennies")
    while True:
        payment = int(input("How many quarters do you put?: ")) * 0.25
        payment += int(input("How many dimes do you put?: ")) * 0.10
        payment += int(input("How many nickels do you put?: ")) * 0.05
        payment += int(input("How many pennies do you put?: ")) * 0.01
        if payment < MENU[type_of_coffee]['cost']:
            print("\n****Not enough funds****\n")
        else:
            change = round(payment - MENU[type_of_coffee]['cost'], 2)
            money = MENU[type_of_coffee]['cost']
            if change > 0:
                print(f"\n****Please, take you change {change}$****")
                return money
            else:
                return money


def make_coffee(type_of_coffee):
    resources['water'] -= MENU[type_of_coffee]['ingredients']['water']
    resources['coffee'] -= MENU[type_of_coffee]['ingredients']['coffee']
    if type_of_coffee == 'espresso':
        return
    resources['milk'] -= MENU[type_of_coffee]['ingredients']['milk']


def end():
    finish = False
    while not finish:
        shut_down = int(input('Press 1 to more coffee.\nPress 2 to shutdown.\n'))
        if shut_down == 1:
            return
        elif shut_down == 2:
            print("Goodbye.")
            return True
        else:
            print("You chose wrong number. Try again, please.")


def report():
    print(f"Water: {resources['water']} ml'")
    print(f"Milk: {resources['milk']} ml'")
    print(f"Coffee: {resources['coffee']} ml'")
    print(f"Money: {profit} $")


profit = 0
off = False
while not off:
    print(logo)
    order = chose_number()
    ingredients = MENU[order]['ingredients']
    check_resources(ingredients)
    profit += transaction(order)
    make_coffee(order)
    print("\n\n****Enjoy your coffee!****")
    print("\n\nDo you want order one more coffee or shutdown coffee machine?")
    off = end()
