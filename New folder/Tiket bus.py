print ("-------------------------------------------------")
print ("              PENJUALAN TIKET BUS                ")
print ("                      XYZ                        ")
print ("-------------------------------------------------")
Pembeli = input ("Nama Pembeli :")
No_Hp = input ("No. Handphone :")
Jurusan = input ("Kode Jurusan yang dipilih :")


#Proses
if Jurusan=="SBY":
    NamaJurusan="Surabaya"
    Harga=300000
elif Jurusan=="BL":
    NamaJurusan="Bali"
    Harga=350000
else  :
    NamaJurusan="Lampung"
    Harga=500000

#Input Jumlah Beli
jumlah= int(input("Masukkan Jumlah Beli : "))

#proses potongan
if jumlah >=3 :
    potongan=( jumlah*Harga )*0.1
else :
    potongan=0
total=(jumlah*Harga)-potongan

#cetak hasil
print("Nama Pembeli : "+str(Pembeli))
print("No. Handphone : "+str(No_Hp))
print("Kode Jurusan yang dipilih : "+str(Jurusan))
print("Nama Kota Tujuan : "+str(NamaJurusan))
print("Harga : ",+(Harga))
print("Jumlah Beli : ",+(jumlah))
print("------------------------------------")
print("potongan yang didapat : ",+(potongan))
print("Total Bayar : ",+(total))
ubay=int(input("Masukkan Uang Bayar : "))
uangkembali=ubay-total
print("Uang Kembali : ",+uangkembali)
