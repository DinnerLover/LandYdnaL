# function = A statement containing a certain task that can be used indefinitely.
def greeting():
    print("Good morning!")
def limit():
    print("-"*25)
limit()
greeting()
limit()

def myname(name):
    print(f"My name is {name}.")
myname("Barkins")

limit()

def biodata(name, age, address, birthday):
    print(f"My name is {name}. I'm currently {age} years old, I currently live in {address}, and I was born on {birthday}.")
biodata("C.K.", 22, "Forks", "April 8, 2002")

def massalforce(m, g):
    print(f"Massal force ({g}) = {m*g} N")
limit()
m = int (input ("Insert mass here ="))
g = int (input ("Insert gravitation here = "))
massalforce(m, g)
limit()
def mathtyme(a, b):
    endresult = a + b
    return endresult

endresult = mathtyme(8, 90)
print(f"1. {endresult}")
print(f"2. {mathtyme(9, 14)}")

limit()
def massalforce2(m, g):
    return(m * g)
print(f"Massal force 2 ={massalforce2(8, 10)}N")
limit()
def random(DATA):
    D = DATA.copy()
    for i in D:
        print(f"I'm looking for {i}.")
dList = ["L", "$290", "Elex", "$150"]
random(dList)
limit()
def mymath(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    modulo = a % b
    return addition, subtraction, multiplication, division, modulo
print(f"Result = {mymath (8, 8)}")
addition, subtraction, multiplication, division, modulo = mymath (8, 8)
print(f"R1 = {addition}")
print(f"R2 = {subtraction}")
print(f"R3 = {multiplication}")
print(f"R4 = {division}")
print(f"R5 = {modulo}")