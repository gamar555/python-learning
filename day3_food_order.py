import datetime

# 🧍 Step 1: Get customer's name and current date/time
customer_name = input("Please enter your name: ")
now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

# 🧾 Step 2: Start building the receipt string
receipt = "🏪 *************** Welcome to the Python Cafe! ***************\n"
receipt += f"👤 Customer Name: {customer_name}\n📅 Date and time: {date_time}\n\n"

# 🍽️ Step 3: Menu items
menu = {
    "pizza": 8.5, "burger": 6.5, "salad": 5.0, "soda": 2.0, "fries": 3.0, "dessert": 4.0,
    "pasta": 7.0, "sandwich": 5.5, "wings": 9.0, "steak": 12.0, "tacos": 7.5, "sushi": 10.0,
    "ice cream": 3.5, "coffee": 2.5, "tea": 2.0, "water": 1.0, "juice": 2.5, "cake": 4.5,
    "brownie": 3.0, "pancakes": 5.0, "waffles": 6.0, "omelette": 7.0, "bagel": 2.0
}

# 🧾 Step 4: Show the menu
print("📋 Here is our menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: ${price:.2f}")

# 🛒 Step 5: Collect order
order_items = []
order_quantities = []

while True:
    order = input("\n📝 What would you like to order? (type 'done' to finish): ").strip().lower()
    if order == 'done':
        break
    if order in menu:
        quantity = int(input(f"🧮 How many {order}s would you like? "))
        order_items.append(order)
        order_quantities.append(quantity)
    else:
        print("⚠️ Sorry, we don't have that item on the menu.")

# 💵 Step 6: Print and build receipt
total = 0
receipt += "🍽️ *************** Your Order Receipt ***************\n"

for item, quantity in zip(order_items, order_quantities):
    price = menu[item]
    item_total = price * quantity
    total += item_total
    line = f"{item.capitalize()} x {quantity} @ ${price:.2f} each: ${item_total:.2f}\n"
    print(line)
    receipt += line

receipt += "💳 -------------------------------------------\n"
receipt += f"💰 Total cost: ${total:.2f}\n"

# 💳 Step 7: Ask for payment method
print("\n💳 Payment Methods:\n1. Cash 💵\n2. Card 💳\n3. UPI 📲\n4. Wallet 👜")
payment_choice = input("Please select a payment method (1-4): ").strip()

payment_methods = {
    "1": "Cash 💵",
    "2": "Card 💳",
    "3": "UPI 📲",
    "4": "Wallet 👜"
}

selected_payment = payment_methods.get(payment_choice, "Not specified")

receipt += f"🧾 Payment Method: {selected_payment}\n"
receipt += "🙏 Thank you for visiting the Python Cafe! Have a great day!\n"

# 💾 Step 8: Save to file
with open("receipt.txt", "w", encoding="utf-8") as file:
    file.write(receipt)

print("✅ Receipt saved to receipt.txt")
