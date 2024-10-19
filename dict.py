#Create dictionary
dDict1 = {
    "1": "Ice", 
    "2": "Coffee", 
    "3": "Igloo"
}
print(f"Data1 = {dDict1}")
dDict2 = dict(
    A = "Snack", 
    B = "Incense", 
    Z = "Hail"
)
print(f"Data2 = {dDict2}")
print("-"*25)
print(f"Data key 3 of dict 1 = {dDict1['3']}")
print(f"Data key Z of dict 2 = {dDict2['Z']}")
print(f"Data key B of dict 2 = {dDict2.get('B')}")
print(f"Data key C of dict 2 = {dDict2.get('C')}")
print(f"Data key D of dict 2 = {dDict2.get('D', 'NO DATA FOUND LOL')}")
dCar = dict(
    Brand = "Subaru",
    Model = "Legacy",
    Trim = "B4",
    MY = "2008",
    MT = True,
    Color = ['Navy blue', 'White', 'Black'],
)
print("-"*25)
print(f"Model = {dCar ['Model']}")
print(f"Manual? {dCar ['MT']}")
print(f"Model year = {dCar ['MY']}")
print(f"Color = {dCar.get ('Color')[2]}")
dMovie = dict(
    Title = "Another Day in the Office",

    Genre = "Animated comedic action-adventure, with some romance and tragedy on the side",

    Rating = "R",

    Released = "20/5/2024",

    Length = "2 hours and 5 minutes",

    Starring = "Christian Bale, Milla Jovovich, Rick Hunter, Maryke Hendrikse, Joe Taslim, Iko Uwais, Jennifer Hale",

    GudScenes = "The Gun Kata Duel Between Jovovich and Bale"
)
print(f"Movie Data = {dMovie}")
#update:
print(f"Title = {dMovie.get ('Title')}")
dMovie['Title'] = "Good Movie?"
print(f"New Title = {dMovie.get ('Title')}")
print(f"Released = {dMovie.get ('Released')}")
dMovie.update(Released = 2022)
print(f"New release date = {dMovie.get ('Released')}")
dMovie['Starring'] = "Trevor Devall"
print(f"Movie Data = {dMovie}")
#delete:
del dMovie['Title']
print(f"New Movie Data = {dMovie}")
dMovie.clear()
print(f"New NEW Movie Data = {dMovie}")
print("-"*25)
bioData = dict(
    Name = "Vanessa Hawkeye",
    Birthday = "15/4/1977",
)
print(f"Biodata = {bioData}")
bioData["Name"]
bioData["Birthday"]
bioData.update(Bloodtype = "A-")
print(f"New Biodata = {bioData}")