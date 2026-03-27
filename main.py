#TASK 1 - A

# a)
customer = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input("Enter price per unit (KZT): "))
quantity = int(input("Enter quantity: "))

# (b) and (c)

print("=" * 30)
print("         SHOP RECEIPT")
print("=" * 30)

print(f"Customer: {customer}")
print(f"Product: {product}")
print(f"Price: {price}" + " KZT")
print(f"Quantity: {quantity}")

print("-" * 30)
subtotal = price * quantity

if subtotal > 5000:
    print(f"Subtotal: {subtotal}" + " KZT")
    discount = subtotal * 0.1
    total = subtotal - discount
    print(f"Discount: {discount}" + " KZT")
    print(f"Total: {total}" + " KZT")
else:
    discount = 0
    total = subtotal
    print(f"Total: {subtotal}" + " KZT")

# d)
print("-" * 30)
print("Discount applied: ", subtotal > 5000)
print("Paid more than 3000: ", total > 3000)
print("=" * 30)