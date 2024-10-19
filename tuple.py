dList = [1, 2, 3, 4]
dTuple = (1, 2, 3, 4)
dSet = {"A", "B", "C", "D"}
print(f"List = {dList}")
print(f"Tuple = {dTuple}")
print(f"Set = {dSet}")
print("List no. 0: {dList[0]}")
print("Tuple no. 0: {dTuple[0]}")
print("Set no. 0: {dSet[0]}")
#print("Set no. 0: {dSet[0]}") #set: Can't index LOL
print("-"*25, "Insert data here")
dList.insert(0, "Start")
print(f"Data List = {dList}")
dSet.add("First")
print(f"Data Set = {dSet}")
print("-"*25, "Update time!")
dList[1] = "Start;"
print(f"Data List = {dList}")
print("-"*25, "DELETE")
dList.remove = ("Start")
print(f"Data List = {dList}")
dSet.remove("First")
print(f"Data Set = {dSet}")
print("-"*25, "Loop time!")

for i in dSet:
    print(f"Data set: {i}")

for z in dTuple:
    print(f"Data tuple: {z}")