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
c = int ( input( "Angka 3 = "))
Hasil_1 = a * b - c
Hasil_2 = a + b / 23 // ( a + c ) * Hasil_1
Hasil_3 = 127 + ( a - c + b ) % Hasil_2**Hasil_1 

print( "1. Hasil 1 : ", Hasil_1)
print( "2. Hasil 2 : ", Hasil_2)
print( "3. Hasil 3 : ", Hasil_3)
