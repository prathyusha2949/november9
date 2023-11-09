inventory_quantity = int(input("enter inventory quantity"))
try:
    user_quantity = int(input("Enter the quantity you want to purchase:"))
    if user_quantity <= 0:
       raise ValueError("Quantity should br a positive number")
    if user_quantity > inventory_quantity:
       raise ValueError(f"Sorry,we have only{inventory_quantity}items in stock.")
    quantity_increase = user_quantity - inventory_quantity
    inventory_quantity = user_quantity
    print(f"product added to the cart.Quantity increased by {quantity_increase}.")
except ValueError as e:
    print(f"Error:{e}")
except ZeroDivisionError:
    print("ZeroDivisonError occured.")
except Exception as e:
    print(f"An unexpected error occured: {e}") 