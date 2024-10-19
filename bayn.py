import os
import random
import string
data = dict()
while True:
    os.system("cls")#Windows
    print(f"{"Big Database":-^35}")
    keyF = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    Title = input("Title? \t\t:")
    Year = input("Year it came out? \t\t:")
    Director = input("Director? \t:")
    Distributor = input("Distributor? \t:")
    Genre = input("Genre? \t:")
    Gross = input("Amount of money grossed? \t:")
    # data[keyF] = {keyF : {'tkey': Title, 'ykey': Year, 'wkey': Writer, 'pkey': Publisher, 'gkey': Genre}}
    data[keyF] = {keyF : {'tkey': Title, 'ykey': Year, 'dirkey': Director, 'distkey': Distributor, 'gkey': Genre, 'grkey': Gross}}
    option = input("Want to input again? (Y/N): ").lower()
    if option == 'Y':
        break