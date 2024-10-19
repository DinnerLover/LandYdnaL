placedata = {
    "PLG": "Palembang",
    "ME": "Muara Enim",
    "BL": "Bengkulu"
}
for i in placedata:
    print(f"Data = {i}")
print("-"*25)
for z in placedata.keys():
    print(f"Key data = {z}")
print("-"*25)
for z in placedata.values():
    print(f"Value data = {z}")
print("-"*25)
for k, v in placedata.items():
    print(f"Key data = {k} and value data = {v}")

