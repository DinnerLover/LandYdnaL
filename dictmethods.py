stationdata = {
    "BDG": "Bandung",
    "YGK": "Yogyakarta",
    "PLG": "Palembang",
    "J": "Jakarta"
}
datakopy = stationdata.copy()
stationdata["J"] = "Jambi"
print(f"Station data = {stationdata}")
print(f"datakopy = {datakopy}")
cardata = {
    "Car 1": {
    "Model": "Toyota Sprinter Trueno GT-Apex",
    "Year": "1985",
    "Color": "Red"   
    },
    "Car 2": {
    "Model": "Nissan Silvia Spec-R",
    "Year": "2002",
    "Color": "White"   
    },
    "Car 3": {
    "Model": "Toyota Century",
    "Year": "2002",
    "Color": "British racing green"
    },
    "Car 4": {
    "Model": "Mitsubishi Lancer Evolution IX MR GSR",
    "Year": "2006",
    "Color": "Red"
    },
}
print("-"*25, "Pop")
print(f"Model Data 1 = {cardata ['Car 1']["Model"]}")
print(f"Model Data 2 = {cardata.get ('Car 2')["Model"]}")
print(f"Color Data = {cardata.get ('Car 3').get("Color")}")
cardata2= cardata.copy()
print("-"*25, "Deepcopy")
cardata['Car 4']['Model'] = "BMW M5"
cardata['Car 4']['Year'] = "2007"
cardata['Car 4']['Color'] = "Black"
print(f"Car Data = {cardata}")
print(f"Car Data 2 = {cardata2}")
from copy import deepcopy
cardata3 = deepcopy(cardata)
cardata['Car 1']['Model'] = "Lamborghini Countach"
print(f"Car Data = {cardata}")
print(f"Car Data 3 = {cardata3}")

print("-"*25, "Comprehend this.")
w = "ABC"
D = {i for i in w}
print(f"Data = {D}") #Turn into set, please
D2 = {i: i for i in w}
print(f"Data 2 = {D2}") #Turn into dict, please
D3 = {i: i*3 for i in w}
print(f"Data 3 = {D3}")

e = ["a", "b", "c"]
x = [11, 12, 13]
ex = {e: x**2 for e, x in zip(e, x)}
print(f"EX = {ex}")