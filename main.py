
#TASK 1 - A

# a)
customer = input("Enter customer name: ")
check = True
count = 0
subtotal = 0

while check == True:
    product = input("Enter product name: ")
    if product == "done":
        check = False
    else:
        price = float(input("Enter price per unit (KZT): "))
        count = count + 1
        subtotal += price


# (b) and (c)

print("=" * 30)
print("         SHOP RECEIPT")
print("=" * 30)

print(f"Customer: {customer.upper()}")
print(f"Items: {count}")
print(f"Price: {price}" + " KZT")

print("-" * 30)

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
