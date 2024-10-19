print(f"{'CALCULATE FOR ME':_^35}")
print('''
1. Addition [+]
2. Subtraction [-]
3. Multiplication [*]
4. Division [/]
5. Modulo [%]
''')
selection = input("What do you want to do? (1/2/3/4/5)")
print("-"*30)
num1 = int(input("Num 1:"))
num2 = int(input("Num 2:"))

if selection == "1":
    result = num1 + num2
    op = "+"
if selection == "2":
    result = num1 - num2
    op = "-"
if selection == "3":
    result = num1 * num2
    op = "*"
if selection == "4":
    result = num1 / num2
    op = "/"
if selection == "5":
    result = num1 % num2
    op = "%"
else:
    result = 0
    op = "??"

print(f"{num1} {op} {num2} = {result}")