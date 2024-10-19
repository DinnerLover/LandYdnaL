import os
import random
import string
data = dict()
while True:
    os.system("cls")#Windows
    print(f"{"Foreign Languages Taken by Students":-^35}")
    keyF = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    name = input("Name? \t\t")
    klass = input("Class? \t\t")
    flang = input("Foreign language? \t")
    # data[keyF] = {keyF : {'Name K' : name, 'Class K' : klass, 'Foreign Language K' : flang}}
    data[keyF] = {keyF : {'namekey' : name, 'klasskey' : klass, 'flangkey' : flang}}
    option = input("Want to input again? (Y/N): ").lower()
    if option == 'Y':
        break

print("-"*35)
print(f"Key\t Name\t Klass\t F.Lang\t")
print("-"*35)
for key, value in data.items():
    print(f"{key}.t {data[key]['namekey']}\t {data[key]['klasskey']}\t {data[key]['flangkey']}")