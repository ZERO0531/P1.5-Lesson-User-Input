# 1. What is different about how we took user input concerning the price as compared to how input was taken for the item name? There are two differences.
# The float() function converts the user's input into a numerical value, allowing for decimal points. For the price, the input prompt is combined with the input() function, whereas for the item name, the prompt is printed separately before taking input.

# 2. Because it looks better, make your user input for name and quantity also appear on the same line (like price). 
# Moved the input prompts for name and quantity inside the input() functions. 
print("Enter the following information about an item you wish to purchase..")
print()

name = input("The name of the item: ")
price = float(input("The price: $"))
print()
quantity = int(input("How many do you want? "))

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total:}")

# 3. Explain the use of the int() and float() functions. Why are they used? What happens if you remove them? i.e., price = input("The price: $") 
# int() converts input into a whole number. These functions ensure that user input numbers, allowing for mathematical operations. Removing int() or float() can lead to errors in calculations
