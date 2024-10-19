num = int(input("Insert number here: "))

prime = True
for i in range(2, num):
    if num % i == 0:
        prime = False
    elif num == 1:
        prime = False
print(f"Prime number or not? : {prime}")