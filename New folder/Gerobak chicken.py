print(" " * 15,"GEROBAK FIRED CHICKEN", " " * 15)
print("-" * 52)
#input
print("GEROBAK FRIED CHICKEN")
print("_________________________________________")
print("Kode     Jenis Potong    Harga")
print("_________________________________________")
print("D        DADA            Rp.2500")
print("P        PAHA            Rp.2000")
print("S        SAYAP           Rp.1500")
print("__________________________________________")
banyak=int(input("banyak Jenis : "))
#perulangan Input
listkode=[]
listjumlah=[]
for i in range(banyak):
    print("\ndata ke-",i+1)
    kode=input("Kode Potong [D/P/S] :")
    listkode.append(kode)
    jumlah=int(input("jumlah Beli :"))
    listjumlah.append(jumlah)
#jumlahbayar
jmlh_byr = input("\nJumlah Bayar : ")
#output
print("         GROBAK FRIED CHICKEN")
print("-" * 45)
print("No    Jenis    Harga    Banyak    Jumlah")
print("      Potong   Satuan   Beli      Harga ")
print("-" * 45)

#proses oprasi
total_beli=0
for i in range(banyak):
    #fungsi IF
    if listkode[i]=='D' or listkode[i]=='d':
        jenis_ptg="DADA"
        harga=2500
    elif listkode[i]=='P' or listkode[i]=='p':
        jenis_ptg="PAHA"
        harga=2000
    elif listkode[i]=='S' or listkode[i]=="s":
        jenis_ptg="SAYAP"
        harga=1500
    else:
         jnsptg="-"
         harga=0
    #Subtotal
    subtotal=harga*listjumlah[i]
    #SUM total
    total_beli=total_beli+subtotal
    #ppn
    ppn=total_beli*0.1
    #oprasi total bayar
    total_bayar=total_beli+ppn
    #kembalian
    kembali=int(jmlh_byr)-int(total_bayar)

    print(i+1,"    ",jenis_ptg,"    ",harga,"    ",listjumlah[i],"    ",format(subtotal,',d'))

print("-" * 45)
print("                   Total pembelian     Rp.",format(total_beli,',d'))
print("                   ppn                 Rp.",format(round(ppn),',d'))
print("                   Total bayar         Rp.",format(round(total_bayar),',d'))
print("________________________________________________-")
print("                   kembali             Rp.",format(round(kembali),',d'))
print("Terimakasih sudah berbelanja di GROBAK FRIED CHICKEN")
print("Kami Tunggu Kedatangan Anda Kembali.")