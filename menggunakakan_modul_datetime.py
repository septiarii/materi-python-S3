#https://koding.alza.web.id/menggunakan-modul-datetime/
import datetime

tanggal_saat_ini =datetime.date.today()
print(tanggal_saat_ini) #tanggal pada hari ini akan di tampilkan di layar

saat_ini = datetime.datetime.now()
print(saat_ini) #waku saat ini akan di tampilkan di layar

#menggisi variabel dengan tanggal tertentu
tgl = datetime.date(2019, 7, 31) #tahun, bulan, tanggal
print(tgl) 

#mengakses nilai pada variabel
print("tahun", tgl.year)
print("bulan,", tgl.month)
print("tanggal", tgl.day)

#dst, lihat revrensi si atas halaman