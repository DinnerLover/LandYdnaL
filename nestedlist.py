data1 = [5, 6, 7, [3, 21]]
print(f"index-0 = {data1[0]}")
print(f"index-3 = {data1[3]}")
print(f"index-3,0 = {data1[3][0]}")
data2 =[5, 6, 7, [3, 61], 8, ["A", "Z", "C"], "B"]
print(f"index-0 = {data2[0]}")
print(f"index-3 = {data2[3]}")
print(f"index-5,1 = {data2[5][1]}")
print(f"index-6 = {data2[6]}")
data1[3][0] = 100
print(f"data = {data1}")
data3 = data1.copy()
data2 [5][2] = 100
print(f"data = {data1}")
print(f"data2 = {data2}")
print("-"*30)
print(f"Mem1 = {hex (id (data1))}")
print(f"Mem2 = {hex (id (data2))}")

print("-"*30)
print(f"Mem1[3][0] = {hex (id (data1[3][0]))}")
print(f"Mem2[5][2] = {hex (id (data2[5][2]))}")

print("-"*30)
from copy import deepcopy
data3 = deepcopy( data1 )
data1[3][0] = 100
print(f"data = {data1}")
print(f"data3 = {data3}")