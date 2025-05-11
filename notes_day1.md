#🧠 Day 1 - Python Cafe Menu Ordering App

## ✅ What I Learned
- How to define and use a Python dictionary
- Taking user input with `input()`
- Using loops (`while`) to handle multiple user inputs
- Conditional checks using `if`, `else`
- String formatting using f-strings
- Calculating total cost of ordered items
- Basic receipt generation using loop and formatting

## 🍽️ Project Description
I created a simple terminal-based menu ordering system for a virtual Python Cafe.

The program:
- Displays a menu with item prices
- Takes multiple orders from the user until they type `'done'`
- Handles quantity input for each item
- Calculates and displays a receipt with item-wise cost and the total

## 📌 Key Features
- Menu printed from a dictionary using `.items()`
- Input is made case-insensitive using `.strip().lower()`
- Receipt includes quantity, unit price, and total price for each item

## 🧾 Sample Output
```text
*******************Welcome to the Python Cafe!*******************
Here is our menu:
Pizza: $8.50
Burger: $6.50
...

What would you like to order? pizza
How many pizzas would you like? 2
What would you like to order? soda
How many sodas would you like? 3
What would you like to order? done

***************Your Order Receipt***************
Pizza x 2 @$8.50 each: $17.00
Soda x 3 @$2.00 each: $6.00
***********************************************
Total cost: $23.00