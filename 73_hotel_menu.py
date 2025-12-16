menu = {
    'Coffee':50,
    'Burger':80,
    'Pizza' :120,
    'Sandwich':90,
    'Chowmein':70,
}

print("Welcome to Restaurant")
print(" Coffee:50Rs\n Burger:80Rs\n Pizza:120Rs\n Sandwich:90Rs\n Chowmein:70Rs")

order_total = 0

item_1 = input("Enter the name of item of item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!!!")

another_order = input("Do you want to Add another item? (Yes/No): ")
if another_order == "Yes":
    item_2 = input("Enter the second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")

    else:
        print(f"Ordered item {item_2} is not available yet!!!")

print(f"The Total amount of items to pay is {order_total}")