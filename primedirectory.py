print("_____ Prime numbers _____")
min = int(input ("Insert min. number here = "))
max = int(input ("Insert max. number here = "))
dataPrime = dict()
for i in range(min, max + 1):
    prime = True
    if(i == 0 or i == 1):
        prime = False
    for z in range(2, i):
        if i % z == 0:
            prime == False
        elif i == 1:
            prime == False
        if(prime):
            dataPrime[i] = i
print(dataPrime.values())