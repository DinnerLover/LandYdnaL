print(f" {'Receipt':_^80} ")
price = int(input ("Item price\t:"))
quantity = int(input ("Quantity\t\t:"))
subtotal = price * quantity
print(f"Subtotal\t: Rp. {subtotal:>15}")
if quantity >= 5:
    discount = 0.1 * subtotal
else: 
    discount = 0

total = subtotal - discount
print(f"Discount\t\t: Rp. {discount:>15}")
print(f"Total\t\t: Rp. {total:>15}")