print(f"{'Traffic Lights':+^30}")

color = input("Insert color: ")
if(color == "Green"):
    print("Go!")
elif(color == "Yellow"):
    print("Are you ready?")
elif(color == "Red"):
    print("Be patient!")
else: print("Colo(u)r unknown! Try again!")