x = int(input("Nilai x: "))
y = int(input("Nilai y: "))

if (x > 0 and y > 0):
    print(f"Sits at Q1")
elif (x < 0 and y > 0):
    print(f"Sits at Q2")
elif (x < 0 and y < 0):
    print(f"Sits at Q3")
elif (x > 0 and y < 0):
    print(f"Sits at Q4")
if (x == 0 and y == 0):
    print(f"Sits at the center")
else: print(f"Location unknown! Try again!")
