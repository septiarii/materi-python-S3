# Mengimpor Modul Calendar
import calendar
 
# Menginput Tahun dan Bulan
yy = int(input("Masukkan Tahun: "))
mm = int(input("Masukkan Bulan: "))
 
# Menampilkan Kalender Bulanan
print(calendar.month(yy, mm))