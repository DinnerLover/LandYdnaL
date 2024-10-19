print("___________manual")
print("$")
print("$$")
print("$$$")
print("$$$$")
print("$$$$$")

print("___________for loop:")
for i in range(1, 6):
    print(f"$"*i)
print("___________for while: 1:")
i = 1
while i  < 8:
    print(f"$"*i)
    i += 1
print("___________for while: 2:")
i = 1
while True:
    print(f"$"*i)
    if i ==5:
        break
    i += 1
print("___________Method 1")
i = 1
while i < 10:
    print (f"$"*i)
    i += 2
print("___________Method 2")
i = 12
z = 1
while True:
    print (f"$"*i, "¥"*z)
    if i == 0:
        break
    i -= 1
    z += 1
print("___________Method 3")
i = 12
z = 1
while True:
    print (f" "*i, "¥"*z)
    if i == 0:
        break
    i -= 1
    z += 1
    