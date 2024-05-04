print(" " * 15,"GEROBAK FIRED CHICKEN", " " * 15)
print("-" * 52)
print("Kode Jenis Potong    Harga")
print("-" * 30)
print('P   Paha     Rp 2000')
print('D   Dada     Rp 2500')
print('S   Sayap    Rp 1500')
print("-" * 30)
harga_ayam ={} 

# Input banyak jenis, Jenis Potong, Banyak beli
bykjenis = int(input("Banyak Jenis :"))
totalbayar = 0

# Perulangan Daftar Jenis Chicken yang dipesan
a = 0
while a < (bykjenis):
    c = a + 1
    jenispotong = input('Kode Potong [D/P/S] :')
    banyakbeli = int(input("Banyak Potong :"))

    if jenispotong in harga_ayam :
        hargaperptg = harga_ayam[jenispotong]
        totalbayar+= banyakbeli * hargaperptg
    else:
        ("Jenis Potong Tidak Valid")

# Menghitung Pajak
pajak = 0,1 * totalbayar

# Total bayar setelah pajak
totalbayar + pajak 

print("Total pembayaran (termasuk pajak 10%): Rp.", totalbayar)