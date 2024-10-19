'''
    MTK di Python:
    1. Penjumlahan ( + )
    2. Pengurangan ( - )
    3. Perkalian ( * )
    4. Pembagian ( / )
    5. Pangkat ( ** )
    6. Sisa bagi ( % )
    7. Hasil bagi - lantai pembagian ( // )
'''

a = int ( input( "Angka 1 = "))
b = int ( input( "Angka 2 = "))
print( "1. Hasil tambah : ", a + b)
print( "2. Hasil kurang : ", a - b)
print( "3. Hasil kali : ", a * b)
print( "4. Hasil bagi : ", a / b)
print( "5. Hasil pangkat : ", a ** b)
print( "6. Hasil bagi(%) : ", a / b)
print( "7. Sisa bagi (//) : ", a // b)

print("-"*25)
c = 7
d = 6
e = 5
result = ( c + d )**e * e*c - c
print( result )

print("-"*25)