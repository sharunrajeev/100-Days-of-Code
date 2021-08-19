from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

main_menu = Menu()
coffee_assistant = CoffeeMaker()
money_handler = MoneyMachine()

end = False
while not end:
    print("Hi there. Am your personal coffee assistant.")
    c_type = input(f"What would you like? {main_menu.get_items()} : ")
    if c_type == 'report':
        coffee_assistant.report()
        money_handler.report()
    elif c_type == 'espresso' or c_type == 'latte' or c_type == 'cappuccino':
        if coffee_assistant.is_resource_sufficient(main_menu.find_drink(c_type)):
            if money_handler.make_payment(main_menu.find_drink(c_type).cost):
                coffee_assistant.make_coffee(main_menu.find_drink(c_type))
        else:
            print('Insufficient funds')
    elif c_type == 'exit':
        print('Have a nice day!')
        end = True
    else:
        print('Wrong input. Crashed. Shutting down.')
        end = True
