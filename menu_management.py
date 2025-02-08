def add_menu_item(menu, item):
   
    if item not in menu:
        menu.append(item)

def remove_menu_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} is not in the menu.")

def check_menu_item(menu, item):
    return f"{item} is available" if item in menu else f"{item} is not available"

menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"

add_menu_item(menu, add_item)
remove_menu_item(menu, remove_item)
availability = check_menu_item(menu, check_item)

print(f"Updated menu: {menu}")
print(f"Availability: {availability}")
