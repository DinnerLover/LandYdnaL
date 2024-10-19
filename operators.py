'''
    Operator & = And
    Operator | = Or
    Operator ^ = Xor
    Operator ~ = Not
    Operator << = Left shift
    Operator >> = Right shift
'''
a = int ( input( "Angka 1 = "))
b = int ( input( "Angka 2 = "))
h = ~a
print("Nilai a = ", a, "Binary = ", bin(a))
print("Nilai b = ", b, "Binary = ", bin(b))
print("Nilai a & b = ", bin (a & b))
print("Nilai a | b = ", bin (a | b))
print("Nilai a ^ b = ", bin (a ^ b))
print("~a = ", ~a)
print("Nilai a << 1 = ", bin (a << 1))
print("Nilai a << 2 = ", bin (a << 2))
print("Nilai a << 3 = ", bin (a >> 3))
print("Nilai a << 4 = ", bin (a << 4))
print("Nilai a << 1 = ", bin (a << 100))
print("Nilai a >> 1 = ", bin (a >> 1))
print("Nilai a >> 2 = ", bin (a >> 2))
print("Nilai a >> 3 = ", bin (a >> 3))
print("Nilai a >> 4 = ", bin (a >> 4))
print("Nilai a >> 100 = ", bin (a >> 100))