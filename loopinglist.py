dataList = [10, 9, 8, "a", "x"]
for i in range (0, len(dataList)):
    print(f"data no. {i} = {dataList[i]}")
print("-"*25)
for i in dataList:
    print(f"data = {i}")
print("-"*25)
data1= [1, 2, 3, 4, 5, 6] #normal
data2= [i for i in range(1,7)] #comprehension
print(f"data1 = {data1}")
print(f"data2 = {data2}")
data3 = [z*2 for z in range(1,10)] #comprehension
print(f"data3 = {data3}")
data4 = [i for i in range(1,10) if i % 2 == 0]
print(f"data4 = {data4}")
print("-"*25)
emptydata = []
emptydata.append(1)
emptydata.append(2)
emptydata.append(3)
print(f"Empty data = {emptydata}")