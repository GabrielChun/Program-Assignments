menu = {'Pizza': 2.99,
        'Burger': 3.99,
        'Hot Dog': 1.99,
        'Cheese': 0.59,
        'Ice Cream': 1.49,
        'Churro': 0.79,
        'Soda': 0.89}

def total_price(*items):
    total = 0
    not_found = []

    for item in items:
        if item in menu:
            total += menu[item]
        else:
            not_found.append(item)
    if not_found:
        return f"The total price is {total:.2f}. Missing items: {', '.join(not_found)}"
    else:
        return f"The total price is {total:.2f}"
    
user_input = input("Enter menu items separated by commas: ")
item_list = [item.strip() for item in user_input.split(',')]
print(total_price(*item_list))

def price_difference (item1, item2):
    missing = []
    if item1 not in menu:
        missing.append(item1)
    if item2 not in menu:
        missing.append(item2)
    if missing:
            return f"Item(s) not found in menu: {', '.join(missing)}"
    price1 = menu[item1]
    price2 = menu[item2]
    difference = abs(price1 - price2)
    if price1 > price2:
        more_expensive = item1
        cheaper = item2
    elif price2 > price1:
        more_expensive = item2
        cheaper = item1
    else:
        return f"{item1} and {item2} cost the same: ${price1:.2f}"
    
    return f"The difference between {item1} and {item2} is ${difference:.2f}. {more_expensive} is more expensive than {cheaper}"

item1 = input("Enter the first menu item you wish to compare: ").strip()
item2 = input("Enter the second menu item you wish to compare: ").strip()
print(price_difference(item1, item2))

def inflation (multiplier, *items):
    not_found = []
    updated_items = []
    for item in items:
        if item in menu:
            menu[item] = round(menu[item] * multiplier, 2)
            updated_items.append(item)
        else:
            not_found.append(item)

    if not_found:
        print(f"These items were not found in the menu: {', '.join(not_found)}")
    if updated_items:
        print(f"The following items were updated: {', '.join(updated_items)}")
    else:
        print("No items were updated")

    return menu
    
user_items = input("Enter the menu items to inflate separated by commas: ")
user_inflate = input("Enter the multiplier: ")
item_list = [item.strip() for item in user_items.split(',')]
try:
    multiplier = float(user_inflate)
    updated_menu = inflation(multiplier, *item_list)
    print("Updated menu: ")
    print(updated_menu)
except ValueError:
    print("Invalid multiplier. Please enter a number like 1.5")