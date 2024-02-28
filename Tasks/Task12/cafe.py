def find_total_value():     #Made the calculation of total value a function to make my code modular.
    total_value = 0
    for i in menu:
        total_value += stock[i]*prices[i]
    return total_value

menu = ["water", "bread", "cappuccino", "caramel coffee"]
#I would use a better method of creating these dictionaries but as I am not planning on changing the list, this works fine.
stock = {menu[0]: 67,
         menu[1]: 120,
         menu[2]: 60,
         menu[3]: 4}

prices = {menu[0]: 3.09,
          menu[1]: 2.50,
          menu[2]: 5.40,
          menu[3]: 4.50}

print(f"Total value of stock is: £{find_total_value()}")
