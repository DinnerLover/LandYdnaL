import os
import random
import string
#dictFrom key:
data1 = dict.fromkeys(range(5), "Coding")
print(data1)
print("-"*(25))
dataTuple = ("C", "D", "E")
data2 = dict.fromkeys(dataTuple, "INF")
os.system("cls")#Windows
key1 = random.choice("abcdefghijklmnopqrstuvwxyz")
print(f"Key 1 = {key1}")
alfa = string.ascii_uppercase
print(f"Alfa = {alfa}")
key2 = "".join(random.choice(string.ascii_uppercase) for i in range(3))
print(f"Key 2 = {key2}")