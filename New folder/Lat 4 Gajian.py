print("       Progam Hitung Gaji Karyawan      ")
print("      -----------------------------     ")

# Data tunjangan jabatan
tunjanganjabatan = {
    1: 0.05,  
    2: 0.1,   
    3: 0.15}
# Data tunjangan pendidikan
tunjanganpendidikan = {
  "SMA": 0.025,  
  "D1": 0.05,    
  "D3": 0.2,     
  "S1": 0.3}
# Gaji pokok per bulan
gajipokok = 300000
# Honor lembur per jam
honorlembur= 3500
# Input data karyawan
nama = input("Nama Karyawan: ")
golongan = int(input("Golongan Jabatan (1/2/3): "))
pendidikan = input("Pendidikan (SMA/D1/D3/S1): ")
jam_kerja = int(input("Jumlah jam kerja: "))

# Hitung tunjangan jabatan
if golongan=="1" :
    tunjanganjabatan= 0.05 * gajipokok
elif golongan=="2" :
    tunjanganjabatan= 0.1 * gajipokok
else:
    tunjanganjabatan= 0.15 * gajipokok

# Hitung tunjangan pendidikan
if pendidikan=="SMA" :
    tunjanganpendidikan= 0.025 * gajipokok
elif pendidikan=="D1" :
    tunjanganpendidikan= 0.05 * gajipokok
elif pendidikan=="D3" :
    tunjanganpendidikan= 0.2 * gajipokok
else :
    tunjanganpendidikan= 0.3 * gajipokok

# Hitung honor lembur
if jam_kerja > 8:
    lembur = (jam_kerja - 8) * honorlembur
else:
    lembur = 0

# Hitung total gaji
total_gaji = gajipokok + tunjanganjabatan + tunjanganpendidikan + lembur

# Tampilkan rincian gaji karyawan
print("------------------------------------------------")
print("Karyawan yang bernama " , str(nama))
print("Honor yang diterima")
print(    "Tunjangan Jabatan      Rp.", tunjanganjabatan)
print(    "Tunjangan Pendidikan   Rp.", tunjanganpendidikan)
print(    "Honor Lembur           Rp.", lembur)
print(    "                          ____________ +")
print(    "Total Gaji                 Rp ", total_gaji)