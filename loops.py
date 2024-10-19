print("_______FOR LOOPS")
# range:
for i in range(10):
    print(f"{i}'s value")
print("-"*30)
for z in range(2, 6):
    print(f"{z}'s value")
print("-"*30)
for x in range(1, 10, 2):
    print(f"{x}'s value")
print("-"*30)
for e in range(1, 10, 2):
    print (f"{e} * 2 = {e * 2}")
else:
    print("Done!")
print("-"*30)
for i in "abcd":
    print (i)
print("-"*30)
for i in ["Cat", "Cow", "Crow"]:
    print (i)
print("_______While loops")
i = 1
while i < 5:
    print(f"{i}'s value")
    i += 1
print("-"*30)
i = 2
z = 5
while i < 10:
    print(f"{i} and {z}'s values")
    i += 2
    z -= 1
print("-"*30)
while True:
    if i == 5:
        break
    i += 1
print("-"*30)
for i in range(5):
    print(f"{i}")
    if i == 3:
        break
print("-"*30)
for z in range (6):
    print(z)
    if z == 3:
        continue
    print("Okay!")