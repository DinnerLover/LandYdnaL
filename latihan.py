print(f"{'CBA Travel':_^35}")
print('''
Destinasi:
1. Prabumulih
2. Muara Enim
3. Lubuklinggau
''')
# perkalian = *
print("-"*30)
selection = input("Mau kemana? (1/2/3) \t: ")
ticket = int(input("Mau berapa tiket? \t: "))

if selection == "1":
    ticket_price = 150000
elif selection == "2":
    ticket_price = 300000
elif selection == "3":
    ticket_price = 400000
else: ticket_price = 0
total = ticket_price * ticket
print(f"Harga ticket: Rp. {ticket_price}")
print(f"Total: Rp. {total}")
