umur = int(input("Umur Anda: "))
if umur >= 17 :
    menikah = input("Menikah? (Y/T): ").upper()
    if menikah == "Y":
        print("Anda bisa ikut pemilu.")
    elif menikah == "T":
        print("Anda tidak bisa ikut pemilu.")
    else:
        print("Eh? Apa tadi?")
else: 
    print("Anda bisa ikut pemilu.")