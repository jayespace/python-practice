from menu import MENU, resources


def ingredient(choice):
    return MENU[choice]["ingredients"]


def is_enough_ingre(water, milk, coffee):
    if water <= resources['water'] and milk <= resources[
            'milk'] and coffee <= resources['coffee']:
        return True
    else:
        return False


def insert_coins(total):
    print('Please insert coins.')
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


collected_money = 0
is_on = True

while is_on:

    choice = input(
        "  What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        is_on = False

    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${collected_money}")
    else:
        chosen_ingre = ingredient(choice)
        water = chosen_ingre['water']
        milk = chosen_ingre['milk']
        coffee = chosen_ingre['coffee']

        check = is_enough_ingre(water, milk, coffee)

        if check == True:
            input_dollar = insert_coins(collected_money)
            price = MENU[choice]['cost']

            if input_dollar < price:
                print(f"Sorry that's not enough money. Money refunded.")
            else:
                if input_dollar == price:
                    print(f"Here is your {choice} ☕️. Enjoy!")
                    collected_money += input_dollar
                else:
                    change = round(input_dollar - price, 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {choice} ☕️. Enjoy!")

                resources['water'] -= water
                resources['milk'] -= milk
                resources['coffee'] -= coffee
                collected_money += input_dollar

        else:
            print(f"Sorry there is not enough {choice}.")
