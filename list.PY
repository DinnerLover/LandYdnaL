data1 = [6, 9, 10, 15, 20, 23]
print(f"data = {data1}")
#        0  1  2 3 4
#        -5  -4  -3 -2 -1
data2 = ["I", "G", "S", 7, 10]
print(f"data ke3 = {data2[3]}")
print(f"data ke0 = {data2[0]}")
print(f"data ke4 = {data2[-1]}")
print(f"Banyak data 1 = {len(data1)}")
print(f"Banyak data 2 = {len(data2)}")
print("-"*20, "Extend +")
data1.extend(data2)
print(f"Hasil extend data 1 dan 2 {data1}")
data3 = [3, 2, 1]
data4 = ["x", "y"]
print(f"Hasil data3 + data4 = {data3 + data4}")
print("-"*20, "Repetition time!")
print(f"Hasil data3 * 2= {data3 * 2}")
print("-"*20, "Member in:")
if 4 in data3:
    print("There's data.")
else:
    print("No data!")
print("-"*20, "Loop in list")
for i in data3:
    print(f"data = {i}")
print("-"*20, "Insert list here, please")
print("data 3 = {data3}")
data3.insert(2, "I'm ready!")
print(f"new1. data3 = {data3}")
data3.append("Go!")
print(f"new2. data3 = {data3}")
print("-"*20, "Update time!")
data3[0] = "Start"
print(f"new3. data3 = {data3}")
print("-"*20, "Bye bye!")
data3.remove("Start")
print(f"4. data3 = {data3}")
del data3 [-2]
print(f"5. data3 = {data3}")
data3.pop()
print(f"6. data3 = {data3}")
print("-"*20, "Index & Count list")
data5 = ["a", 1, 2, 3, 1, "a", 1]
print(f"angka 2 list data5 ada di: {data5.index(2)}")
print(f"jumlah a di data5: {data5.count("a")}")
print("-"*20, "Max-min list")
data6= [1, 2, 3, 4]
print(f"data min in data6 = {min(data6)}")
print(f"data min in data6 = {min(data6)}")
data7= ["a", "B", "c", "D"]
print(f"data min in data7 = {min(data7)}")
print(f"data min in data7 = {min(data7)}")
# data8 = [1, 2, 3, 4, "a", "B", "c", "D"] //differing values: Impossible!
print("-"*20, "Sort-reverse list")
data9 = ["I", "F", "A", "C", "K", "T"]
print(f"Before sorting: {data9}")
data9.sort()
print(f"After sorting: {data9}")
print("-"*20, "Copy data list")
data10 = data9
print(f"data 10 = {data10}")
data9[2] = 91
print(f"New1 data 9 = {data9}")
print(f"data 10 = {data10}")
print(f"Adress memory data9 = {hex(id(data9))}")
print(f"Adress memory data10 = {hex(id(data10))}")
data11 = data10.copy()
print(f"Adress memory data11 = {hex(id(data11))}")
data10[0] = 100
print(f"New1 data 10 = {data10}")
print(f"data 11 = {data11}")