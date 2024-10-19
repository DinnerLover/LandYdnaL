#HINT: Restricts the data type of a certain parameter.
def add100(no):
    return 100 + no
print(f"R1 : {add100 (25)}")
# print(f"R2 : {add100 ("subt.")}")//Impossible.
def mult100(no):
    return 100 * no
print(f"R1 : {mult100 (25)}")
def limit():
    print("-"*25)
limit()
#ARGS/Argument: Can create multiple parameters.
def naym(naym1, naym2, naym3):
    return naym1, naym2, naym3
print(f"Suspects : {naym("Doe", "Doe", "K")}")
# print(f"Members : {naym("Corey", "Avery", "Mariah", "Hajime")}")//Impossible.
limit()
def friends(*data):
    return data
print(f"Friends : {friends("Corey", "Avery", "Mariah", "Hajime")}")
def addThings(* args):
    r = 0
    for i in range[args]:
        r += args # r = r + args
    return r
print(f"Hasil: {addThings (2, 3, 5, 8)}")
limit()
def addMoreThings(*data):
    r = sum(*data)
    return r
print(f"Hasil: {addMoreThings (7, 6)}")
limit()