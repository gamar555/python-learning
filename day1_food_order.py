menu = {
    "pizza": 8.5,
    "burger": 6.5,
    "salad": 5.0,  
    "soda": 2.0,
    "fries": 3.0,
    "dessert": 4.0,
    "pasta": 7.0,
    "sandwich": 5.5,
    "wings": 9.0,
    "steak": 12.0,
    "tacos": 7.5,
    "sushi": 10.0,
    "ice cream": 3.5,
    "coffee": 2.5,
    "tea": 2.0,
    "water": 1.0,
    "juice": 2.5,
    "cake": 4.5,
    "brownie": 3.0,
    "pancakes": 5.0,
    "waffles": 6.0,
    "omelette": 7.0,
    "bagel": 2.0
}
print("*******************Welcome to the Python Cafe!*******************" "\nHere is our menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: ${price:.2f}")


# initialize an empty list to store the order
order_items = []
order_quantities = []

#Loop to take orders
while True:
    order = input("What would you like to order? (type 'done' to finish) ").strip().lower()
    if order == 'done':
        break
    if order in menu:
        quantity = int(input(f"How many {order}s would you like? "))
        order_items.append(order)
        order_quantities.append(quantity)
    else:
        print("Sorry, we don't have that item on the menu.")

#initialize total cost
total = 0
#print receipt
print("\n***************Your Order Receipt***************")

for item, quantity in   zip(order_items, order_quantities):
    price = menu[item]
    item_total = price * quantity
    total += item_total
    print(f"{item.capitalize()} x {quantity} @ ${price:.2f} each: ${item_total:.2f}")
print("***********************************************")
print(f"Total cost: ${total:.2f}")
