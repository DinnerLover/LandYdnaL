print(f"{"CBA Travel"}")
print('''
Destinasi:
1. Prabumulih
2. Muara Enim
3. Lubuklinggau
''')
tujuan = input("Mau kemana? \t: ")
print('''
Kelas:
1. Ekonomi
2. Bisnis
3. Eksekutif
''')
kelas = int(input("Mau kelas mana? \t: "))
jumlah = int(input("Mau berapa tiket? \t: "))
if(tujuan == 2 and kelas == 1):
    promo = input("Ada kode?")
    if promo == 'igs':
        diskon = 0.1
    else:
        diskon = 0
elif(tujuan == 3 and kelas == 3):
    promo = input("Ada kode?")
    if promo == 'igs':
        diskon = 0.1
    else:
        diskon = 0
else:
    diskon = 0
if tujuan == 1:
    if kelas == 1:
        harga = 100000
    elif kelas == 2:
        harga = 400000
    elif kelas == 3:
        harga = 700000
    else:
        harga = 0
elif tujuan == 2:
    if kelas == 1:
        harga = 200000
    elif kelas == 2:
        harga = 500000
    elif kelas == 3:
        harga = 800000
    else:
        harga = 0
elif tujuan == 3:
    if kelas == 1:
        harga = 300000
    elif kelas == 2:
        harga = 600000
    elif kelas == 3:
        harga = 900000
    else:
        harga = 0
print(f"Harga tiket \t: Rp. {harga}")
subtotal = jumlah * harga
print(f"Harga tiket \t: Rp. {subtotal}")
totaldiskon = subtotal * diskon
print(f"Diskon \t: Rp. {totaldiskon}")
totalbayar = subtotal - totaldiskon
print(f"Total bayar \t: Rp. {totalbayar}")