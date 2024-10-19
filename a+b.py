#Comparison operators: and (&), or (|), xor(^), not(~)

print("-"*35, "And: ")
a = True
b = True
print(a, "&", b, "=", a and b)#True
a = True
b = False
print(a, "&", b, "=", a and b)#False
a = False
b = True
print(a, "&", b, "=", a and b)#False
a = False
b = False
print(a, "&", b, "=", a and b)#False

print("-"*35, "Or: ")
a = True
b = True
print(a, "|", b, "=", a or b)#True
a = True
b = False
print(a, "|", b, "=", a or b)#True
a = False
b = True
print(a, "|", b, "=", a or b)#True
a = False
b = False
print(a, "|", b, "=", a or b)#False

print("-"*35, "Xor: ")
a = True
b = True
print(a, "^", b, "=", a ^ b)#False
a = True
b = False
print(a, "^", b, "=", a ^ b)#True
a = False
b = True
print(a, "^", b, "=", a ^ b)#True
a = False
b = False
print(a, "^", b, "=", a ^ b)#False

print("-"*35, "Not: ")
a = True
b = False
print("not", a, "=", not(a) )#False
print("not", b, "=", not(a) )#True

print("-"*30, "latihan")
a = 21
b = 20
hasil1 = a > b #F
hasil2 = a < b #T
hasilAkhir = a and b
print("a and b = ", hasil1 and hasil2)
print("-"*30, "latihan2")
a = 20
b = 21
hasil1 = a > b #F
hasil2 = a < b #T
hasilAkhir = a and b
print("a and b = ", hasil1 and hasil2 and hasil1)